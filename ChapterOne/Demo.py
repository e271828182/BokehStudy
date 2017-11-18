# -*- coding: utf-8 -*-
from bokeh.plotting import figure
from bokeh.embed import components

# 定义一个图形布局，指定宽高，之后的元素都画在这张图上
p = figure(plot_width=400, plot_height=400)

# 在坐标轴上画出圆圈，指定坐标大小，颜色和透明度（alpha）
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# 获取生成的html，指定资源来cdn网站
script, div = components(p)

html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Bokeh Scatter Plots</title>
        <link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-0.12.10.min.css" type="text/css" />
        <script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-0.12.10.min.js"></script>

        <!-- COPY/PASTE SCRIPT HERE -->
        {}
    </head>
    <body>
    
        <!-- INSERT DIVS HERE -->
        {}
    </body>
</html>""".format(div, script)

with open('demo2.html', 'w') as f:
    f.write(html)
