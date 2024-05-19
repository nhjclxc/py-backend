#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/5/19 15:20
# Module    : test1_urllib.py
# explain   :
import json
# 引入urllib
import urllib.request
import urllib.parse


def test1():
    ''' 初认urllib '''

    # 定义url
    url = 'http://www.baidu.com'

    # 发送请求
    response = urllib.request.urlopen(url)

    # 读取请求响应数据
    # content = response.read() # 默认返回二级制编码
    # 对响应数据进行utf-8解码
    content = response.read().decode('utf-8')

    print(content)


def test2():
    # 一个类型和6个方法
    url = 'http://www.baidu.com'

    response = urllib.request.urlopen(url)

    print(type(response))

    # print(response.read())

    # 读取5个字节
    # print(response.read(5))

    # 读取一行
    # print(response.readline())

    # 读取5行
    # print(response.readlines(5))

    print(response.getcode())
    print(response.geturl())
    headers = response.getheaders()
    print(headers)
    print(headers[0])
    print(headers[0][0])
    print(headers[0][1])

    pass


def test3():
    ''' 网页资源下载 '''

    # 下载网页
    # html_url = 'http://www.baidu.com'
    # urllib.request.urlretrieve(html_url, 'baidu.html')

    # 下载图片
    img_url = 'https://tse2-mm.cn.bing.net/th/id/OIP-C.WCcv0ffd9N8BsrlGMIEsWgHaLH?rs=1&pid=ImgDetMain'
    urllib.request.urlretrieve(img_url, 'lisa.jpg')


    pass


def test4():
    ''' 请求对象的定制 '''

    # https
    url = 'https://www.baidu.com'

    # 所有https请求都要带上User-Agent请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    # 封装urllib的request对象
    request = urllib.request.Request(url = url, headers = headers)

    # 执行请求
    response = urllib.request.urlopen(request)

    print(response.readlines(5))



    pass


def test5():
    ''' get方法的quote方法  --->>> 对中文进行unicode编码 '''

    url = 'https://www.baidu.com/s?wd='

    # 对中文进行编码
    name = urllib.parse.quote('王冰冰') # import urllib.parse

    url = url + name

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request)

    print(response.read().decode('utf-8'))

    pass


def test6():
    ''' urlencode的使用， 可以将多个参数进行unicode编码并且可以拼接 '''


    url = 'https://www.baidu.com/s?'

    query = {
        'wd': '王冰冰',
        'key': '电视台主持人'
    }

    url = url + urllib.parse.urlencode(query)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request)

    print(response.read().decode('utf-8'))


def test7():
    ''' post请求百度翻译案例 '''

    url = 'https://fanyi.baidu.com/sug'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    data = {
        'kw': 'you'
    }

    # 编码post数据
    # post请求方式的参数必须编码，参数是放在请求对象定制的方法中，编码之后需要调用encode方法
    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url, data=data, headers=headers)

    response = urllib.request.urlopen(request)

    print(response.read().decode('utf-8'))
    # {"errno":0,"data":[{"k":"you","v":"pron. \u4f60; \u5927\u5bb6; \u4f60\u4eec\uff0c\u60a8\u4eec; \u5404\u4f4d"},{"k":"YOU","v":"abbr. Youth Opportunities Unlimited \u9752\u5e74\u673a\u9047\u65e0\u9650; Youth "},{"k":"youg","v":"n. \u5c24\u683c\u98ce\uff08\u5730\u4e2d\u6d77\u5730\u533a\u590f\u5929\u7684\u70ed\u98ce\uff09"},{"k":"your","v":"pron. \u4f60\u7684\uff0c\u4f60\u4eec\u7684; \u5c0a; \u7389; \u4e43"},{"k":"you'd","v":"abbr. you had \u4f60\u5df2\u7ecf; you would \u4f60\u5e94\u8be5"}],"logid":77973787}

    pass


