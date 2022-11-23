import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel("非洲通讯产品销售数据.xlsx")
data["year"]=data["日期"].dt.year
data['quarter']=data['日期'].dt.quarter
diqu=data.pivot_table(['利润','销售额'],index=['year','quarter'],columns='地区',aggfunc=['sum','mean','median'],margins=True)
data1=data.groupby(["服务分类", "国家"])["销售额"].sum()
print(diqu)
cj.to_excel(outpath,index=True,header=True)