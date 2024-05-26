import scrapy
import requests

class ProgramBookSpider(scrapy.Spider):
    name = "program_book"
    allowed_domains = ["e.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cid4004279.html"]

    def download_img(self, img_url, img_path):
        if img_url is None or img_path is None:
            return

        response = requests.get(img_url)
        # 检查请求是否成功
        if response.status_code == 200:
            # 获取图片数据并保存到本地
            with open(img_path, "wb") as f:
                f.write(response.content)
                print(img_path, '下载完成')

    def parse(self, response):
        # 根数据
        phone_list = response.xpath("//div[@id='search_nature_rg']/ul/li")

        print('-------------------------------------------------------------------------')
        print(len(phone_list))

        index = 0
        for phone in phone_list:
            '''
            print(phone)
            print('==============')
            # 提取phone这个selector对象指向的标签的title属性
            print(phone.xpath('./@title'))
            print(phone.xpath('./@title').extract())
            print(phone.xpath('./@title').extract_first())

            print('==============')
            # .表示从phone的这一级开始查找，也就是相对路径
            print(phone.xpath('./p'))
            print(phone.xpath('/p')) # 错误写法，必须加上一个.
            print(phone['title'])
            break
            
            '''
            # 图片路径
            scr = phone.xpath("./a[@class='pic']/img/@src").extract_first()
            print(scr)

            # 手机价格
            price = phone.xpath("./p/span[@class='price_n']/text()").extract_first()
            print(price)

            # 手机名称
            name = phone.xpath("./p[@class='name']/a/text()").extract_first()
            print(name)

            self.download_img('https:' + scr, name + price + '.jpg')

            print('================================')

            index += 1
            if index > 5:
                break

        print('-------------------------------------------------------------------------')

        pass
