import scrapy


class CarHomeSpider(scrapy.Spider):
    name = "car_home"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/car/"]

    def parse(self, response):
        aodi_car_name_list = response.xpath('//dl[@id=33]/dd/ul//h4/a/text()')
        aodi_car_price_list = response.xpath("//dl[@id=33]/dd/ul//div/a[@class='red']/text()")

        print('======================================================')
        car_price_len = len(aodi_car_price_list)
        for (index, item) in enumerate(aodi_car_name_list):
            car_name = item.extract()
            car_price = '暂无指导价格' if index >= car_price_len else aodi_car_price_list[index].extract()
            print(car_name, car_price)
            # break
        print('======================================================')


        pass
