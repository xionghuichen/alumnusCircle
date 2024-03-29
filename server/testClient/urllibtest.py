#urllibtest.py
# coding=utf-8
import urllib2
import urllib
import cookielib
import json
import random
import hashlib
prefix ="http://139.196.207.155:8000"
# prefix = "http://127.0.0.1:8000"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
# get _xsrff
resp = urllib2.urlopen(prefix+'/')
the_page = resp.read()
print resp.getcode() == 200
print the_page

_xsrf = json.loads(the_page)['Data']['_xsrf']

def set_resquest(api,data,method):
    # data is dictory.
    # method can be get put delete post ?
    # get _xsrff
    for item in cj:
        if item.name == '_xsrf':
            _xsrf = item.value
    if method != 'GET':
        data['_xsrf'] = _xsrf
    data = urllib.urlencode(data)
    url = prefix + api
    if method == 'GET':
        url = url + "?"+ data
    request = urllib2.Request(url,data)
    request.get_method = lambda: method # or 'DELETE' 
    return request

def setMessage(message,num,content):
   message[num] = "No.%s "%num + content + "\r\n"

def set_info_json(dic):
    info_json = json.dumps

def do_request(api,dic,message,method,otherPara):
    count = 0
    while count < len(dic):
        info_json = json.dumps(dic[count])
        para = otherPara[count]
        para['info_json'] = info_json
        # print "do request :" + str(para) + str(ot)
        req = set_resquest(api,para,method)
        response = urllib2.urlopen(req)
        the_page = response.read()
        print message[count] + the_page
        count = count + 1   

def leave_circle():
    api = '/leave_circle'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
        "umeng_circle_id":"57d79ab1d36ef3cdf599bd89",#the circle you want to leave. this is a string get from circle list.
    }
    info_json[num] = {
    }
    message[num] = "leave circle : \n"    
    do_request(api,info_json,message,"POST",otherPara) 

def apply_circle():
    api = '/apply_circle'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
        "circle_id":"57d79ab1d36ef3cdf599bd89",
        "circle_name":"互联网创业圈",
        "reason":"我喜欢这个圈子,我想加入呢~",
        "creator_id":"118",
        # change delete icon_url
    }
    info_json[num] = {
    }
    message[num] = "clear my message list : \n"    
    do_request(api,info_json,message,"POST",otherPara) 

def checkmessage():
    api = '/checkmessage'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
    }
    info_json[num] = {
    }
    message[num] = "clear my message list : \n"    
    do_request(api,info_json,message,"POST",otherPara) 


def getcommentlist():
    api = '/get_my_comment'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
    }
    info_json[num] = {
        "count":30,
        "type":'received', # set 'received' as default. we can also set 'sent' to get all of comments I have sent.
        "page":1
    }
    message[num] = "my comment list : \n"    
    do_request(api,info_json,message,"POST",otherPara) 


def getmessage():
    api = '/getmessage'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
        'my_circle_list':'_26_28_30_33_36_35_37_27_39_',
    }
    info_json[num] = {
    }
    message[num] = "get message : \n"    
    do_request(api,info_json,message,"POST",otherPara)  


def like():
    api='/like'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        'method':'POST',# POST or DELETE stand for like and cancel like
        "feed_id":"57d2e44dd36ef3fbfcb032e4",
    }
    info_json[num] = {

    }
    message[num] = "like \n"    
    """
    num +=1
    otherPara[num] = {
        'method':'DELETE',# POST or DELETE stand for like and cancel like
        "feed_id":"57d2e44dd36ef3fbfcb032e4",
    }
    info_json[num] = {
    }    
    message[num] = "cancel like \n"    
    """
    do_request(api,info_json,message,"POST",otherPara) 


def pub_comment():
    api='/pubcomment'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {

    }
    info_json[num] = {
        "feed_id":"57d40332d36ef3a36eb2f145",
        "content":"[很长]我评论了这条动态! 我评论了这条动态!我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! "
    }
    message[num] = "pub comment  \n"    
    do_request(api,info_json,message,"POST",otherPara)

def commit_list():
    api='/commentlist'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "feed_id":"57d84b2fb9a9960f37a1072b",
        "page":1,
        "count":30
    }
    info_json[num] = {
    }
    message[num] = "comment list \n"    
    do_request(api,info_json,message,"POST",otherPara)  


