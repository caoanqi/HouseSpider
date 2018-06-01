# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
import json
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

    urlAll = ["gongyeyuan", "wuzhong", "gusu", "gaoxin1", "xiangcheng", "wujiang"]
    areaAll = ["工业园区", "吴中", "姑苏", "高新区", "相城", "吴江"]

    def start_requests(self):
        size = len(self.urlAll)
        for i in range(0, size):
            url = self.baseUrl + self.urlAll[i] + self.suffix_url
            yield Request(url, self.parse, meta={'area': self.areaAll[i]})

    def parse(self, response):
        res = response.xpath('//div[@class="con-box"]/div[@class="list-wrap"]')
        pageCount = json.loads(res.xpath('./div[@class="page-box house-lst-page-box"]/@page-data').extract()[0])["totalPage"]
        rent_area = response.meta['area']
        for i in range(1, pageCount):
            url_path = response.url + 'pg' + str(i) + '/'
            yield Request(url_path, callback=self.get_house_renting_info, meta={'rent_area': rent_area})

    def get_house_renting_info(self, response):
        rentings = response.xpath('//div[@class="con-box"]/div[@class="list-wrap"]/ul[@class="house-lst"]/li')

        for renting in rentings:
            item = HouseSpiderItem()

            item['title'] = renting.xpath('./div[@class="info-panel"]/h2/a/text()').extract()[0]
            xiaoqu = renting.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/a/span/text()').extract()[0]
            house_room = renting.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span[@class="zone"]/span/text()').extract()[0]
            house_area = renting.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span[@class="meters"]/text()').extract()[0]
            house_room_face = renting.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span[3]/text()').extract()[0]
            item['address'] = xiaoqu  # + house_room + house_area + house_room_face

            item['other'] = renting.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="other"]/div[@class="con"]/a/text()').extract()[0]

            time = str(renting.xpath('./div[@class="info-panel"]/div[@class="col-3"]/div[@class="price-pre"]/text()').extract()[0].encode('utf-8'))
            item['updateTime'] = time.replace('更新', '')
            item['price'] = renting.xpath('./div[@class="info-panel"]/div[@class="col-3"]/div[@class="price"]/span/text()').extract()[0]
            item['lookCount'] = renting.xpath('./div[@class="info-panel"]/div[@class="col-2"]/div[@class="square"]/div/span[@class="num"]/text()').extract()[0]
            item['area'] = response.meta['rent_area']
            yield item
