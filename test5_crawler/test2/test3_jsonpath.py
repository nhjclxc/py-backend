#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/5/19 18:25
# Module    : test3_jsonpath.py
# explain   :

'''
只能解析本地文件
pip install jsonpath
教程：https://blog.csdn.net/luxideyao/article/details/77802389
    https://www.bilibili.com/video/BV1Db4y1m7Ho?p=73
'''

import urllib.request
import urllib.parse
import json
import jsonpath

# json_data = json.load(open('jsonpath.json', encoding='utf-8'))
# print(json_data)

# $表示根节点
# .表示找直接子级
# ..表示所有子级
# *表示所有

# 书店所有书的作者
# res = jsonpath.jsonpath(json_data, '$.store.book[*].author')
# print(res)

# 所有的作者
# res = jsonpath.jsonpath(json_data, '$.store..author')
# print(res)

# store下面的所有元素
# res = jsonpath.jsonpath(json_data, '$.store.*')
# print(res)

# store里面所有东西的price
# res = jsonpath.jsonpath(json_data, '$.store.*.price')
# print(res)

# 第三本书 在[]里面写条件 索引从0开始
# res = jsonpath.jsonpath(json_data, '$.store.book[2]')
# print(res)

# 第三本书 @.length获取book的长度，(@.length-1)获取最后一本书的索引
# res = jsonpath.jsonpath(json_data, '$.store.book[(@.length-1)]')
# print(res)

# 前两本书
# res = jsonpath.jsonpath(json_data, '$.store.book[0,1]')
# res = jsonpath.jsonpath(json_data, '$.store.book[:2]')
# print(res)

# 所有包含isbn的书 ?()条件过滤，条件写在()里面
# res = jsonpath.jsonpath(json_data, '$.store.book[?(@.isbn)]')
# print(res)

# 价格低于10的书
# res = jsonpath.jsonpath(json_data, '$.store.book[?(@.price < 10)]')
# print(res)

# 价格低于10的书
# res = jsonpath.jsonpath(json_data, '$.*')
# print(res)
def get_taopiaopiao_data():
    # 解析淘票票里面的所有城市
    url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1716217790268_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
    headers = {
        'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'xlly_s=1; isg=BPPzog3XkdFWUl2F8nl-mg3QgvcdKIfq84W2AqWQP5JJpBJGLfqDOjM6XtRKOd_i',
        'referer': 'https://dianying.taobao.com/',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }
    request = urllib.request.Request(url, headers=headers)
    print(request)
    response = urllib.request.urlopen(request)
    print(response)
    res = response.read().decode('utf-8')
    print(res)

    # 得到()里面的数据
    def extract_parentheses_content(s):
        # 找到左括号和右括号的位置
        start = s.find('(')
        end = s.find(')', start)

        # 如果找到了括号，提取括号内的内容
        if start != -1 and end != -1:
            return s[start + 1:end]
        else:
            return None

    res = extract_parentheses_content(res)
    print(res)
    # 保存json数据到本地
    with open('taopiaopiao.json', 'w', encoding='utf-8') as fp:
        fp.write(res)


# get_taopiaopiao_data()

# 加载本地json数据
json_data = json.load(open('taopiaopiao.json', 'r', encoding='utf-8'))

regionName_list = jsonpath.jsonpath(json_data, '$.returnValue..regionName')
print(regionName_list)

