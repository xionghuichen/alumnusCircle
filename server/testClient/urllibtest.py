#urllibtest.py
# coding=utf-8
import urllib2
import urllib
import cookielib
import json
import random
prefix = "http://localhost:8000"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
# get _xrsf
resp = urllib2.urlopen(prefix+'/')
the_page = resp.read()
print the_page

_xsrf = json.loads(json.loads(the_page)['Data'])['_xsrf']

def set_resquest(api,data,method):
    # data is dictory.
    # method can be get put delete post ?
    # get _xsrf
    for item in cj:
        if item.name == '_xsrf':
            _xsrf = item.value    
    data['_xsrf'] = _xsrf
    data = urllib.urlencode(data)
    url = prefix + api
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

def registerTest():
    api = '/register'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    the_same_phone = "151961"+str(random.randint(10000,99999))
    city = 123
    faculty_id = 71
    major_id = 1
    companny = "google China"
    admission_year = 2014
    job = "student"
    gender = 0
    password = "cxh1234567"
    name = "陈雄辉"
    # set request.
    dic[num] = {
        "city":city,
        "faculty_id":faculty_id,
        "name":name,
        "major_id":major_id,
        "company":companny,
        "admission_year":admission_year,
        "telephone":the_same_phone,
        "job":job,
        "gender":gender,
        "password":password
    }
    otherPara[num] = {}
    setMessage(message,num,"注册成功")
    num = num + 1
    dic[num] = {
        "city":city,
        "faculty_id":faculty_id,
        "name":name,
        "major_id":major_id,
        "company":companny,
        "admission_year":admission_year,
        "telephone":the_same_phone,
        "job":job,
        "gender":gender,
        "password":password
    }
    otherPara[num] = {}
    setMessage(message,num,"重复注册实例")
    num = num + 1
    #request.
    do_request(api,dic,message,"POST",otherPara)

def loginTest():
    api ='/login'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
        "password":"zp123455",
        "telephone":"15196175063"
    }
    otherPara[num] = {}
    setMessage(message,num,"密码错误")
    num = num + 1
    dic[num] = {
        "password":"cxh1234567",
        "telephone":"15196175063"
    }
    otherPara[num] = {}
    setMessage(message,num,"登陆成功")
    num = num + 1
    dic[num] = {
        "password":"cxh1234567",
        "telephone":"15196175063"
    }
    otherPara[num] = {}
    setMessage(message,num,"重复登陆")
    num = num + 1
    dic[num] = {
        "password":"zp19950310",
        "telephone":"15125861442"
    }
    otherPara[num] = {}
    setMessage(message,num,"账号不存在")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def logoutTest():
    api = "/logout"
    dic = {}
    otherPara = {}
    message = {}
    num = 0
    dic[num] = {}
    otherPara[num] = {}
    setMessage(message,num,"第1次退出账号")
    num = num + 1
    dic[num] = {}
    otherPara[num] = {}
    setMessage(message,num,"第2次退出账号")
    do_request(api,dic,message,"POST",otherPara)

def updateInfoTest():
    api = '/updateinfo'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
    }
    update_json = {
        "icon_url":"defauslts",        
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":0,
        "update_json":update_json
    }
    setMessage(message,num,"更新信息，icon_url 是 defaults")
    num += 1
    dic[num] = {
    }
    update_json = {
        "icon_url":"default",
        "job":"worker"+str(random.randint(1,120))     
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":0,
        "update_json":update_json
    }
    setMessage(message,num,"更新信息，icon_url 是 default，job 是 worker")
    num += 1
    dic[num] = {
    }
    update_json = {
        "icon_url":"default",
        "job":"worker"+str(random.randint(1,120)),
        "city":"321"      
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":0,
        "update_json":update_json
    }
    setMessage(message,num,"更新信息，icon_url 是 default，job 是 worker,city = 321")   
    num += 1
    dic[num] = {
    }
    update_json = {
        "icon_url":"default",
        "job":"worker"+str(random.randint(1,120)),
        "city":"321",
        "company":"another company"
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":0,
        "update_json":update_json
    }
    setMessage(message,num,"更新信息，icon_url 是 default，job 是 worker,city = 321,company = another company")   
    do_request(api,dic,message,"POST",otherPara)

def editTest():
    api ='/edittopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
        "description":"changed!",
        "topic_id":"57bfa306ee78507903b49a06"
    }
    otherPara[num] = {}
    setMessage(message,num,"change description")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def detailTest():
    api = '/detailtopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
        "topic_id":"57bfa306ee78507903b49a06"
    }
    otherPara[num] = {}
    setMessage(message,num,"get topic detail")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def gettypetopicTest():
    api = '/gettypetopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
    "t_cat_id":"57bdcad0d0146385e6abb6be"
    }
    otherPara[num] = {}
    setMessage(message,num,"get topic type")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def searchTopicTest():
    api = '/searchtopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
        "count":10,
        "q":"软院",
        "page":1
    }
    otherPara[num] = {}
    setMessage(message,num,"search topic")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)    


def createTopic():
    api = '/createTopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {
    }
    dic[num] = {

    }
    otherPara[num] = {
        "circle_name":"new circle",
        "circle_icon_url":"default",
        "creator_uid":123,
        "circle_type_id":1,
        "reason_message":"I love you!",
        "description":" the circle will be beautiful!"
    }
    setMessage(message,num,"create topic")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def reviewListTest():
    api = "/reviewlisttopic"
    num = 0
    dic = {}
    message ={}
    otherPara = {}
    dic[num] = {}
    otherPara[num] ={
        "result":0,
        "since_id":1,
        "limit_num":5
    }
    setMessage(message,num,"review create topic list")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def reviewTest():
    api = "/reviewResult"
    num = 0
    dic = {}
    message ={}
    otherPara = {}
    dic[num] = {}
    otherPara[num] ={
        "result":1,
        "review_id":1,
    }
    setMessage(message,num,"review topic")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

registerTest()    
loginTest()
updateInfoTest()
editTest()
detailTest()
searchTopicTest()
gettypetopicTest()
createTopic()
reviewListTest()
reviewTest()    