def feed_detail():
    api = '/feed_detail'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "feed_id":"587f6bc7b9a9967cc4c35443"
    }
    info_json[num] = {
    }
    message[num] = "feed deatail\n"    
    do_request(api,info_json,message,"POST",otherPara)

def user_detail():
    api = '/user_detail'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "uid":'117'
    }
    info_json[num] = {
    }
    message[num] = "user deatail\n"    
    do_request(api,info_json,message,"POST",otherPara)     


def search():
    api='/search_user'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "filter_admission_year_min":0,# 0 for not filter
        "filter_admission_year_max":9999,# 9999 for not filter
        "filter_major_list":json.dumps([]),#([u'_金融_',u'_软件学院_']), # [] for not filter
        "filter_city_list": json.dumps([]), # ([u'_中国_福建_漳州_']), # [] for not filter 
        "all_match":2,# 0 for filter search. 1 for query search ,2 to get all people
        "query":"",
        "page":1,
        "size":10
    }
    info_json[num] = {
    }
    message[num] = "search,\n"    
    do_request(api,info_json,message,"POST",otherPara)     

def circle_member_list():
    api = '/circle_member_list'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
    }
    info_json[num] = {
        "count":1000,
        "topic_id":"57d835b1b9a9964cc69af298",# this is the only circle can be use when test.
        "page":1
    }
    message[num] = "circle member list .\n"    
    do_request(api,info_json,message,"POST",otherPara) 


def circle_feed_list():
    api = '/circle_feed'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
    }
    info_json[num] = {
        "count":10,
        "topic_id":"57d2dd11d36ef3fc508aee94",# this is the only circle can be use when test.
        "page":1,
        "order":0
    }
    message[num] = "feed of a special circle.\n"    
    do_request(api,info_json,message,"POST",otherPara) 

def update_feed():
    api ='/myfeed/update'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
    }
    info_json[num] = {
            "content":"4这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!",
            "topic_ids":"57d402d8b9a9965b02927330",
            "title":" 4circle feed list !",
            # "image_urls":[{'origin':'http://test1.jpg', '360':'http://test2.jpg', '750':'http://test3.jpg'}],
            "img_str":"http://tupian.qqjay.com/tou3/2016/0605/9848ad4d58f2cf2ac07a2645d66e20e6.jpg;http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg"
    }
    message[num] = "update a feed."    
    do_request(api,info_json,message,"POST",otherPara) 


def get_follow_list():
    api= '/followslist'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
    }
    info_json[num] = {
        "count":30,
        "page":1,
        "uid":36
    }
    message[num] = "get my circle list."    
    do_request(api,info_json,message,"POST",otherPara) 

def follow_test():
    api = '/follow'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "target":"follow",
        "uid":'66'
    }
    info_json[num] = {
    }
    message[num] = "follow."
    do_request(api,info_json,message,"POST",otherPara)    

def get_all_circle_test():
    api = '/get_my_circle'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {}
    info_json[num] = {
    }
    message[num] = "get my circle list."
    do_request(api,info_json,message,"POST",otherPara)    

def get_my_filter_circle_test():
    api = '/get_my_filter_circle'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {"my_filter_circle":"_14_"}
    info_json[num] = {

    }
    message[num] = "get my admin circle list."
    do_request(api,info_json,message,"POST",otherPara)   


def circle_apply_test(): 
    api ='/circle_apply_result'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "result":1,
        "apply_user_id":118,
        "apply_user_name":"白洋",
        "circle_id":"30",
        "circle_name":"互联网创业圈"
        # change
    }

    info_json[num] = {
    }
    message[num] = "agree the user apply to the circle."
    do_request(api,info_json,message,"POST",otherPara)
    """
    follow success:
    {
        "update": {
            
        },
        "response": {
            "stats": {
                "fans": 0,
                "feeds": 0
            },
            "description": "the circle will be beautiful!",
            "tags": [
                
            ],
            "icon_url": {
                "origin": null,
                "80": null,
                "160": null
            },
            "image_urls": [
                
            ],
            "custom": "{\"virtual_cid\": \"57c69d67d36ef3151eb80ba9\", \"creator_uid\": \"123\"}",
            "secret": false,
            "create_time": "2016-08-31 17:03:36",
            "has_followed": True,
            "id": "57c69d68d36ef3151eb80bac",
            "name": "new circle 983"
        }
    }
    }
    """

