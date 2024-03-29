#!/usr/bin/env python
# coding=utf-8
# my_feed.py
#Author ChenXionghui
"""
operate to my feed.
include:
    update 
    [needn't] delete feed
"""
import json
import logging
import urllib

import tornado.httpclient
import tornado.web
from request import RequestHandler
import base
import request

"""
To update a new feed user upload.
"""
class UpdateFeedHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(RequestHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/update'
        self.methodUsed = 'POST' 
        self.requestName = 'update'       
# [todo:]upload img to server at first.
    @request.authenticated('update')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        """
        request from client:

        POST['info_json']:
            "content":[string] the content of feed
            "topic_ids":
            "title"
            "image_urls"
            "img_str"
        """
        uid = self.get_secure_cookie('uid')
        DataJson = self.get_argument('info_json')
        Data = json.loads(DataJson)
        code = 0
        access_token = self.get_redis_dict_access_token(uid)
        # logging.info("access %s and Data %s:"%(access_token,Data))
        count,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        code = self.return_code_process(count)
        self.return_to_client(code,message,Data)
        self.finish()

"""
[needn't]

delete a feed user has upload before.
[todo]:check if the feed deleted must upload by its creator.
"""
class DeleteFeedHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(RequestHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/destroy'
        self.methodUsed = 'DELETE'
        
    @request.authenticated('delete')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        """
        Request from client:
            POST['info_json']:
                feed_id:[string] the feed you want to delete
        """
        uid = self.get_secure_cookie('uid')
        DataJson = self.get_argument('info_json')
        Data = json.loads(DataJson)
        code = 0
        access_token = self.get_user_dict(uid)[1]
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        code = self.return_code_process(count)
        self.return_to_client(code,message,Data)
        self.finish()