def test8():
    ''' 百度详细翻译 '''
    url = 'https://fanyi.baidu.com/ait/text/translate'

    # 加请求头一般都是为了实现反爬
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        # 'Acs-Token': '1716033689442_1716109076322_1U9tqHE2ZAtasATFyj/ePg3fsebXjR1TW0bwBFBQFpY5bsZdizppu/Uho0uH/FMgbmZbAspmnDUDeA99uqZuA73Z7LcJkOipmmINGXKQfIu7C92TiLLMpY+m5PDnFqsgt0PA/EThtuoYhpubCdPKC39uOXa21J9RBv8xvp4Ud0bQdoj0IjP8sDTpompzjCTQKOnWxCBL6URnpXRYO9jQR42PV6tKYN0I0np/8qc98+JFxrzCnVRcSf6AGNaF3ulWLyXlKUUKjhKUJ+QhRPbErb//umykZTFepnyJJqvoS6dxfa2YpztKMIt/KBMdccsMGazE6NlqAj8KUOZBraJenC4Akhj1iN1iaqPD6DFxre/DTy1wlBiPCzMo2lBP3pM3BVzD1op4PdnqZDITGXBqFwLdOuGyVp7wTyV+xSHNAL2defBQhdWR2bYJsvJpW2Q1iZ8Jw4qyik9yodcm2V2ZNaJGWPcR8LlgeVB+wqkbH3ibo4e1+JHL1dJBftRMHNip',
        'Cookie': 'BAIDUID=0336248F5EBF4362BE7AA5674D44405B:FG=1; BAIDUID_BFESS=0336248F5EBF4362BE7AA5674D44405B:FG=1; ab_sr=1.0.1_YTkyZTgxMWVhMWI5NzMwNDNmYTMxMGE2ODQwMjYwZTYxYjBhYTFkODE5NDhkOTllMDJkYmYwODNlNzkzZGI1NTdiYjkwMzg5NTBmOWExZGY4OGE1MWFiNDIxN2QxZDRkM2UxNmE4MWJiMzdhZjgyZGQzNDkyNTY5OTY5NTJkYTBjMjIxYWFjNmNiNWIwNzg0NzU4ZmNhMjk2MjE2YzFhYw==; RT="z=1&dm=baidu.com&si=131d4595-62a6-4200-b419-a3d5b5abf520&ss=lwdb0sby&sl=3&tt=3ap&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1iyh'
    }

    data = {
        "query": "you",
        "from": "en",
        "to": "zh",
        "reference": "",
        "corpusIds": [ ],
        "qcSettings": [
            "1","2","3","4","5","6","7","8","9","10","11"
        ],
        "needPhonetic": True,
        "domain": "common",
        "milliTimestamp": 1716109123285
    }


    # 编码post数据
    # post请求方式的参数必须编码，参数是放在请求对象定制的方法中，编码之后需要调用encode方法
    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url, data=data, headers=headers)

    response = urllib.request.urlopen(request)

    print(response.read().decode('utf-8'))

    pass


def test9():
    ''' 获取豆瓣电影的前100条数据 '''

    params = {
        'type': 17,
        'interval_id': '100:90',
        'start': 0,
        'limit': 20
    }
    list_dict = []
    do_request(params, list_dict)

    print(list_dict)

    pass

def do_request(params, list_dict):

    url = 'https://movie.douban.com/j/chart/top_list?'

    url = url + urllib.parse.urlencode(params)
    # print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)

    res = response.read().decode('utf-8')

    json_res = json.loads(res)

    for item in json_res:
        list_dict.append({
            'id': item['id'],
            'title': item['title'],
        })

    if(params['start'] < 40):
        params['start'] = params['start'] + 20
        do_request(params, list_dict)


def test10():
    ''' 模拟cookie登录 '''




    pass


def test11():
    ''' handel处理器 '''

    pass


if __name__ == '__main__':

    # test1()

    # test2()

    # test3()

    # test4()

    # test5()

    # test6()

    # test7()

    # test8()

    # test9()

    test10()
    pass