def registerTest():
    api = '/register'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    the_same_phone = "159961"+str(random.randint(10000,99999))
    city = u"洛阳"
    country = u"中国"
    state = u"河南"
    faculty = u"建筑设计及其理论"
    major = u"建筑学院(研)"
    companny = "google China"
    admission_year = 2014
    job = "设计师"
    gender = 0
    password = "cxh1234567"
    name = "曾博晖"
    # set request.
    info_json[num] = {
        "city":city,
        "state":state,
        "country":country,
        "faculty":faculty,
        "name":name,
        "major":major,
        "company":companny,
        "admission_year":admission_year,
        "telephone":the_same_phone,
        "job":job,
        "gender":gender,
        "password":password,
        "icon_url":"http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg"
    }
    otherPara[num] = {}
    setMessage(message,num,"注册成功")
    num = num + 1
    #request.
    do_request(api,info_json,message,"POST",otherPara)

def loginTest():
    api ='/login'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    # info_json[num] = {
    #     "password":"xcf324",
    #     "telephone":"15689236999"
    # }
    # otherPara[num] = {}
    # setMessage(message,num,"密码错误")(.*)
    # num = num + 1
    info_json[num] = {
        "password":"by123456",
        "telephone":"15851856958"
        #"password":"cxh123456",
        #"telephone":"15195867777"
    }
    otherPara[num] = {}
    setMessage(message,num,"登陆成功")
    # num = num + 1
    # info_json[num] = {
    #     "password":"zp19950310",
    #     "telephone":"15996198251"
    # }
    # otherPara[num] = {}
    setMessage(message,num,"账号不存在")
    num = num + 1
    do_request(api,info_json,message,"POST",otherPara)

def logoutTest():
    api = "/logout"
    info_json = {}
    otherPara = {}
    message = {}
    num = 0
    info_json[num] = {}
    otherPara[num] = {}
    setMessage(message,num,"第1次退出账号")
    num = num + 1
    info_json[num] = {}
    otherPara[num] = {}
    setMessage(message,num,"第2次退出账号")
    do_request(api,info_json,message,"POST",otherPara)

def updateInfoTest():
    api = '/updateinfo'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    info_json[num] = {
        'icon_url':'http://www.seu.edu.cn/319791473743423.0.jpg',
        'job':'首席架构师',
        'city':'周口',
        'state' : '河南',
        'country':'中国',
        'company': '阿里巴巴',
        'public_contact_list':json.dumps({'telephone':'15195861108'}),
        'introduction':'我是帅气的白洋哈哈哈哈哈'
    }
    setMessage(message,num,"更新信息")
    otherPara[num] = {}
    do_request(api,info_json,message,"POST",otherPara)


def editTest():
    api ='/edittopic'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    info_json[num] = {
        "description":"changed!",
        "topic_id":"57bfa306ee78507903b49a06"
    }
    otherPara[num] = {}
    setMessage(message,num,"change description")
    num = num + 1
    do_request(api,info_json,message,"POST",otherPara)

def detailTest():
    api = '/detailtopic'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    info_json[num] = {
        "topic_id":"57c69d68d36ef3151eb80bac"
    }
    otherPara[num] = {}
    setMessage(message,num,"get topic detail")
    num = num + 1
    do_request(api,info_json,message,"POST",otherPara)

def gettypetopicTest():
    api = '/gettypetopic'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    info_json[num] = {
    "t_cat_id":"57cd049d55c400f83aa1384c",
    "page":1,
    "count":10
    }
    otherPara[num] = {}
    setMessage(message,num,"get topic type")
    num = num + 1
    do_request(api,info_json,message,"POST",otherPara)

def searchTopicTest():
    api = '/searchtopic'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    info_json[num] = {
        "count":10,
        "q":"软院",
        "page":1
    }
    otherPara[num] = {}
    setMessage(message,num,"search topic")
    num = num + 1
    do_request(api,info_json,message,"POST",otherPara)    

