# 欢迎，一起学习bokeh
Bokeh可以基于python自动生成js代码，用来展现各式各样的图形。初学者可以花几分钟开一下，或许帮你少踩坑。
## Chapter One-Bokeh做了什么
```python
# -*- coding: utf-8 -*-
from bokeh.plotting import figure, output_file, show
from bokeh.plotting import figure

# 输出到一个静态的html页面
output_file("Demo1.html")

# 定义一个图形布局，指定宽高，之后的元素都画在这张图上
p = figure(plot_width=400, plot_height=400)

# 在坐标轴上画出圆圈，指定坐标大小，颜色和透明度（alpha）
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# 在浏览器上打开生成的页面
show(p)
```
以上代码得到的图形如下

![Image](./ChapterOne/1.PNG)

查看页面源码（或者打开生成的html文件，浏览器地址栏指出了文件路径），可以发现
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Bokeh Plot</title>
        
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-0.12.10.min.css" type="text/css" />
        
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-0.12.10.min.js"></script>
<script type="text/javascript">
    Bokeh.set_log_level("info");
</script>
        <style>
          html {
            width: 100%;
            height: 100%;
          }
          body {
            width: 90%;
            height: 100%;
            margin: auto;
          }
        </style>
    </head>
    <body>
        
        <div class="bk-root">
            <div class="bk-plotdiv" id="a8f2c044-c093-4381-bf25-4b73e4728aea"></div>
        </div>
        
        <script type="text/javascript">
            (function() {
          var fn = function() {
            Bokeh.safely(function() {
              (function(root) {
                function embed_document(root) {
                  var docs_json = {"fef2da18-6a5d-4f27-8611-f4279b141215":{"roots":{"references":[{"attributes":{"source":{"id":"e9b7c248-e551-4cfb-b336-40106975318e","type":"ColumnDataSource"}},"id":"c9f1373d-39e2-4c8c-abfc-65008abe0688","type":"CDSView"},{"attributes":{"overlay":{"id":"3272077c-2f47-4132-ac08-14994a0f3af1","type":"BoxAnnotation"}},"id":"0fd270a0-47d5-461f-890d-d55efa7d98f7","type":"BoxZoomTool"},{"attributes":{"formatter":{"id":"25924213-e6ae-45d3-9853-faabd32debd1","type":"BasicTickFormatter"},"plot":{"id":"5b3f616f-5da2-4ee4-a8ca-c07834c5d9c2","subtype":"Figure","type":"Plot"},"ticker":{"id":"135bb74f-48af-438b-9a9c-572bc9404304","type":"BasicTicker"}},"id":"df2cc63d-c3a1-42a1-a8f4-e1464d52b2bd","type":"LinearAxis"},{"attributes":{"below":[{"id":"6639c602-f97c-4e31-8329-22b37c0cf733","type":"LinearAxis"}],"left":[{"id":"df2cc63d-c3a1-42a1-a8f4-e1464d52b2bd","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"6639c602-f97c-4e31-8329-22b37c0cf733","type":"LinearAxis"},{"id":"5ad214cd-8cec-4bf5-96c4-06faee9e9930","type":"Grid"},{"id":"df2cc63d-c3a1-42a1-a8f4-e1464d52b2bd","type":"LinearAxis"},{"id":"82962a6a-16ef-4430-9b6d-2dd4816e2bff","type":"Grid"},{"id":"3272077c-2f47-4132-ac08-14994a0f3af1","type":"BoxAnnotation"},{"id":"b177f56e-b7ee-4436-804e-7b22ee9354f5","type":"GlyphRenderer"}],"title":{"id":"3c4d2d2f-c405-4c34-ad77-8a22f43030ec","type":"Title"},"toolbar":{"id":"d4fd4cb6-9395-4097-95f9-e89d23197abf","type":"Toolbar"},"x_range":{"id":"e42e3c5d-ca61-4ab2-a33e-48e9522755ac","type":"DataRange1d"},"x_scale":{"id":"a3ff54d6-a4ae-426e-95f4-1b5fa86dde13","type":"LinearScale"},"y_range":{"id":"9e3f38e6-9c9b-473b-8fc8-1e5c9b628c84","type":"DataRange1d"},"y_scale":{"id":"18c37411-815e-4c0b-a0f6-f31527982f60","type":"LinearScale"}},"id":"5b3f616f-5da2-4ee4-a8ca-c07834c5d9c2","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"25924213-e6ae-45d3-9853-faabd32debd1","type":"BasicTickFormatter"},{"attributes":{},"id":"fa87bba0-5d7b-44c9-8111-7f480da26abb","type":"WheelZoomTool"},{"attributes":{},"id":"18e6b457-d182-4207-a347-fa2b2d0aa13e","type":"SaveTool"},{"attributes":{"callback":null},"id":"9e3f38e6-9c9b-473b-8fc8-1e5c9b628c84","type":"DataRange1d"},{"attributes":{"callback":null,"column_names":["y","x"],"data":{"x":[1,2,3,4,5],"y":[6,7,2,4,5]}},"id":"e9b7c248-e551-4cfb-b336-40106975318e","type":"ColumnDataSource"},{"attributes":{},"id":"8b7e0c37-5383-4f6c-a3a6-63d87a690529","type":"BasicTicker"},{"attributes":{},"id":"a3ff54d6-a4ae-426e-95f4-1b5fa86dde13","type":"LinearScale"},{"attributes":{},"id":"3572ad84-e29e-4eb7-8547-d254e846f472","type":"HelpTool"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":20},"x":{"field":"x"},"y":{"field":"y"}},"id":"1cd66376-7760-46b6-8d28-276b488f03f6","type":"Circle"},{"attributes":{},"id":"a6b9b833-00b4-4559-9503-ef24907bc25c","type":"ResetTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"3272077c-2f47-4132-ac08-14994a0f3af1","type":"BoxAnnotation"},{"attributes":{"formatter":{"id":"6ef54f62-cdb0-410b-93ce-3b5a583126db","type":"BasicTickFormatter"},"plot":{"id":"5b3f616f-5da2-4ee4-a8ca-c07834c5d9c2","subtype":"Figure","type":"Plot"},"ticker":{"id":"8b7e0c37-5383-4f6c-a3a6-63d87a690529","type":"BasicTicker"}},"id":"6639c602-f97c-4e31-8329-22b37c0cf733","type":"LinearAxis"},{"attributes":{},"id":"6ef54f62-cdb0-410b-93ce-3b5a583126db","type":"BasicTickFormatter"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"95790c42-0f0c-42d6-8f5a-5d32b63a1992","type":"PanTool"},{"id":"fa87bba0-5d7b-44c9-8111-7f480da26abb","type":"WheelZoomTool"},{"id":"0fd270a0-47d5-461f-890d-d55efa7d98f7","type":"BoxZoomTool"},{"id":"18e6b457-d182-4207-a347-fa2b2d0aa13e","type":"SaveTool"},{"id":"a6b9b833-00b4-4559-9503-ef24907bc25c","type":"ResetTool"},{"id":"3572ad84-e29e-4eb7-8547-d254e846f472","type":"HelpTool"}]},"id":"d4fd4cb6-9395-4097-95f9-e89d23197abf","type":"Toolbar"},{"attributes":{"callback":null},"id":"e42e3c5d-ca61-4ab2-a33e-48e9522755ac","type":"DataRange1d"},{"attributes":{},"id":"95790c42-0f0c-42d6-8f5a-5d32b63a1992","type":"PanTool"},{"attributes":{},"id":"18c37411-815e-4c0b-a0f6-f31527982f60","type":"LinearScale"},{"attributes":{},"id":"135bb74f-48af-438b-9a9c-572bc9404304","type":"BasicTicker"},{"attributes":{"plot":null,"text":""},"id":"3c4d2d2f-c405-4c34-ad77-8a22f43030ec","type":"Title"},{"attributes":{"dimension":1,"plot":{"id":"5b3f616f-5da2-4ee4-a8ca-c07834c5d9c2","subtype":"Figure","type":"Plot"},"ticker":{"id":"135bb74f-48af-438b-9a9c-572bc9404304","type":"BasicTicker"}},"id":"82962a6a-16ef-4430-9b6d-2dd4816e2bff","type":"Grid"},{"attributes":{"data_source":{"id":"e9b7c248-e551-4cfb-b336-40106975318e","type":"ColumnDataSource"},"glyph":{"id":"2465510d-d4c5-4e22-ac10-f27ef3e42ba0","type":"Circle"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1cd66376-7760-46b6-8d28-276b488f03f6","type":"Circle"},"selection_glyph":null,"view":{"id":"c9f1373d-39e2-4c8c-abfc-65008abe0688","type":"CDSView"}},"id":"b177f56e-b7ee-4436-804e-7b22ee9354f5","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"5b3f616f-5da2-4ee4-a8ca-c07834c5d9c2","subtype":"Figure","type":"Plot"},"ticker":{"id":"8b7e0c37-5383-4f6c-a3a6-63d87a690529","type":"BasicTicker"}},"id":"5ad214cd-8cec-4bf5-96c4-06faee9e9930","type":"Grid"},{"attributes":{"fill_alpha":{"value":0.5},"fill_color":{"value":"navy"},"line_alpha":{"value":0.5},"line_color":{"value":"navy"},"size":{"units":"screen","value":20},"x":{"field":"x"},"y":{"field":"y"}},"id":"2465510d-d4c5-4e22-ac10-f27ef3e42ba0","type":"Circle"}],"root_ids":["5b3f616f-5da2-4ee4-a8ca-c07834c5d9c2"]},"title":"Bokeh Application","version":"0.12.10"}};
                  var render_items = [{"docid":"fef2da18-6a5d-4f27-8611-f4279b141215","elementid":"a8f2c044-c093-4381-bf25-4b73e4728aea","modelid":"5b3f616f-5da2-4ee4-a8ca-c07834c5d9c2"}];
              
                  root.Bokeh.embed.embed_items(docs_json, render_items);
                }
              
                if (root.Bokeh !== undefined) {
                  embed_document(root);
                } else {
                  var attempts = 0;
                  var timer = setInterval(function(root) {
                    if (root.Bokeh !== undefined) {
                      embed_document(root);
                      clearInterval(timer);
                    }
                    attempts++;
                    if (attempts > 100) {
                      console.log("Bokeh: ERROR: Unable to embed document because BokehJS library is missing")
                      clearInterval(timer);
                    }
                  }, 10, root)
                }
              })(window);
            });
          };
          if (document.readyState != "loading") fn();
          else document.addEventListener("DOMContentLoaded", fn);
        })();
        
        </script>
    </body>
