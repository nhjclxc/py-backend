#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/5/19 18:25
# Module    : test6_requests.py
# explain   :

'''
pip install requests

https://requests.readthedocs.io/projects/cn/zh-cn/latest/
'''

import requests


def test1():
    ''' get练习 '''
    # r = requests.get('https://api.github.com/events')
    # print(type(r))
    # print(r)
    # print(r.text)

    # get传参 例如， httpbin.org/get?key=val。
    # Requests 允许你使用 params 关键字参数，以一个字符串字典来提供这些参数
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)
    print(r.ok)
    print(r.status_code)
    print(r.raise_for_status())  # 检查是否有抛出异常
    print(r.url)
    # print(r.text)
    print(r.encoding)
    print(type(r.text))
    print(r.request)
    print(r.request.headers)
    print(r.headers)
    print(r.headers['Content-Type'])
    print(r.headers.get('content-type'))
    # 将响应转化为json
    import json
    print(type(json.loads(r.text)))
    # print(r.json())
    print(type(r.json()))

    # 下载二级制文件
    img_url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
    response = requests.get(img_url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 获取图片数据并保存到本地
        with open("baidu_image.jpg", "wb") as f:
            f.write(response.content)

    # 定制请求头
    url = 'https://api.github.com/some/endpoint'
    headers = {
        'user-agent': 'my-app/0.0.1',
        'token': 'qwertyui',
    }

    res = requests.get(url, headers=headers)

    print(res.request)
    print(res.request.headers)

    pass


def test2():
    ''' 模拟post请求 '''
    data = {
        'key': 'value',
        'key2': 'value2',
    }
    # data = (('key1', 'value1'), ('key1', 'value2'))
    # 这个是表单application/x-www-form-urlencoded格式
    # res = requests.post('http://httpbin.org/post', data = data)
    # 以下是application/json格式
    res = requests.post('http://httpbin.org/post', json = data)


    print(res.request)
    print(res.request.headers)
    print(res.request.body)
    print(res.text)

    print()
    print()

    # post传输文件
    url = 'http://httpbin.org/post'
    files = {'file': open('img_1.png', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)


    pass

import json
def test3():
    ''' 类似于chatgpt一样的流式请求 '''
    # https://requests.readthedocs.io/projects/cn/zh-cn/latest/user/advanced.html#streaming-requests

    r = requests.get('http://httpbin.org/stream/20', stream=True)

    if r.encoding is None:
        r.encoding = 'utf-8'

    for line in r.iter_lines():

        # filter out keep-alive new lines
        if line:
            decoded_line = line.decode('utf-8')
            print(json.loads(decoded_line))
    pass


def test4():
    ''' 配置代理 '''
    import requests

    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }

    requests.get("http://example.org", proxies=proxies)

    # 要为某个特定的连接方式或者主机设置代理，使用 scheme://hostname 作为 key， 它会针对指定的主机和连接方式进行匹配。
    # proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}


    pass




def get_chrome_driver():
    ''' 获取selenium驱动 '''
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    # 设置Chrome为无头模式
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    # 启动Chrome浏览器
    driver = webdriver.Chrome(options=chrome_options)

    return driver

    # # 访问网页
    # url = 'http://www.baidu.com'
    # driver.get(url)
    #
    # # 打印页面标题
    # print(driver.title)
    #
    # driver.save_screenshot('baidu.png')
    #
    # # 关闭浏览器
    # # driver.quit()

def grayscale_image(image_obj):
    ''' 将图片转化为灰度图片 '''
    img = image_obj.convert("L")  # 转灰度
    pixdata = img.load()
    w, h = img.size
    threshold = 160  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def delete_spot(image_obj):
    ''' 图片降噪 '''
    data = image_obj.getdata()
    w, h = image_obj.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]  # 中央像素点像素值
            if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                # 判断上下左右的黑色像素点总个数
                if top_pixel < 10:
                    black_point += 1
                if left_pixel < 10:
                    black_point += 1
                if down_pixel < 10:
                    black_point += 1
                if right_pixel < 10:
                    black_point += 1
                if black_point < 1:
                    image_obj.putpixel((x, y), 255)
                black_point = 0
    # images.show()
    return image_obj

import re  # 用于正则
def decode_iamge_code_local():
    # 解析本地图片
    from PIL import Image
    from io import BytesIO
    import pytesseract
    # 设置tesseract位置
    pytesseract.pytesseract.tesseract_cmd = r'D:\develop\Tesseract-OCR\tesseract.exe'  # 替换为你的Tesseract安装路径

    # 加载验证码图片
    iamge_path = 'iamge_code.png'
    captcha_image = Image.open(iamge_path)

    # captcha_image = grayscale_image(captcha_image)
    # captcha_image = delete_spot(captcha_image)

    # 使用Tesseract进行OCR识别
    captcha_text = pytesseract.image_to_string(captcha_image, lang='chi_sim')
    resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", captcha_text)  # 去除识别出来的特殊字符
    result_four = resultj[0:4]  # 只获取前4个字符
    print(resultj)

    # 打印识别结果
    print("验证码内容:", captcha_text)

