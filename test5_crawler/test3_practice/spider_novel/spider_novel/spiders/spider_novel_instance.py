import scrapy

from ..items import SpiderNovelItem

class SpiderNovelInstanceSpider(scrapy.Spider):
    name = "spider_novel_instance"
    allowed_domains = ["fanqienovel.com"]
    start_urls = ["https://fanqienovel.com/page/7363514807082830910"]

    def parse(self, response, **kwargs):
        chapter_list = response.xpath("//div[@class='chapter']/div[@class='chapter-item'][position()>=7 and position()<=last()]")
        index = 0
        for chapter in chapter_list:
            print(chapter)
            # /reader/7363514849046842430
            next_url = chapter.xpath('./a/@href').extract_first()
            chapter_name = chapter.xpath('./a/text()').extract_first()

            # https://fanqienovel.com/reader/7363514849046842430
            next_url = 'https://fanqienovel.com' + next_url

            yield scrapy.Request(url=next_url, callback= self.parse_inner, meta={'chapter_name': chapter_name})

            index += 1
            if index > 3:
                break

        print('小说解析完成！！！')

    def parse_inner(self, response):
        chapter_name = response.meta['chapter_name']
        print('chapter_name', chapter_name)
        content_list = response.xpath("//div[@class='muye-reader-content noselect']/div/p[@class='content']/text()")
        content = ''
        for c in content_list:
            # print(c.get())
            content += c.get()

        # print('content', content)
        item = SpiderNovelItem(chapter = chapter_name, content = content)

        yield item

        pass