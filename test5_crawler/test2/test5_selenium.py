#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/5/19 18:25
# Module    : test5_selenium.py
# explain   :

'''
使用selenium来模拟浏览器行为

pip install selenium

(1）操作谷歌浏览器驱动下载地址
http://chromedriver.storage.googleapis.com/index.html
https://developer.chrome.com/docs/chromedriver/downloads?hl=zh-cn
https://www.selenium.dev/
（2）谷歌驱动和谷歌浏览器版本之间的映射表
http://blog.csdn.net/huilan_same/article/details/51896672
（3）查看谷歌浏览器版本
谷歌浏览器右上角‐‐>帮助‐‐>关于
（4）pip install selenium
'''
import time

# 使用selenium来模拟浏览器将不在需要设置ua代理

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test1():
    # https://developer.chrome.com/docs/chromedriver/get-started?hl=zh-cn

    # 正确的chromedriver路径
    chrome_path = './chromedriver.exe'
    # 创建一个 Service 对象
    service = Service(chrome_path)

    # 设置Chrome选项（如果需要）
    chrome_options = webdriver.ChromeOptions()

    # 启动Chrome浏览器
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 打开一个网页
    url = 'https://www.jd.com/'
    driver.get(url)

    # 进行其他操作
    response = driver.page_source

    # 关闭浏览器
    driver.quit()

    print(response)



    pass


def test2():
    ''' 元素定位练习 '''

    # 1、创建驱动服务
    chrome_path = './chromedriver.exe'
    service = Service(chrome_path)

    # 2、加载驱动
    browser = webdriver.Chrome(service=service)

    # 3、打开指定网页
    url = 'https://www.baidu.com'
    browser.get(url)

    # 4、获取页面响应数据
    # response = browser.page_source

    # 5、对数据进行解析操作
    # 获取指定元素练习 by指定是要找的key，value指的是要找到value
    # 通过id查找
    # button = browser.find_element(by='id', value='su')
    # print(button)
    # input = browser.find_element(by='id', value='kw')
    # print(input)

    # 通过标签的name属性查找
    # input = browser.find_element(by='name', value='wd')
    # print(input)

    # 通过xpath语法来查找
    # input = browser.find_element(by='xpath', value='//map')
    # print(input)

    # 通过标签名称查找语法来查找
    from selenium.webdriver.common.by import By
    input = browser.find_element(by=By.TAG_NAME, value='input')
    print(input)

    # 通过css选择器来查找
    input = browser.find_element(by=By.CSS_SELECTOR, value='.hot-refresh-text')
    print(input)


    # 6、关闭浏览器
    browser.quit()

    pass

from selenium.webdriver.common.by import By

def test3():
    ''' 访问元素信息 '''
    service = Service('./chromedriver.exe')

    browser = webdriver.Chrome(service=service)

    url = 'http://www.baidu.com'
    browser.get(url)

    button = browser.find_element(by=By.ID, value='su')

    print(button.get_attribute('class'))
    print(button.get_attribute('type'))
    print(button.get_attribute('value'))

    print(button.text)
    print(button.tag_name)

    browser.quit()

    pass


def test4():
    ''' 交互 '''

    service = Service('./chromedriver.exe')

    browser = webdriver.Chrome(service=service)

    url = 'http://www.baidu.com'
    browser.get(url)

    input2 = browser.find_element(by=By.ID, value='kw')
    # 输入，给元素设置值
    input2.send_keys('当前时间')

    button = browser.find_element(by=By.ID, value='su')
    # 点击
    button.click()

    # 滚动到页面底部
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 等待一段时间以便观察滚动效果
    time.sleep(2)
    # 滚动到页面顶部
    browser.execute_script("window.scrollTo(0, 0);")

    input('模拟阻塞，防止浏览器自动关闭')
    # 退出浏览器
    # browser.quit()


    pass


def test5():
    ''' 通过headless来使用selenium '''
    # 无界面模式
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    # 设置Chrome为无头模式
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    # 启动Chrome浏览器
    driver = webdriver.Chrome(options=chrome_options)

    # 访问网页
    url = 'http://www.baidu.com'
    driver.get(url)

    # 打印页面标题
    print(driver.title)

    driver.save_screenshot('baidu.png')

    # 关闭浏览器
    # driver.quit()

    pass






if __name__ == '__main__':

    # test1()

    # test2()

    # test3()

    # test4()

    test5()



    pass