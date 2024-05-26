import scrapy

'''
scrapy genspider baidu_scrapy https://www.baidu.com
'''
class BaiduScrapySpider(scrapy.Spider):
    # 爬虫名字
    name = "baidu_scrapy"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始访问的路径
    start_urls = ["https://www.baidu.com"]

    # start_urls执行的回调函数，response就是start_urls请求返回的数据
    def parse(self, response):
        print('response返回的数据', response.status)
        print('response返回的数据', response.text)
        pass

# 运行爬虫脚本：scrapy crawl 爬虫名称
# 这个爬虫名称就是name
# 本示例启动：scrapy crawl baidu_scrapy
# 如果就这样启动的话无法爬取数据，因为这样遵循robots.txt协议
# 因此，在settings.py里面将robots.txt协议关闭
# 关闭robots.txt协议：注释ROBOTSTXT_OBEY = True
