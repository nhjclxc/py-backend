#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/12/21 10:45
# Module    : uni_ubi_test.py
# explain   :



import requests
import time

# 获取当前时间戳（秒级）
timestamp_seconds = time.time()

# 转换为毫秒级时间戳
timestamp_milliseconds = int(timestamp_seconds * 1000)

# URL 和请求头
url = 'https://sc.uni-ubi.com/sc/api/v1/person'

personStatus = 1
current = 1
state = 1
size = 10
t = timestamp_milliseconds

headers = {
    # ':authority': 'sc.uni-ubi.com',
    # ':path': f"/sc/api/v1/person?personStatus={personStatus}&current={current}&state={state}&size={size}&t={t}",
    # ':scheme': 'https',
    'referer': 'https://sc.uni-ubi.com/person/admin/worker',
    'Token': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'User-Agent': '/gH9K4/wtVnz4qA1ltXlKb0NjQIlqiekv1IbIS5WEt/m/nc9nVgIoIUHUlxLVk7I',
    'Cookie': 'INGRESSCOOKIE=1727225328.22.8228.672021|67f6653e63135351ccc461fe0de9e1f0; HMACCOUNT=FE8AE853502F549B; lang=zh_CN; Hm_lvt_b97569d26a525941d8d163729d284198=1732502842; Hm_lvt_e8002ef3d9e0d8274b5b74cc4a027d08=1732502842; jcloud_alb_route=ad62da8c2c0ac7ba10827211d8b50cb9; Sc-Token=322D151FEE544384AE8A10820EF13A48; loginAccount=main; uniubi=B7D79F4CF951A2F6093529446C181BE46858EDB5800289E7EF84AE354A3FA08E5445BB9DF3E65A4AB743DA5EFB4644CD22690CB6014443E581D62C29D20B1242ACE91926CB8671C5A1A65AB6E903C2897B7E5B94E6583F4E2C0D0D96ADD9A447A2006F42EEAA71420FA259697AAA355D1734689984701; developerId=14666; isShowTip=true; Hm_lpvt_b97569d26a525941d8d163729d284198=1734749661; Hm_lpvt_e8002ef3d9e0d8274b5b74cc4a027d08=1734749661'
}


params = {
    'personStatus': personStatus,
    'current': current,
    'state': state,
    'size': size,
    't': t
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print('请求失败:', response.status_code)
