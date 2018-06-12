# -*-coding:utf-8-*-

from pyecharts import Bar, Pie, Line
from HouseSpider.mysqlpipelines.sql import Sql

attr = ["工业园区", "吴中", "吴江", "高新区", "姑苏", "相城"]

min_price = []
max_price = []
# line = Line("房租分析折线图")

for i in range(6):
    min_price.append(Sql.select_min_price(attr[i]))  # 最小房租
    max_price.append(Sql.select_max_price(attr[i]))  # 最大房租

# line.add("最低房租", attr, min_price, mark_point=["average"])
# line.add("商最房租", attr, max_price, is_smooth=True, mark_line=["max", "average"])
#
# line.render()

pie = Pie("饼图示例")
pie.add("", attr, min_price, is_label_show=True)
pie.render()
