from app import test_app
from flask import render_template


@test_app.route('/')
def index():
    return render_template("index.html")


# 画echart图
from random import randrange
from pyecharts import options as opts
from pyecharts.charts import Bar


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c

@test_app.route("/test")
def test():
    return render_template("test.html")


@test_app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()