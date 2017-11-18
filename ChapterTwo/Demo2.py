# -*- coding: utf-8 -*-
from bokeh.plotting import Figure, show
from bokeh.models import Circle, ColumnDataSource

p = Figure(plot_width=400, plot_height=400)
data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

source = ColumnDataSource(data=data)

# circle = Circle(x='x_values', y='y_values', line_color='red', fill_color='navy', size=20, fill_alpha=0.5)
# p.add_glyph(source, circle)

p.circle(x='x_values', y='y_values', source=source, size=20,line_color='red', fill_color='navy', color='blue' ,alpha=0.5)


show(p)