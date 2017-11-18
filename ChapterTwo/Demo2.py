# -*- coding: utf-8 -*-
from bokeh.plotting import Figure, show
from bokeh.models import Circle, ColumnDataSource, LabelSet, Legend, LegendItem, GlyphRenderer, HoverTool


hover = HoverTool(
        tooltips=[
            ("x轴", "@x_values"),
            ("y值", "@y_values{0.2f}" )
            ],
        mode = "mouse",
        formatters={
        'date'      : 'datetime', # use 'datetime' formatter for 'date' field
        'adj close' : 'printf',   # use 'printf' formatter for 'adj close' field
        }
)
p = Figure(plot_width=400, plot_height=400, tools=[hover])
data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6],
        'label_value': ["%d%%" % (100*y) for y in [6, 7, 2, 3, 6]]}

source = ColumnDataSource(data=data)
labels = LabelSet(x='x_values', y='y_values', x_offset=0, y_offset=10, text='label_value', source=source)
p.add_layout(labels)
#
# circle = Circle(x='x_values', y='y_values', line_color='red', fill_color='navy', size=20, fill_alpha=0.5)
# p.add_glyph(source, circle)

p.circle(x='x_values', y='y_values', source=source, size=20,color='blue', alpha=0.5, legend="xValue")
# labels = LabelSet(x='x_values', y='y_values', x_offset=0, y_offset=10, text='y_values', source=source)
# p.add_layout(labels)
# circle2 = Circle(line_color='red', fill_color='navy', size=10)
# renderer = GlyphRenderer(glyph=circle)
# item = LegendItem(label="x_values", renderers=[renderer])
# legend = Legend(items=[item])
# p.add_layout(legend)

# hover = p.select_one(HoverTool)
# hover.point_policy = "follow_mouse"
# hover.tooltips = [
# ("x轴", "@x_values"),
# ("y值", "@y_values{0.2f}" )]


show(p)