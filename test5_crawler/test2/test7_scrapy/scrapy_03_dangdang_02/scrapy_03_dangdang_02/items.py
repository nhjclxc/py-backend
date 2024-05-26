# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy03Dangdang02Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义管道的数据结构
    src = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()

    pass
