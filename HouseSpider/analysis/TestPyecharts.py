# -*-coding:utf-8-*-

from pyecharts import Bar, Pie

# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
# bar.render()    # 生成本地 HTML 文件


# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 10, 10]
# v2 = [19, 22, 33, 44, 45, 55]
#
# pie = Pie('饼图', title_pos='center', width=900)
# pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
#
# pie.render()

# from pyecharts import Bar, Line
# from pyecharts.engine import create_default_environment
#
# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
#
# line = Line("我的第一个图表", "这里是副标题")
# line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
#
# env = create_default_environment("html")
# # 为渲染创建一个默认配置环境
# # create_default_environment(filet_ype)
# # file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'
#
# env.render_chart_to_file(bar, path='bar.html')
# env.render_chart_to_file(line, path='line.html')


from pyecharts import Bar

# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [5, 20, 36, 10, 75, 90]
# v2 = [10, 25, 8, 60, 20, 80]
#
# bar = Bar("柱状图数据堆叠")
#
# # bar.add('商家1', attr, v1, is_stack=True)
# # bar.add('商家2', attr, v2, is_stack=True)
#
# # bar.add('商家1', attr, v1, mark_point=["average"])
# # bar.add('商家2', attr, v2, mark_line=["min", "max"])
#
# bar.add('商家1', attr, v1, mark_point=["average"])
# bar.add('商家2', attr, v2, is_convert=True)
#
# bar.render()


# from pyecharts import Pie
#
# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 10, 10]
# pie = Pie("饼图示例")
# pie.add("", attr, v1, is_label_show=True)
# pie.render()
