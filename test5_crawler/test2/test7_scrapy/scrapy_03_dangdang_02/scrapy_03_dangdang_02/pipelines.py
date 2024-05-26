# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import requests
import os

# 如果想要使用管道的话，那么就必须在settings里面开启管道
# ITEM_PIPELINES的注释去掉
class Scrapy03Dangdang02Pipeline:

    # 爬虫文件开始执行之前执行的方法
    def open_spider(self, spider):
        print('++++++++++++++++开始+++++++++++++++++++')

    def download_img(self, img_url, img_path):
        if img_url is None or img_path is None:
            return

        # 获取当前py文件的目录路径
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # 组合目录路径和文件夹名称
        test_folder_path = os.path.join(current_directory, 'data/')
        # 检查test文件夹是否存在，如果不存在就创建它
        if not os.path.exists(test_folder_path):
            os.makedirs(test_folder_path)

        response = requests.get(img_url)
        # 检查请求是否成功
        if response.status_code == 200:
            # 获取图片数据并保存到本地
            with open(test_folder_path + img_path, "wb") as f:
                f.write(response.content)
                print(img_path, '下载完成')

    def process_item(self, item, spider):
        # 爬虫数据下载与保存的后续操作在这里进行

        print('process_item')
        print('https:' + item['src'])
        print('/data/' + item['name'] + item['price'] + '.jpg')

        img_path = item['name'] + item['price'] + '.jpg'
        # img_path = item['name'] + item['price'] + '.jpg'
        img_path = img_path.replace(' ', '-')
        print('img_path', img_path)

        self.download_img('https:' + item['src'], img_path)
        print()


        return item

    # 爬虫文件执行之后执行的方法
    def close_spider(self, spider):
        print('--------------结束------------------')


# 一个爬虫文件开启多条管道步骤
# 1) 定义一条管道
# 2) 在settings.ITEM_PIPELINES里面加入这条自定义管道



# 1) 定义一条管道
class Scrapy03Dangdang02CustomPipeline:
    def open_spider(self, spider):
        print('++++++++++++++++自定义管道开始+++++++++++++++++++')

    # 必须写这个方法
    def process_item(self, item, spider):
        print('================自定义管道执行中===================')
        # 这个管道的业务逻辑

        # 必须写这个返回值
        return item

    def close_spider(self, spider):
        print('--------------自定义管道结束---------------------')