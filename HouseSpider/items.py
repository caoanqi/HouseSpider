# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    address = scrapy.Field()
    other = scrapy.Field()
    price = scrapy.Field()
    updateTime = scrapy.Field()
    lookCount = scrapy.Field()
    area = scrapy.Field()
    pass
