# -*-coding:utf-8-*-

from pyecharts import Bar, Pie

# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
# bar.render()    # 生成本地 HTML 文件


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 22, 33, 44, 45, 55]

pie = Pie('饼图', title_pos='center', width=900)
pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')

pie.render()
