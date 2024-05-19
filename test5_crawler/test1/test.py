#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author    : LuoXianchao
# Datetime  : 2024/5/17 21:16
# Module    : test.py
# explain   :


# with open('__init__.py', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     while line != '':
#         print(line, end='')
#         line = file.readline()
#
# print('文件读取完毕')


import requests

# pip install bs4
from bs4 import BeautifulSoup


def test1():
    url = 'http://books.toscrape.com/'
    response = requests.get(url)
    if response.ok:
        print(response.text)
    else:
        print('请求错误')


def test2():
    url = 'https://movie.douban.com/top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.ok:
        print(response.text)
    else:
        print('请求错误')


def test3():
    '''
        获取http://books.toscrape.com/里面所有书名和价格的对应关系
    :return:
    '''
    url = 'http://books.toscrape.com/'
    response = requests.get(url)
    if response.ok:
        context = response.text
        soup = BeautifulSoup(context, 'html.parser')
        # print(soup.p)
        # 查找所有价格数据
        p_list = soup.findAll('p', attrs={'class': 'price_color'})
        print(len(p_list))

        book_price_list = []
        for p in p_list:
            # print(p, p.string)
            book_price_list.append(p.string)

        # 查找所有书名
        h3_list = soup.findAll('h3')
        print(len(h3_list))
        a_list = []
        for h3 in h3_list:
            a = h3.findAll('a')
            # a_list.append(a[0])
            a_list.append(*a) # *表示py的解包操作

        book_name_list = []
        for a in a_list:
            # print(a, a.string)
            # print(a.string)
            book_name_list.append(a['title'])


        book_price_dict = {}
        index = 0
        for book_name in book_name_list:
            book_price_dict[book_name] = book_price_list[index]
            index += 1

        for book_name, book_price in book_price_dict.items():
            print(f"{book_name}要{book_price}")



    else:
        print('请求错误')


def test4(douban_all_movie_title, start = 0):
    '''
        获取https://movie.douban.com/top250的所有电影标题
    :return:
    '''

    # https://movie.douban.com/top250?start=25&filter=
    url = f"https://movie.douban.com/top250?start=${start}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.ok:
        # print(response.text)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # all_div = soup.findAll('div', attrs={'class': 'hd'})
        # for div in all_div:
        #     a = div.find('a') # 拿到所有的a标签
        #     span = a.find('span') #拿到a标签里面的第一个span标签
        #     # print(span)
        #     douban_all_movie_title.append(span.string)
        all_title_list = soup.findAll('span', attrs={'class': 'title'})
        for title in all_title_list:
            t = title.string
            # 去除原标题The Shawshank Redemption
            if not t.startswith(" / "):
                douban_all_movie_title.append(title.string)

        # 接着招下一页
        if start < 225:
            test4(douban_all_movie_title, start + 25)
    else:
        print('请求错误')

    pass

import os

# https://www.meitu131.com/meinv/
# https://nanrenhome.cc/2047.html
# https://www.tujigu.top/photo
def test5():

    base_url = 'https://www.tujigu.top'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }


    # 获取第一页的所有tab
    home_response = requests.get(base_url, headers=headers)
    pussy_list = []
    if home_response.ok:
        html = home_response.text
        soup = BeautifulSoup(html, 'html.parser')
        # pussy_list = soup.findAll('h2 > a', attrs={'rel': 'bookmark'})
        pussy_list = soup.select('h2 > a')
        print(len(pussy_list))

    for (index, pussy) in enumerate(pussy_list):
        download_file(base_url, pussy['href'], headers, pussy.text)
        if index > 3:
            break

    print('全部下载完成')


def download_file(base_url, sub_url, headers, folder_name):
    folder_name = 'pussy/' + folder_name
    # 获取当前py文件的目录路径
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # 组合目录路径和文件夹名称
    test_folder_path = os.path.join(current_directory, folder_name)
    # 检查test文件夹是否存在，如果不存在就创建它
    if not os.path.exists(test_folder_path):
        os.makedirs(test_folder_path)

    response = requests.get(base_url+sub_url, headers=headers)
    if response.ok:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        img_list = soup.findAll('img', attrs={'class': 'img-fluid'})
        for (index, img) in enumerate(img_list):
            download_url = base_url + img['src']
            # 发起GET请求获取文件内容
            response = requests.get(download_url, stream=True)
            filename = folder_name + '/' + str(index) + ".jpg"
            print(filename)
            # 确保请求成功
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    # 以二进制写入模式打开文件，并逐块写入文件内容
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
            if index > 3:
                break
    print(folder_name + '下载完成')


if __name__ == '__main__':

    # test1()

    # test2()

    # test3()

    # douban_all_movie_title = []
    # test4(douban_all_movie_title)
    # print(len(douban_all_movie_title))
    # for title in douban_all_movie_title:
    #     print(title)

    # from urllib.parse import quote
    # print(quote('IMiss爱蜜社 2023.06.14 Vol.734 九月生'))
    # print(url)

    test5()






