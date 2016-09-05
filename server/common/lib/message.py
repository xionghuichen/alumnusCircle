#!usr/bin/env python
# coding=utf-8
# message.py
import sys
import os
reload(sys)   
sys.setdefaultencoding('utf8')  
location = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir)))+'/'
sys.path.append(location)
import time
import string
import pdb
import torndb
import modules.message
from common.variables import redis_dict

"""Message class is to deal the process of a message.
"""
class Message(object):
    def __init__(self,db):
        self._user_message = modules.message.UserMessageModule(db)
        self._circle_message = modules.message.MessageCircleModule(db)
        self._message = modules.message.MessagesListModule(db)

    @property
    def user_message(self):
        return self._user_message
    
    @property
    def circle_message(self):
        return self._circle_message
    
    @property
    def message(self):
        return self._message

    def create_message(self,type_id,circle_name=' ',circle_id=' ',reason=' '):
        """input parameter of a special type of message, then return the message id.

        Args:
            type_id: message type id, look "databases.md" for detail
            circle_name:
            circle_id:
            reason: 

        Returns:
            mid of ac_message_table.
        """
        if type_id == 1:
            # create message successfully.
            dic = {'circle_name':circle_name,'circle_id':circle_id}
        elif type_id == 2:
            # create message failed.
            dic = {'circle_name':circle_name,'reason':reason}

        mid = self.message.set_message(type_id,str(dic))
        return mid

    def init_message(self,uid):
        """After user login, we should store its update information in redis dictory.

        Args:
            uid: user id in mysql

        Returns:
            update_time: the message update time of a user. 
        """
        update_time = self.user_message.get_update_time_by_uid(uid)
        redis_dict.hset("user:"+str(uid),"update_time",update_time['update_time'])
        return update_time

    def init_message_to_all(self):
        """After server start, we should execuute this function to initial update time of every circles.

        Args:

        Returns:

        """
        result_list = self.circle_message.get_all_info()
        for value in result_list:
            ucid = value['cid']
            to_redis = value
            redis_dict.hmset("circle:"+ucid,to_redis)     

    def add_new_message_queue_to_all(self,cid):
        """After we create a new circle, we should initial its information to redis distory.

        Args:
            mc_id: message circle id. after ceate a new circle will get it.
        """
        entity = self.circle_message.get_info_by_cid(cid)
        redis_dict.hmset("circle:"+str(cid),entity)

    def deal_message_to_one(self,mid,uid):
        """ Deal a new message which is to a special user.
        We should save it in ac_message_table,ac_message_user_table
        then add this message to redis dictory of a special user..

        Args:
            mid: message id in ac_message_tabel
            uid: user id

        Returns:
            error or ok.[todo]
        """
        # in normal return 1.
        result = self.user_message.set_update_message_by_uid(uid,mid)
        if redis_dict.hexists("user:" + str(uid),"_xsrf"):
            # update user update_time.
            format_time = "%Y-%m-%d %H:%M:%S"
            update_time = time.strftime(format_time,time.localtime())
            redis_dict.hset("user:"+str(uid),"update_time",update_time)

    def deal_message_to_many(self,mid,uid_list):
        """Deal a new message which is to a user list.
        We should save it in ac_message_table,ac_message_user_table
        then add this message to redis dictory to all of user referenced.

        Args:
            mid: message id in ac_message_tabel
            uid_list: all of user referenced.

        Returns:
            error or ok.[todo]       
        """
        uid_list = self.custom_list_to_list(uid_list)
        for value in uid_list:
            self.deal_message_to_one(mid,value)

    def deal_message_to_all(self,mid,cid):
        """Deal a new message which is to all of user belong to a circle.
        We should save it in ac_message_table,ac_circle_mesage_table.
        then add this message to redis dictory to all of circle referenced.
        Args:
            mid: message id in ac_message_tabel
            cid: circle_id in ac_circle_table

        Returns:
            error or ok.[todo]       
        """
        result = self.circle_message.set_update_message_by_cid(cid,mid)
        message_update = redis_dict.hget("circle:"+str(cid),"message_queue")
        message_update = message_update+str(mid) + "_"
        redis_dict.hset("circle:"+str(cid),"message_queue",message_update)
        
    def custom_list_to_list(self,custom_list):
        """We define list as "_item_item_item", this function change it to python list.
        
        Args:
            custom_list: custom list we define.

        Returns
            message_list: python list.
        """
        custom_list = custom_list.split('_')
        print custom_list
        del custom_list[0]
        del custom_list[-1]
        message_list = [string.atoi(elem) for elem in custom_list]
        return message_list


    def __time_check_unit(self,last_update_time,update_time_now):
        """Campare last update time and update time now.

        Args:
            last_update_time:
            update_time_now:

        Returns:
        """
        format_time = "%Y-%m-%d %H:%M:%S"
        strp_now = time.strptime(update_time_now,format_time)
        strp_last = time.strptime(last_update_time,format_time)
        result = time.mktime(strp_now) - time.mktime(strp_last)
        if result >= 0:            
            return True
        else:
            return False

    def check_and_get_message(self,uid,my_circle_list,last_update_time):
        """Find user's update message [include circle message and user message.]

        Args:
            uid: user id
            last_update_time: request from client, last time user send a message.
            my_circle_list:  request from client, the circle id user has join in.
        Returns:
            message_list 
        """
        update_time_now = redis_dict.hget("user:"+str(uid),"update_time")
        if self.__time_check_unit(last_update_time,update_time_now) >= 0:
            # this update time is latter than last time, we should send message to client.
            message_list = {}
            message_id_list = self.user_message.get_message_queue_by_uid(uid)['message_queue']
            print "message _list is " + str(message_id_list)
            message_id_list = message_id_list[:-1]# delete the last char '_'
            circle_list = self.custom_list_to_list(my_circle_list)
            circle_message_id_list = ''
            for cid in circle_list:
                print "uid :" + str(uid) + " cid " + str(cid) + " update time : "+ str(last_update_time)
                update_time_now = redis_dict.hget("circle:"+str(cid),"update_time")
                print "update_time_now: "+ str(update_time_now)
                if self.__time_check_unit(last_update_time,update_time_now):
                    circle_message_id_list += self.circle_message.get_message_queue_by_cid(cid)['message_queue']
                    circle_message_id_list = circle_message_id_list[:-1]
            if message_id_list != '_':
                # get user message content.
                message_id_list = self.custom_list_to_list(message_id_list)
                message_list['user'] = self._message.get_message_by_mid_list(message_id_list)    
            if circle_message_id_list != '_':
                # get ciecle message content.
                circle_message_id_list = self.custom_list_to_list(circle_message_id_list)
                # [todo]: if circle message can be repeated, use set to delete it.
                #print "circle list before: "+str(circle_message_id_list)
                #circle_message_id_list = list(set(circle_message_id_list))
                #print "circle list  after: "+str(circle_message_id_list)                
                message_list['circle'] = self._message.get_message_by_mid_list(circle_message_id_list,last_update_time)                                                   
            return message_list
        return {}

    def return_message_check(self,code,uid,my_circle_list,last_update_time):
        """Check the status. If client receive the message or not. if not, resend it.
        
        Args:
            code: 
                0 : receive failed. 1 receive success.
            uid: user id
            last_update_time: request from client, last time user send a message.
            my_circle_list:  request from client, the circle id user has join in.

        Returns:
            
        """
        if code ==0:
            # send message again.
            return self.update_check(uid,my_circle_list,last_update_time)
        elif code == 1:
            # clear message queue.
            self.user_message.clear_message_queue(uid)

    def find_user_message(self,uid):
        """Send all of message in message_queue to client.
        [deleted]: replaced by check_and_get_message
        Args:
            uid: user id.

        Returns:
            message_content_list:[json string]
                example:
                    [{'message': u'{test}', 'type': 1}, 
                    {'message': u'{test}', 'type': 1}, 
                    {'message': u'{test}', 'type': 1}]
        """
        message_list = self.user_message.get_message_queue_by_uid(uid)
        message_list = self.custom_list_to_list(message_list['message_queue'])
        print "send message before delete :%s"%message_list
        return self._message.get_message_by_mid_list(message_list)    

 
    def update_check_user(self,id_type,uid,id,last_update_time):
        """ check if update time in server has been updated.
        Check the user in client's last update time, compare it to server.
        if last_update_time is early then update_time now. we should execute send_message
        [deleted]: replaced by check_and_get_message
        Args:
            uid: user id.
            last_update_time: client's last update time.
            id_type:string: "circle:" or "user:"

        Returns:
            True or false.
        """
        update_time_now = redis_dict.hget(id_type+str(uid),"update_time")
        print "update_time_now : %s"%update_time_now
        format_time = "%Y-%m-%d %H:%M:%S"
        strp_now = time.strptime(update_time_now,format_time)
        strp_last = time.strptime(last_update_time,format_time)
        result = time.mktime(strp_now) - time.mktime(strp_last)
        if result >= 0:
            # this update time is latter than last time, we should send message to client.
            return True
        else:
            return False

    def send_message_to_all(self,uid,my_circle_list,last_update_time):
        """ Check user's circle has update or not.
        [deleted]: replaced by check_and_get_message
        Args:
            my_circle_list: user's circle list.

        Returns:
            result_message_dict: a list dictory,return all of circle's update informations
        """

        result_message_dict = {}
        print "in send message  to all"
        for cid in circle_list:
            print "uid :" + str(uid) + " cid " + str(cid) + " update time : "+ str(last_update_time)
            redis_dict.hget("circle:"+str(cid),"update_time")
            if self.update_check("circle:",uid,cid,last_update_time):
                self.send_message_to_all(cid,last_update_time)
                circle_message_list = self.circle_message.get_message_queue_by_cid(cid,last_update_time)
                result_message_dict[cid] = circle_message_list
        return result_message_dict

    def update_check_circle(self,cid,last_update_time):
        """
        [deleted]: replaced by check_and_get_message
        """
        update_time_now = redis_dict.hget("circle:"+cid,"update_time")
        print "update_time_now : %s"%update_time_now
        format_time = "%Y-%m-%d %H:%M:%S"
        strp_now = time.strptime(update_time_now,format_time)
        strp_last = time.strptime(last_update_time,format_time)
        result = time.mktime(strp_now) - time.mktime(strp_last)
        if result >= 0:
            # this update time is latter than last time, we should send message to client.
            return True
        else:
            return False