</html>
```
从这段HTML中可以发现两个json对象：render_items和docs_json，图形的数据就在doc_json中。同时，有个class为"bk-root"的div元素来展示图形，另外自动引入了cdn网站的css和js文件。
我们可以通过file_html函数获取到，print函数打印出来的内容与上面文本一样
```python
# -*- coding: utf-8 -*-
from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN

# 定义一个图形布局，指定宽高，之后的元素都画在这张图上
p = figure(plot_width=400, plot_height=400)

# 在坐标轴上画出圆圈，指定坐标大小，颜色和透明度（alpha）
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# 获取生成的html，指定资源来cdn网站
html = file_html(p, CDN)
print(html)
```
或者，我们可以通过components函数方式分别获取到js和html代码
```python
# -*- coding: utf-8 -*-
from bokeh.plotting import figure
from bokeh.embed import components

# 定义一个图形布局，指定宽高，之后的元素都画在这张图上
p = figure(plot_width=400, plot_height=400)

# 在坐标轴上画出圆圈，指定坐标大小，颜色和透明度（alpha）
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# 获取生成的html，指定资源来cdn网站
script, div = components(p)
print(script)
print("---------------------------------------------")
print(div)
```
以上输出内容如下:
```html
<script type="text/javascript">
    (function() {
  var fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
          var docs_json = {"2f812de8-0d2c-49f5-be66-97b9f1c487a0":{"roots":{"references":[{"attributes":{},"id":"8f705dd6-5588-4376-b1d7-6183c7478e39","type":"LinearScale"},{"attributes":{"data_source":{"id":"44edcec5-ab99-40c4-a0bd-602dbc6df83a","type":"ColumnDataSource"},"glyph":{"id":"d9cefcc3-2c7f-4692-b7d3-28c768415d1d","type":"Circle"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"60f71218-c35d-4455-886c-d14d4ae5281f","type":"Circle"},"selection_glyph":null,"view":{"id":"688c9cbe-e27b-4c19-bb8a-01a93a32b0c0","type":"CDSView"}},"id":"310ba9e4-c8de-4590-9dff-59849ed6e70b","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"14dbd1d9-9ce6-4015-be6a-5c09e4f37208","subtype":"Figure","type":"Plot"},"ticker":{"id":"97406f89-7ff6-40bd-9b18-1c9170cf8361","type":"BasicTicker"}},"id":"1e4bd542-940c-4e7e-8d77-95374c527896","type":"Grid"},{"attributes":{"fill_alpha":{"value":0.5},"fill_color":{"value":"navy"},"line_alpha":{"value":0.5},"line_color":{"value":"navy"},"size":{"units":"screen","value":20},"x":{"field":"x"},"y":{"field":"y"}},"id":"d9cefcc3-2c7f-4692-b7d3-28c768415d1d","type":"Circle"},{"attributes":{"below":[{"id":"63c4296e-e360-4fc3-9e4f-d24a07dc2834","type":"LinearAxis"}],"left":[{"id":"2c808025-51e5-4303-b4c2-f67c7fffdfde","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"63c4296e-e360-4fc3-9e4f-d24a07dc2834","type":"LinearAxis"},{"id":"1e4bd542-940c-4e7e-8d77-95374c527896","type":"Grid"},{"id":"2c808025-51e5-4303-b4c2-f67c7fffdfde","type":"LinearAxis"},{"id":"09f2945a-4134-43d3-9fe1-566609d62f48","type":"Grid"},{"id":"ce640f8a-963c-4c94-886f-a2eb7eb23cc3","type":"BoxAnnotation"},{"id":"310ba9e4-c8de-4590-9dff-59849ed6e70b","type":"GlyphRenderer"}],"title":{"id":"f1ba7d96-c1b2-4dbe-b66c-69ff80957548","type":"Title"},"toolbar":{"id":"1ad7400c-322d-47ef-8721-874c50846f25","type":"Toolbar"},"x_range":{"id":"3787f820-882d-4051-bbfd-2eecf043316d","type":"DataRange1d"},"x_scale":{"id":"8f705dd6-5588-4376-b1d7-6183c7478e39","type":"LinearScale"},"y_range":{"id":"18f55766-8bb9-4fc2-b4f5-9f7fd293203e","type":"DataRange1d"},"y_scale":{"id":"254d2985-7573-4730-9cdf-b498515aa7bf","type":"LinearScale"}},"id":"14dbd1d9-9ce6-4015-be6a-5c09e4f37208","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"f399cf76-3b8b-431d-9685-badb3892de48","type":"BasicTickFormatter"},{"attributes":{"formatter":{"id":"f399cf76-3b8b-431d-9685-badb3892de48","type":"BasicTickFormatter"},"plot":{"id":"14dbd1d9-9ce6-4015-be6a-5c09e4f37208","subtype":"Figure","type":"Plot"},"ticker":{"id":"970209c7-882c-4f52-8c9d-64756f30afac","type":"BasicTicker"}},"id":"2c808025-51e5-4303-b4c2-f67c7fffdfde","type":"LinearAxis"},{"attributes":{"callback":null},"id":"3787f820-882d-4051-bbfd-2eecf043316d","type":"DataRange1d"},{"attributes":{"callback":null,"column_names":["y","x"],"data":{"x":[1,2,3,4,5],"y":[6,7,2,4,5]}},"id":"44edcec5-ab99-40c4-a0bd-602dbc6df83a","type":"ColumnDataSource"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"f53ad2c7-aed9-43f9-b732-5b2aa27e52a7","type":"PanTool"},{"id":"80ff822f-ac4e-49c4-9665-2523ca6e95f7","type":"WheelZoomTool"},{"id":"180ebdf4-254b-4664-b9ad-183dfbeec172","type":"BoxZoomTool"},{"id":"148fb013-6116-42b9-8aa3-b5191ddddeb8","type":"SaveTool"},{"id":"a8f2cae6-5325-43f8-afeb-e889c8d29826","type":"ResetTool"},{"id":"eeb4abc3-1768-4764-917b-e86e718748c7","type":"HelpTool"}]},"id":"1ad7400c-322d-47ef-8721-874c50846f25","type":"Toolbar"},{"attributes":{},"id":"a8f2cae6-5325-43f8-afeb-e889c8d29826","type":"ResetTool"},{"attributes":{"plot":null,"text":""},"id":"f1ba7d96-c1b2-4dbe-b66c-69ff80957548","type":"Title"},{"attributes":{},"id":"148fb013-6116-42b9-8aa3-b5191ddddeb8","type":"SaveTool"},{"attributes":{},"id":"80ff822f-ac4e-49c4-9665-2523ca6e95f7","type":"WheelZoomTool"},{"attributes":{"overlay":{"id":"ce640f8a-963c-4c94-886f-a2eb7eb23cc3","type":"BoxAnnotation"}},"id":"180ebdf4-254b-4664-b9ad-183dfbeec172","type":"BoxZoomTool"},{"attributes":{"callback":null},"id":"18f55766-8bb9-4fc2-b4f5-9f7fd293203e","type":"DataRange1d"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":20},"x":{"field":"x"},"y":{"field":"y"}},"id":"60f71218-c35d-4455-886c-d14d4ae5281f","type":"Circle"},{"attributes":{},"id":"97406f89-7ff6-40bd-9b18-1c9170cf8361","type":"BasicTicker"},{"attributes":{"dimension":1,"plot":{"id":"14dbd1d9-9ce6-4015-be6a-5c09e4f37208","subtype":"Figure","type":"Plot"},"ticker":{"id":"970209c7-882c-4f52-8c9d-64756f30afac","type":"BasicTicker"}},"id":"09f2945a-4134-43d3-9fe1-566609d62f48","type":"Grid"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"ce640f8a-963c-4c94-886f-a2eb7eb23cc3","type":"BoxAnnotation"},{"attributes":{},"id":"f53ad2c7-aed9-43f9-b732-5b2aa27e52a7","type":"PanTool"},{"attributes":{},"id":"970209c7-882c-4f52-8c9d-64756f30afac","type":"BasicTicker"},{"attributes":{"source":{"id":"44edcec5-ab99-40c4-a0bd-602dbc6df83a","type":"ColumnDataSource"}},"id":"688c9cbe-e27b-4c19-bb8a-01a93a32b0c0","type":"CDSView"},{"attributes":{},"id":"eeb4abc3-1768-4764-917b-e86e718748c7","type":"HelpTool"},{"attributes":{},"id":"254d2985-7573-4730-9cdf-b498515aa7bf","type":"LinearScale"},{"attributes":{"formatter":{"id":"15118476-67bb-4b2b-9e0d-6e33dd506379","type":"BasicTickFormatter"},"plot":{"id":"14dbd1d9-9ce6-4015-be6a-5c09e4f37208","subtype":"Figure","type":"Plot"},"ticker":{"id":"97406f89-7ff6-40bd-9b18-1c9170cf8361","type":"BasicTicker"}},"id":"63c4296e-e360-4fc3-9e4f-d24a07dc2834","type":"LinearAxis"},{"attributes":{},"id":"15118476-67bb-4b2b-9e0d-6e33dd506379","type":"BasicTickFormatter"}],"root_ids":["14dbd1d9-9ce6-4015-be6a-5c09e4f37208"]},"title":"Bokeh Application","version":"0.12.10"}};
          var render_items = [{"docid":"2f812de8-0d2c-49f5-be66-97b9f1c487a0","elementid":"ad783c20-4dea-4eef-9aad-4ee017d25800","modelid":"14dbd1d9-9ce6-4015-be6a-5c09e4f37208"}];
      
          root.Bokeh.embed.embed_items(docs_json, render_items);
        }
      
        if (root.Bokeh !== undefined) {
          embed_document(root);
        } else {
          var attempts = 0;
          var timer = setInterval(function(root) {
            if (root.Bokeh !== undefined) {
              embed_document(root);
              clearInterval(timer);
            }
            attempts++;
            if (attempts > 100) {
              console.log("Bokeh: ERROR: Unable to embed document because BokehJS library is missing")
              clearInterval(timer);
            }
          }, 10, root)
        }
      })(window);
    });
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();

