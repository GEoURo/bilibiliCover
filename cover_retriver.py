#!/usr/bin/env python
# coding: utf-8
import json
import requests
from PIL import Image
from io import BytesIO
from Error import *


class bilibili_cover_retriver(object):
    def __init__(self, verbose=False, User_Agent=None):
        self.__verbose = verbose
        self.__image   = None
        self.__aid     = None
        self.__headers = {'User-Agent': User_Agent,
                          'Referer': 'https://www.bilibili.com'}
        
        
    
    def get(self, aid=None):
        self.__aid = str(aid)
        url = 'https://api.bilibili.com/x/web-interface/view?aid=%s' % (aid)
        response = requests.get(url, headers=self.__headers)
        contents = json.loads(response.content)

        if contents.get('code') == 0:
            pic_url = contents.get('data').get('pic')
            pic_res = requests.get(pic_url, headers=self.__headers)
            self.__image = Image.open(BytesIO(pic_res.content))
            return self.__image

        else:
            if self.__verbose:
                print("av%s不存在" % aid)

            raise aidError("av" + str(aid) +  "不存在")        


    def save(self, path='./'):
        try:
            self.__image.save(path + '/av' + str(self.__aid) + '.jpg')
        except IOError:
            if self.__verbose:
                print("路径错误或文件不存在")

if __name__ == "__main__":
    verbose = True
    path = input("请输入要保存的路径(默认为当前目录)：")
    if path == '\n':
        path = './'
    
    aid = input("请输入要获取封面的AV号：")
    
    User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    
    retriver = bilibili_cover_retriver(verbose=verbose)
    retriver.get(aid)
    retriver.save(path)