# decode_iamge_code_local()


def decode_iamge_code(captcha_url):
    '''
        pip install pytesseract pillow
    '''


    # https://blog.csdn.net/qq_38463737/article/details/109679007
    # https://digi.bib.uni-mannheim.de/tesseract/ 【直接下载最新版】
    # https://github.com/UB-Mannheim/tesseract/wiki

    # 解析网络图片
    from PIL import Image
    from io import BytesIO
    import pytesseract
    # 设置tesseract位置
    pytesseract.pytesseract.tesseract_cmd = r'D:\develop\Tesseract-OCR\tesseract.exe'  # 替换为你的Tesseract安装路径

    # 下载验证码图片
    # captcha_url = "https://so.gushiwen.cn/RandCode.ashx"
    response = requests.get(captcha_url)

    print(response.status_code)
    # 检查是否成功下载图片
    if response.status_code == 200:

        with open('iamge_code.png', 'wb') as fp:
            fp.write(response.content)
        # 将图片数据转换为Image对象
        captcha_image = Image.open(BytesIO(response.content))
        # captcha_image = Image.open('iamge_code.png')


        # 使用Tesseract进行OCR识别

        # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
        captcha_text = pytesseract.image_to_string(captcha_image, lang='chi_sim')
        # captcha_text = pytesseract.image_to_string(captcha_image)

        # 打印识别结果
        print("验证码内容:", captcha_text)

        print("验证码内容captcha_text[:4]:", captcha_text[:4])
        return captcha_text
    else:
        print("无法下载验证码图片")
        return None

# 检查字符串是否为空串
def is_empty_string(s):
    return s is None or len(s) == 0

# print(is_empty_string(None))
# print(is_empty_string(''))
# print(is_empty_string('aa'))

from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test5():
    ''' 古诗文网登录练习 '''
    # https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx

    # 登录接口 post请求
    # url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    # 请求数据 表单格式
    '''
        __VIEWSTATE: oexvF2HMpmDXgt3kNetxy4ENbJ5pXwLzcy1zZCJlju3fdysmWrlQcLk+DHhO/S54F2+149yJJRfCLe0kRa73ZK0aQcVkGaRgsUXt35zSiQN6ZmrAV7cB945QDqYWVVjQryJEbLQViKnmNZbEkBPsaqlK4aA=
        __VIEWSTATEGENERATOR: C93BE1AE
        from: https://www.gushiwen.cn/
        email: [用户名]
        pwd: [密码]
        code: [验证码]
        denglu: 登录
        
        其中 __VIEWSTATE和__VIEWSTATEGENERATOR是动态的在页面里面获取的，要通过解析页面的方式来获取
    '''

    # 1、访问页面获取__VIEWSTATE和__VIEWSTATEGENERATOR的动态数据
    page_url = 'https://so.gushiwen.cn/user/login.aspx'
    # driver = get_chrome_driver()
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(page_url)

    # # 获取图片验证码
    # # imgCode = driver.find_element(by=By.ID, value='imgCode')
    # # imgCodeSrc = imgCode.get_attribute('src')
    #
    # # https://so.gushiwen.cn/RandCode.ashx
    # # 下载验证码图片
    # # captcha_url = "https://so.gushiwen.cn/RandCode.ashx"
    # response = requests.get(imgCodeSrc)
    #
    # print(response.status_code)
    # # 检查是否成功下载图片
    # if response.status_code == 200:
    #
    #     with open('iamge_code.png', 'wb') as fp:
    #         fp.write(response.content)
    # print('captcha_text', captcha_text)

    captcha_text = input('请输入验证码：')


    # 获取元素
    viewstate_input = driver.find_element(by=By.ID, value='__VIEWSTATE')
    viewstategenerator_input = driver.find_element(by=By.ID, value='__VIEWSTATEGENERATOR')
    email_input = driver.find_element(by=By.ID, value='email')
    pwd_input = driver.find_element(by=By.ID, value='pwd')
    code_input = driver.find_element(by=By.ID, value='code')
    login_button = driver.find_element(by=By.ID, value='denglu')

    email_input.send_keys('19329051078')
    pwd_input.send_keys('lxc123456')
    code_input.send_keys(captcha_text)
    login_button.click()

    with open('gushiwen.html', 'w', encoding='utf-8') as fp:
        fp.write(driver.page_source)

    # 阻塞窗口
    input('')


    pass


if __name__ == '__main__':
    # test1()

    # test2()

    # test3()

    # test4()

    test5()

    # decode_iamge_code_local()
    # decode_iamge_code("https://so.gushiwen.cn/RandCode.ashx")


    # r = requests.put('http://httpbin.org/put', data = {'key':'value'})
    # r = requests.delete('http://httpbin.org/delete')
    # r = requests.head('http://httpbin.org/get')
    # r = requests.options('http://httpbin.org/get')

    pass
