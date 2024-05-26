import scrapy

# 引入Scrapy03Dangdang02Item
from ..items import Scrapy03Dangdang02Item

import re

class ProgramPhoneSpider(scrapy.Spider):
    name = "program_phone"
    # 多页下载,时必须只写域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cid4004279.html"]

    base_url = 'https://category.dangdang.com/'


    def parse(self, response):

        # item数据结构定义
        # pipelines数据下载


        phone_list = response.xpath("//div[@id='search_nature_rg']/ul/li")

        print('-------------------------------------------------------------------------')
        print(len(phone_list))

        for phone in phone_list:
            # 1、从源码中提取数据

            # 图片路径
            src = phone.xpath("./a[@class='pic']/img/@src").extract_first()
            print(src)

            # 手机价格
            price = phone.xpath("./p/span[@class='price_n']/text()").extract_first()
            print(price)

            # 手机名称
            name = phone.xpath("./p[@class='name']/a/text()").extract_first()
            print(name)

            print('================================')

            # 2、创建item对象
            item = Scrapy03Dangdang02Item(src=src, price=price, name=name)

            # 3、将item放如管道pipelines进行数据下载与保存的后续操作
            # 使用yield的方式将数据交给管道
            yield item

            break

        print('-------------------------------------------------------------------------')

        # 多页数据的下载
        # 第一页(也就是起始页start_urls): https://category.dangdang.com/cid4004279.html
        # 第二页: https://category.dangdang.com/pg2-cid4004279.html
        # 第三页: https://category.dangdang.com/pg3-cid4004279.html
        # 因此只需要在后续的连接上加上pg2 pg3即可

        # 先获取当前页数,如何在当前页数的基础上加一

        current_url = response.url
        current_page_number = extract_page_number(current_url)
        # if current_page_number is None:
        #     # 表明当前是第一页
        #     next_url = ProgramPhoneSpider.base_url + 'pg2-' + ProgramPhoneSpider.url_type
        # else:
        #     next_url = ProgramPhoneSpider.base_url + 'pg' + str(current_page_number+1) + '-' + ProgramPhoneSpider.url_type

        if current_page_number is None:
            # 表明当前是第一页
            current_page_number = 1

        next_url = ProgramPhoneSpider.base_url + 'pg' + str(current_page_number+1) + '-cid4004279.html'

        # 执行下一页数据的解析
        # scrapy.Request表示继续执行某一个连接
        # url就是你要继续执行的连接
        # callback就是这个连接执行完成下载到数据之后,要用哪个方法来进行解析数据, 注意这里将一个函数作为对象来进行传递,因此parse函数后面不要加()
        yield scrapy.Request(url=next_url, callback=self.parse)


        pass

def extract_page_number(url):
    # 正则表达式，匹配 "pg" 后面跟着的 1 个或多个数字
    pattern = r'pg(\d+)'
    match = re.search(pattern, url)
    if match:
        return int(match.group(1))  # 返回匹配到的数字，并转换为整数
    else:
        return None  # 如果没有找到匹配项，返回 None



# # 示例 URLs
# urls = [
#     "https://category.dangdang.com/pg2-cid4004279.html",
#     "https://category.dangdang.com/pg222-cid4004279.html",
#     "https://category.dangdang.com/pg3-cid4004279.html"
# ]
#
# # 提取每个 URL 的页码
# for url in urls:
#     page_number = extract_page_number(url)
#     if page_number:
#         print(f"从 URL '{url}' 中提取的页码是: {page_number}")
#     else:
#         print(f"在 URL '{url}' 中没有找到页码")