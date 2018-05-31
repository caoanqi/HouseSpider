# -*-coding:utf-8-*-

from scrapy import cmdline
from HouseSpider.mysqlpipelines.sql import Sql

Sql.clear_table()

cmdline.execute("scrapy crawl HouseRentingSpider".split())

# cmdline.execute("scrapy,crawlall,--nolog".split(','))
