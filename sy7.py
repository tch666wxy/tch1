import datetime
import random
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Calendar

data1=pd.read_csv("stocks.csv",encoding="gbk")
print(data1)

print(data1.iloc[:,6])

c = (
    Calendar()
        .add("", data1.iloc[:,6], calendar_opts=opts.CalendarOpts(range_="2020"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Calendar"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000,
            min_=500,
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="100px",
        ),
    )
    .render("calendar_base.html")
)

