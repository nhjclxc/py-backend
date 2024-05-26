import scrapy

from ..items import Scrapy04DydyttItem

'''
爬取电影天堂里面电影名称及其对应的图片构成图片和电影名称的一个图片文件
注意:电影名称是一个连接,而其对应的图片则是由电影名称对应的一个连接调转的内部连接
因此,这个任务是在练习外部跳到内部的数据爬取
'''

class DydyttSpider(scrapy.Spider):
    name = "dydytt"
    # allowed_domains必须写域名
    allowed_domains = ["dydytt.net"]
    start_urls = ["https://dydytt.net/index.htm"]

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.img_page_url_dict = {}

    def parse(self, response):
        print('+++++++++++++++++++++++++++++++++++++')

        # https://blog.csdn.net/qq_45957529/article/details/124923371
        # scrapy 用xpath爬取不到tbody的问题 这是因为 tbody 是Firefox和Chrome等浏览器自动添加的标记。 但是当使用Scrapy进行抓取时，tbody不在responseHTML中。 所以我们只要把xpath里的tbody删除即可正常爬取的数据
        a_list = response.xpath("//div[@class='co_area2'][1]/div[@class='co_content8']/ul/table/tr[position()>=2 and position()<=last()]/td[1]/a[2]")
        for a in a_list:
            # https://dydytt.net/html/gndy/dyzz/20240525/65020.html
            # /html/gndy/dyzz/20240525/65020.html
            # print(a.xpath('./@href').extract_first())
            img_page_url = 'https://' + DydyttSpider.allowed_domains[0] + a.xpath('./@href').extract_first()
            name = a.xpath('./text()').extract_first()

            # self.img_page_url_dict[name] = img_page_url
            # 继续跳转到下一个页面,并且使用parse_inner来解析源码
            # 使用meat属性来向内部的请求传递数据
            # 当多个请求之间要进行跳转且多个连接之间要进行数据传递的时候,必须使用meta来进行传递数据
            yield scrapy.Request(url=img_page_url, callback=self.parse_inner, meta={'name': name})

            # break

        print('+++++++++++++++++++++++++++++++++++++')

    def parse_inner(self, response):
        print('*******************************************')

        # 这里xpath语法要经过不断测试
        # titel = response.xpath("//div[@class='co_area2'][1]/div[@class='title_all']/h1/font/text()").extract_first()
        # print(titel)
        src = response.xpath("//div[@class='co_content8']/ul/tr[3]/td/div/td/img/@src").extract_first()
        # print(src)

        # 获取外部传入的数据
        name = response.meta['name']

        # 2、创建item对象
        item = Scrapy04DydyttItem(src=src, name=name)

        # 3、将item放如管道pipelines进行数据下载与保存的后续操作
        yield item

        print('*******************************************')