</script>
---------------------------------------------

<div class="bk-root">
    <div class="bk-plotdiv" id="ad783c20-4dea-4eef-9aad-4ee017d25800"></div>
</div>
```
那既然可以分别获取，那我们就可以指定模板，然后将这两段代码嵌入进去，如下：
```python
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

```
## Chapter Two-来绘制一个图
先了解下图中的各个元素

![Image](./ChapterTwo/2.PNG)

[请点击示例Demo2](./ChapterTwo/Demo2.html)
### 第一步，准备数据源
有两种数据源，ColumnDataSource和GeoJSONDataSource，分别用来存放一般图形数据和地图数据。先来看看ColumnDataSource，可以通过data参数接收一个dict对象，也可以通过pandas的DateFrame来构建。每个数据集都指定key的名字，通过DateFrame创建则key为其每列的列名，没有列名，则index为其列名（However, if the index name (or any subname of a MultiIndex) is None, then the CDS will have a column generically named index for the index）。
有了key就可以让多个图形和工具共用同一份数据。
```python
from bokeh.models import ColumnDataSource

data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

source = ColumnDataSource(data=data)
# 通过DataFrame直接创建
source = ColumnDataSource(df)
```

### 第二步，准备画板-Figure
figure函数或者Figure对象选用一个即可，获得Figure对象，之后的图形都是在该图形上叠加
```python
from bokeh.plotting import figure, Figure

