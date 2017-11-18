# -*- coding: utf-8 -*-
from bokeh.plotting import figure, Figure, output_file, show
from bokeh.embed import components

# 定义一个图形布局，指定宽高，之后的元素都画在这张图上
p = Figure(plot_width=400, plot_height=400)

# 在坐标轴上画出圆圈，指定坐标大小，颜色和透明度（alpha）
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

show(p)