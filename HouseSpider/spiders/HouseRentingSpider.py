# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re

from HouseSpider.items import HouseSpiderItem

'''
安居客 租房信息 数据抓取
两种方法能够使 requests 不被过滤: 
1. 在 allowed_domains 中加入 url 
2. 在 scrapy.Request() 函数中将参数 dont_filter=True 设置为 True
'''


class HouseRentingSpider(scrapy.Spider):
    name = 'HouseRentingSpider'
    allowed_domains = ['su.lianjia.com']
    baseUrl = 'https://su.lianjia.com/zufang/'
    suffix_url = '/'

    def start_requests(self):
        for i in range(1, 40):
            url = self.baseUrl + 'pg' + str(i) + self.suffix_url
            yield Request(url, self.parse)

    def parse(self, response):
        rentings = response.xpath('//div[@class="con-box"]/div[@class="list-wrap"]/ul[@class="house-lst"]/li')

        for renting in rentings:
            item = HouseSpiderItem()

            item['title'] = renting.xpath('./div[@class="info-panel"]/h2/a/text()').extract()[0]
            item['address'] = \
                renting.xpath(
                    './div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/a/span/text()').extract()[
                    0] + renting.xpath(
                    './div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span[@class="zone"]/span/text()').extract()[
                    0] + renting.xpath(
                    './div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span[@class="meters"]/text()').extract()[
                    0] + renting.xpath(
                    './div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span[3]/text()').extract()[0]

            item['other'] = renting.xpath(
                './div[@class="info-panel"]/div[@class="col-1"]/div[@class="other"]/div[@class="con"]/a/text()').extract()[
                0]
            item['updateTime'] = renting.xpath(
                './div[@class="info-panel"]/div[@class="col-3"]/div[@class="price-pre"]/text()').extract()[0]
            item['price'] = renting.xpath(
                './div[@class="info-panel"]/div[@class="col-3"]/div[@class="price"]/span/text()').extract()[0]
            item['lookCount'] = renting.xpath(
                './div[@class="info-panel"]/div[@class="col-2"]/div[@class="square"]/div/span[@class="num"]/text()').extract()[
                0]
            yield item
