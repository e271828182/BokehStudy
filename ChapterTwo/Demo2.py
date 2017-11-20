# -*- coding: utf-8 -*-
from bokeh.plotting import Figure, show
from bokeh.models import Circle, ColumnDataSource, LabelSet,\
    Legend, LegendItem, GlyphRenderer, HoverTool, CustomJS, Select, Line, LinearAxis, NumeralTickFormatter, Range1d
from bokeh.layouts import column

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

p2 = Figure(plot_width=400, plot_height=400, tools=[hover])
p2.circle(x='x_values', y='y_values', source=source, size=20,color='blue', alpha=0.5, legend="xValue")

labels2 = LabelSet(x='x_values', y='y_values', x_offset=0, y_offset=10, text='label_value', source=source)
p2.add_layout(labels2)


callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var f = cb_obj.value;
    x = data['x_values'];
    y = data['y_values'];
    console.log(f);
    for (i = 0; i < x.length; i++) {
            y[i] = x[i]*f;
    }
    source.change.emit();
""")
options = source.data["x_values"]
select = Select(title="Option:", value="1", options=[str(x) for x in options])
select.js_on_change('value', callback)

line = Line(x='x_values',y='y_values')
p.extra_y_ranges = {"second_y": Range1d(start=0, end=max(source.data["y_values"]), max_interval=1)}
p.add_glyph(source, line, y_range_name='second_y',name='人效')
second_y = LinearAxis(y_range_name='second_y')
p.add_layout(second_y, 'right')
p.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
p.yaxis[1].formatter = NumeralTickFormatter(format="0.2f%")

layout = column(select, p, p2)



show(layout)
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

# show(column(p, p2))