p = figure(plot_width=400, plot_height=400)

# p = Figure(plot_width=400, plot_height=400)
```
### 第三步，画图-Glyphs
图形有很多种，点散点图（circle，square），折线图（Lines，multi_line）,矩形图（quad，rect），柱状图（vbar，hbar），多边形（patch，patches），椭圆（oval），ellipse（可以分别定义宽度的椭圆），图像（You can display images on Bokeh plots using the image(), image_rgba(), and image_url() glyph methods.），线段（segment），射线（ray），圆弧（arc，wedge，annular_wedge，annulus）
可以将几种图叠加在一张图上，方法大同小异，以下以circle来展现下一般步骤
两种形式，第一种是plot调用方法circle，可以指定source
```python
p.circle(x='x_values', y='y_values', source=source, size=20, color='navy',alpha=0.5)

```
第二种先定义circle对象，再使用plot调用add_glyph时指定source
```python
circle = Circle(x='x_values', y='y_values', fill_color='navy', size=20, fill_alpha=0.5)
p.add_glyph(source, circle)
```
两种方式，第一种比较简洁，第二种更具面向对象风格。第一种参数更加丰富，比如颜色可以传入line_color='red', fill_color='navy'，color='blue'。如果只指定color，则line_color和fill_color默认与color一样。如果单独指定line_color和fill_color，会覆盖color指定。第二种则没有color这个参数
### 第四步，展示
调用show函数就可以实现，jupyter需要先调用output_notebook
```python
from bokeh.plotting import show
show(plot)
```
当然也可以像第一章通过python的io操作或者output_file("Demo1.html")输出到文件。

### 第五步，增加布局
可以同时画多个图形，然后根据布局来布置图形,按照列排列column，按照行排列row，按照网格排列gridplot。如果中间需要有缺省位置，则用None代替，如gridplot([[p1, p2], [None, p3]])
```python
p2 = Figure(plot_width=400, plot_height=400, tools=[hover])
p2.circle(x='x_values', y='y_values', source=source, size=20,color='blue', alpha=0.5, legend="xValue")

