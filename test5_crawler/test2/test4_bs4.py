#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/5/19 18:25
# Module    : test4_bs4.py
# explain   :

'''
pip install bs4
pip install lxml
from bs4 import BeautifulSoup
教程：https://beautifulsoup.cn/、https://beautiful-soup-4.readthedocs.io/en/latest/、https://www.jianshu.com/p/424e037c5dd8
'''

from bs4 import BeautifulSoup

# soup = BeautifulSoup('<p>Hello world</p>', 'lxml')
# print(soup.p)


def test1():
    ''' 标签选择器 '''

    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    soup = BeautifulSoup(html_doc, 'lxml')
    print(soup.title)
    print(type(soup.title))
    print(soup.title.string)
    print(soup.head)
    print(soup.p)
    print(type(soup.p))
    print(soup.a.name)
    print(soup.a['href'])
    print(soup.a.attrs['href'])
    print(soup.a.string)
    pass


def test2():
    # 方法选择器
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="Dormouse"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'lxml')
    print(soup.findAll('a'))
    print(len(soup.findAll('a')))

    a_list = soup.findAll('a')

    for a in a_list:
        print(a)
        print(a.string)
        print('get_text:', a.get_text())

    print()
    # 增加标签的属性作为参数
    print(soup.findAll('a', {'id': 'link3'}))

    pass


def test3():
    # css选择器
    html_doc = """
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello World</h4>   
        </div>

        <div class="panel-body">
            <ul class="list" id="list-1">
               <li class="element">Foo</li>
               <li class="element">Bar</li>
               <li class="element">Jay</li>
            </ul>

            <ul class="list list-samll" id="list-2">
               <li class="element">Foo</li>
               <li class="element">Bar</li>
               <li class="element">Jay</li>
            </ul>
        </div>
        </div>
    </div>
    """
    soup = BeautifulSoup(html_doc, 'lxml')
    # 获取class为panel-heading的节点
    # print(soup.select('.panel-heading'))

    # 获取ul下的li节点
    # print(soup.select('ul > li'))

    # 获取id为list-2下的li节点
    # print(soup.select('#list-2 > li'))

    # 获取所有的ul节点
    # print(soup.select('ul'))
    # print(len(soup.select('ul')))

    # 嵌套的css选择器
    for ul in soup.select('ul'):
        print(ul.select('li'))

    pass

import urllib.request
import urllib.parse
import requests
import os


def test4():
    # 爬取boss首页，公司名称及其公司图片到村到本地
    # https://www.zhipin.com/gongsi/_zzz_c101210400/?ka=open_brand

    url = 'https://www.zhipin.com/gongsi/_zzz_c101210400/?ka=open_brand'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'Cookie': 'lastCity=101210400; __zp_seo_uuid__=4922e416-64f9-4630-a134-76eeb91ab2bc; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1716295134; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fgongsi%2F_zzz_c101210400%2F%3Fka%3Dopen_brand&s=3&g=&friend_source=0&s=3&friend_source=0; wd_guid=0dfe1084-5672-409a-a9ed-e62775c19649; historyState=state; __fid=45a415047905a101eb007b613b3d26e6; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1716296596; __zp_sseed__=Firc73gdHK00uteQH3bobsBGp7MfVR1J2J0IHnGKIFc=; __zp_sname__=1f4c22e5; __zp_sts__=1716297226346; __c=1716295134; __a=88230287.1716295134..1716295134.7.1.7.7; __zp_stoken__=7419fw5zDgncjTSYcH8KAI8KVV1hYwo7ClmPDjHl2woF4w4%2FDhWZkdGFlwq5lwqFsw4zCu1plwrZjwrl6wrrChsODecOEWMSCXsKqWMKqwrvCosSnxJXDlsWWwovCu8OBwq1BRBERJh4bEREmHhscHBoSFx0dGhIXGBgXHxpMRMKpe0xHSlY8WlhYJFhzdlFhXBFsUGVOR21tFxFHQ0FWTkvDjVfDiG7Dh1fDh3bDgl3Dh8OBVlZLQcOBw447MsOOIhrDgR8dw45KEsOLw4Nsw4lTF8ORc8KCwqxDe0RIQMOLxYBKSSxJTk5HQUxJTkk8TCbDkWzCisKhOWA5TixWTklITk5OSUpMSDJJVk8wTlY%2BSBwdFx8XN1PDilLDi8OsTkk%3D',
    }

    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request)

    res = response.read().decode('utf-8')

    # print(res)

    soup = BeautifulSoup(res, 'lxml')

    # class为company-tab-box company-list的div
    # company_div = soup.select('div > ul > li > div > a', {'class': 'company-info'})
    company_div = soup.findAll('a', {'class': 'company-info'})
    # print(company_div)

    print(len(company_div))


    # 获取当前py文件的目录路径
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_name = 'company/'
    # 组合目录路径和文件夹名称
    test_folder_path = os.path.join(current_directory, folder_name)
    # 检查test文件夹是否存在，如果不存在就创建它
    if not os.path.exists(test_folder_path):
        os.makedirs(test_folder_path)

    for company in company_div:
        # 再次使用soup来加载所有的a标签
        img_src = company.find().attrs['src']
        # print(img_src)
        company_name = company.select('div > h4')[0].string
        # print(company_name)
        # 下载保存

        # 发起GET请求获取文件内容
        img_response = requests.get(img_src, stream=True)
        filename = folder_name + company_name + ".jpg"
        print(filename)
        # 确保请求成功
        if img_response.status_code == 200:
            with open(filename, 'wb') as f:
                # 以二进制写入模式打开文件，并逐块写入文件内容
                for chunk in img_response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

    pass


if __name__ == '__main__':

    # test1()

    # test2()

    # test3()

    test4()


    pass