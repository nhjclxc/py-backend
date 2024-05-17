#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/5/17 21:14
# Module    : __init__.py.py
# explain   :

import requests

# 1. 指定url
url = "http://47.96.150.227:8080/captchaImage"
#
# 2. 发起请求
response = requests.get(url=url)
response.raise_for_status()
response.encoding='utf-8'
print(response.status_code)
print(response)
print(response.text)
json_res = response.json()
# json_res["uuid"]
# json_res.get("uuid")
print(json_res["uuid"])
print(json_res.get("uuid"))

#
# # 3. 获取响应数据
# jsonRes = response.json()
#
# # 4. 持久化数据
# print(jsonRes)

