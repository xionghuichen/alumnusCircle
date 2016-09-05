#!/usr/bin/env python
# coding=utf-8
# feed_list.py
"""
several kind of feed list can not been package as one class.
because the parameters are different.
the better way is create a new class for every feed list request.
The class following are public feed list and comment list. shose API need check identifier

feed_list define all of operate to feed list:

include:
get timeline feed list
get a special user's feed list.
"""
import datetime
import tornado.httpclient
import tornado.web
import json
import logging
import functools

import request
from request import RequestHandler

"""Get feed list by timeline

"""
class TimelineHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(TimelineHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/community_timeline'
        self.methodUsed = 'GET'
        self.requestName = 'timeline'

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        """
        request from client:
        page[int]:timeline page number.
        count[int]:the feed amount server return a time 
        """
        again = True
        client = tornado.httpclient.AsyncHTTPClient()
        page = self.get_argument('page')
        Data = {'page':page,'count':self.count}
        access_token = self._public_access
        code,message = yield self.public_Umeng_request(access_token,Data)
        self.return_to_client(code,message)
        self.finish()

"""
Get a special user's feed list by timeline
"""
class UserTimeLineHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(UserTimeLineHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/user_timeline'
        self.methodUsed = 'GET'
        self.count =10
        self.requestName = 'usertimeline'

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        """
            GET value page from client:
            page[integer]:[must] represent the page will return the next request.
            uid[string]:[must] reprsent the comment of a special uid
            count[int]:the feed amount server return a time             
        """
        page = self.get_argument('page')
        uid = self.get_argument('uid')
        logging.info("in usertime line handler")
        Data = {'page':page,'count':self.count,'uid':uid}
        access_token = self._public_access
#        logging.info("access_token :%s"%access_token)
        code,message = yield self.public_Umeng_request(access_token,Data)
        self.return_to_client(code,message)
        self.finish()