def createTopic():
    api = '/createTopic'
    num = 0
    info_json = {}
    message = {}
    otherPara = {
    }
    info_json[num] = {

    }
    otherPara[num] = {
        "circle_name":"python开发小组",
        "circle_icon_url":"http://www.seu.edu.cn/319791473743423.0.jpg",
        "creator_uid":143,
        "creator_name":"陈雄辉",
        # "circle_type_id":"57bdcad0d0146385e6abb6be",
        "circle_type_name":"职业圈",
        "reason_message":"汇聚python开发的大神,一起交流",
        "description":" 汇聚所有python开发大神"
    }
    setMessage(message,num,"create topic")
    num = num + 1
    do_request(api,info_json,message,"POST",otherPara)

def reviewListTest():
    api = "/reviewlisttopic"
    num = 0
    info_json = {}
    message ={}
    otherPara = {}
    info_json[num] = {}
    otherPara[num] ={
        "result":0,
        "since_id":1,
        "limit_num":5
    }
    setMessage(message,num,"review create topic list")
    num = num + 1
    do_request(api,info_json,message,"GET",otherPara)

def reviewTest():
    api = "/reviewresult"
    num = 0
    info_json = {}
    message ={}
    otherPara = {}
    info_json[num] = {}
    otherPara[num] ={
        "result":1,
        "review_id":45
    }
    setMessage(message,num,"review topic")
    do_request(api,info_json,message,"POST",otherPara)
    """
{
    "message": "get umeng api successfully",
    "code": 2900,
    "Data": {
        "update": "empty",
        "response": {
            "status": 0,
            "description": "the circle will be beautiful!",
            "type_id": "57cd04ba55c400f83aa1384d",
            "icon_url": "http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg",
            "tags": "empty",
            "image_urls": "empty",
            "custom": {
                "creator_uid": "123",
                "creator_name": "刘龙飞"
            },
            "secret": false,
            "create_time": "2016-09-09 19:21:25",
            "has_followed": false,
            "creator_uid": "123",
            "id": "57d29b35d36ef3ede3235050",
            "name": "virtual_刘龙飞的圈子"
        }
    }
}
    """

def adminRegister():
    api = '/adminregister'
    num = 0
    info_json = {}
    message ={}
    otherPara = {}    
    city = u"南京"
    country = u"中国"
    state = u"江苏"
    faculty = u"机械制造及其自动化"
    major = u"机械工程学院(研)"
    companny = "google China"
    admission_year = 2014
    job = "设计师"
    gender = 0
    password = "cxh1234567"
    name = "刘龙飞"
    # set request.
    info_json[num] = {
        "city":city,
        "state":state,
        "country":country,
        "faculty":faculty,
        "name":name,
        "major":major,
        "company":companny,
        "admission_year":admission_year,
        "telephone":"15195861108",
        "job":job,
        "gender":gender,
        "password":password,
        "icon_url":"http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg"
    }
    otherPara[num] = {}
    #request.
    do_request(api,info_json,message,"POST",otherPara)    


def adminloginTest():
    api ='/login'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    password = "123456"
    m = hashlib.md5()
    m.update(password)
    psw = m.hexdigest()   
    info_json[num] = {
        "password":psw,
        "telephone":"15195861108"
    }
    otherPara[num] = {}
    setMessage(message,num,"登陆成功")
    do_request(api,info_json,message,"POST",otherPara)

def checkPhone():
    api = '/checkphone'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    info_json[num] = {
    }
    otherPara[num] = {
        "telephone":"15195861108"
    }
    setMessage(message,num,"telephone has been register")
    do_request(api,info_json,message,"POST",otherPara)    

def feedlist():
    api = '/followcircleslist'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
        "page":1,
        "count":10,
    }
    info_json[num] = {
    }
    message[num] = "my follow circle list : \n"    
    do_request(api,info_json,message,"POST",otherPara) 
# checkPhone()
# registerTest()    
# adminloginTest()
# server/common,server/handler,server/init,server/main,server/modules
loginTest()
# apply_circle()
# getcommentlist()
# circle_apply_test()
# feedlist()
# checkmessage()
#　circle_member_list()
# user_detail()
# like()
# commit_list()
# pub_comment()
# search()
# follow_test()
# get_follow_list() 
# update_feed()
# circle_feed_list()
feed_detail()
# logoutTest()
# updateInfoTest()
# editTest()
# detailTest()
# searchTopicTest()
# gettypetopicTest()
# get_all_circle_test()
# leave_circle()
# createTopic()
# reviewListTest()
#　reviewTest()   
# get_my_filter_circle_test()
# logoutTest()
# update_feed()
# adminRegister()