labels2 = LabelSet(x='x_values', y='y_values', x_offset=0, y_offset=10, text='label_value', source=source)
p2.add_layout(labels2)

show(column(p, p2))

```

### 第六步，增加Label
通过LabelSet增加标签，source指定与之前一样，text为要显示的值
这里有个小问题，显示内容不能格式化，所以要显示百分比之类的值，就需要在source里面埋相应的数据，然后在这里取出来。
x_offset和y_offset分别来设置坐标位置偏移量
```python
from bokeh.models import LabelSet, Legend, ColumnDataSource

data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6],
        'label_value': ["%d%%" % (100*y) for y in [6, 7, 2, 3, 6]]}

source = ColumnDataSource(data=data)
labels = LabelSet(x='x_values', y='y_values', x_offset=0, y_offset=10, text='label_value', source=source)
p.add_layout(labels)
```
### 第七步，增加Legend
第一种方式是直接画图时指定legend="xValue"，自动关联图形并提供小图标，然后可以根据p.legend获得并设置其他属性（p.legend.location可以接受枚举如"top_right"、"top_left"等，也可以接受元组指定像素位置）
```pythom
p.circle(x='x_values', y='y_values', source=source, size=20, color='navy',alpha=0.5, legend="xValue")

p.legend.location = (0, 300)
p.legend.orientation = "horizontal"
```
第二种是直接定义legend对象，然后再加入，这样做的好处是可以不遮挡图形
```python
c = p.circle(x='x_values', y='y_values', source=source, size=20,color='blue', alpha=0.5, legend="xValue")

