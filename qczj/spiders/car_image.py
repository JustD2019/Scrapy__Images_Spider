# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline
from qczj.items import QczjItem

class CarImageSpider(scrapy.Spider):
    name = 'car_image'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/4871.html#pvareaid=2042212']

    def parse(self, response):

        uibox = response.xpath("//div[@class='uibox']")[1:] #把全景看车图片忽略
        for box in uibox:
            img_src = box.xpath(".//ul/li/a/img/@src").getall()    #获取图片url
            img_src = list(map(lambda url:response.urljoin(url),img_src))  #增加https完善图片url
            item = QczjItem(image_urls = img_src)
            yield item

if __name__ == '__main__':
    cmdline.execute("scrapy crawl car_image".split())