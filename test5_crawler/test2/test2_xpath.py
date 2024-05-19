#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/5/19 18:25
# Module    : test2_xpath.py
# explain   :

'''
pip install lxml
'''

import urllib.request
import urllib.parse
from lxml import etree

# https://www.meitu131.com/meinv/
# https://nanrenhome.cc/2047.html
# https://www.tujigu.top/photo

def test():
    url = 'https://www.tujigu.top/photo/huayang%E8%8A%B1%E6%BC%BE-20230530-vol536-%E5%B0%A4%E5%A6%AE%E4%B8%9D'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    # url = url + urllib.parse.urlencode(body)

    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request)

    res = response.read().decode('utf‐8')
    print(res)

    # https://www.tujigu.top//wp-content/uploads/fdudGDF0Ql_dU7Zw9dmXbTV-hvYrEBYxqU_3DDozdu07A1jOMxMuFGAUSxufItYD.jpg

    # html_tree = etree.HTML(res)
    # a_list = html_tree.xpath('//div/a[contains(@class, "iusc")]')
    # print(len(a_list))
    # aa = a_list[0]
    # print(aa)
    # print(aa.attrib)
    # print(aa.attrib['class'])
    # print(aa.attrib['style'])
    # print(aa.attrib['m'])


if __name__ == '__main__':
    test()