legend = Legend(items=[
    ("xValue"   , [c])
], location=(0, -30))

p.add_layout(legend, 'right')
```
### 第八步，增加Hover
hover在图形中属于tools的一种，增加hover也有两种方式
第一种是先在Figure中指定添加tools="hover"，然后通过p.select_one(HoverTool)函数找到要设置的hover，设置hover.tooltips里面取值。取值方式有两种，一种是使用$符号，用于获取整个图形的属性，比如鼠标x，y的位置等。另一种是@符号取值，值的来源是sources中data的key,取出来的值后面跟{}可以设置数据格式。
注意，该取值是在js里面获取变量值的方式，所以这只能取值，而不能在python里面做算数运算。
```python
p = Figure(plot_width=400, plot_height=400, tools="hover")

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
("x轴", "@x_values"),
("y值", "@y_values{0.2f}" )]
```
第二种方式是先定义hover对象，在加入到图形中
```python

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
```
### 第九步，增加Widgets
我们来看看js实现交互，我们生成的都是静态页面，页面生成后，数据都埋在了docs_json变量中，如果需要再改变图形，就要根据用户选则改变数据来展现。
需要注意的是，select这里的参数必须是str类型的。
js代码中，cb_obj.value就可以获取到用户选择的值，然后根据该值改变数据源，以达到改变图形的效果。
这种方式自己写回调函数，对于复杂的数据处理很不方便，并且数据一开始就埋在浏览器中，可能浪费浏览器大量内存。(It is critical to note that no python code is ever executed when a CustomJS callback is used.)
后面将会讲到使用jupyter实现交互，则可以在python中利用pandas处理数据。

```python
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
layout = column(select, p, p2)

