#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .sql import Sql
from twisted.internet.threads import deferToThread

from HouseSpider.items import HouseSpiderItem


class HousespiderPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, HouseSpiderItem):
            title = item['title']
            address = item['address']
            other = item['other']
            updateTime = item['updateTime']
            price = item['price']
            lookCount = item['lookCount']

            Sql.insert_netdata(title, address, other, updateTime, price, lookCount)

            print '插入成功'
