# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import requests
import os

class Scrapy04DydyttPipeline:

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

    def open_spider(self, spider):
        self.fp = open('move_list.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):

        print('##########################################')
        # self.download_img(item['src'], item['name'] + '.jpeg')

        self.fp.write(item['src']+ ' --- ' + item['name'] + '\n')
        print('##########################################')

        return item

    def close_spider(self, spider):
        self.fp.close()