show(layout)
```
### 第十步，增加坐标轴
```python
line = Line(x='x_values',y='y_values')
p.extra_y_ranges = {"second_y": Range1d(start=0, end=max(source.data["y_values"]), max_interval=1)}
p.add_glyph(source, line, y_range_name='second_y',name='人效')
second_y = LinearAxis(y_range_name='second_y')
p.add_layout(second_y, 'right')

# 增加坐标轴格式
p.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
p.yaxis[1].formatter = NumeralTickFormatter(format="0.2f%")
```
## Chapter Three-在Jupyter上作图
在Jupyter上使用Bokeh，除了可以更多人分享，还可以使用ipywidgets实现真正意义上的交互，可以在python代码中通过pandas过滤数据来更新页面，而不是一次性将数据写到html。
首先需要执行output_notebook指定图形输出到jupyter
```python
from bokeh.io import output_notebook
output_notebook()
```
安装ipywidgets
```shell
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension
```
在第二章我们已经得到图形了，美中不足的是交互需要自己写js代码完成，现在我们就把Widgets换成ipywidgets，这样我们就可以在python里面利用pandas来组织数据。
改造只要三步，第一，把之前画图的代码封装到函数里面。第二，定义ipywidgets。第三，绑定函数和相应的ipywidgets。
```python
# -*- coding: UTF-8 -*-
import pandas as pd
from bokeh.plotting import Figure, show
from bokeh.models import Circle, ColumnDataSource, LabelSet,\
    Legend, LegendItem, GlyphRenderer, HoverTool, CustomJS, Select, Line, LinearAxis, NumeralTickFormatter, Range1d
from bokeh.layouts import column
import ipywidgets as widgets
from ipywidgets import interact, Layout
from bokeh.io import push_notebook, output_notebook

value = [6, 7, 2, 3, 6]

def make_plot(multi):
    y_value = [multi*y for y in value]
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
            'y_values': y_value,
            'label_value': ["%d%%" % (100*y) for y in y_value]}

    source = ColumnDataSource(data=data)
    labels = LabelSet(x='x_values', y='y_values', x_offset=0, y_offset=10, text='label_value', source=source)
    p.add_layout(labels)

    p.circle(x='x_values', y='y_values', source=source, size=20,color='blue', alpha=0.5, legend="xValue")

    p2 = Figure(plot_width=400, plot_height=400, tools=[hover])
    p2.circle(x='x_values', y='y_values', source=source, size=20,color='blue', alpha=0.5, legend="xValue")

    labels2 = LabelSet(x='x_values', y='y_values', x_offset=0, y_offset=10, text='label_value', source=source)
    p2.add_layout(labels2)

    line = Line(x='x_values',y='y_values')
    p.extra_y_ranges = {"second_y": Range1d(start=0, end=max(source.data["y_values"]), max_interval=1)}
    p.add_glyph(source, line, y_range_name='second_y',name='人效')
    second_y = LinearAxis(y_range_name='second_y')
    p.add_layout(second_y, 'right')
    p.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
    p.yaxis[1].formatter = NumeralTickFormatter(format="0.2f%")

    layout = column(p, p2)

    show(layout)
    
# 设置输出到jupyter
output_notebook()
    
select_multi = widgets.Dropdown(
options=[1, 2, 3],
value=1,
description=u'乘数:',
disabled=False,
)
interact(make_plot, multi=select_multi, continuous_update=False)
```
## Chapter Four-使用bokeh serve
除了jupyter可以调用python代码，再就是bokeh server了，具体可以参考官网的例子。
运行时指定端口，然后就可以通过nginx来转发
bokeh serve myapp.py --port 5100
