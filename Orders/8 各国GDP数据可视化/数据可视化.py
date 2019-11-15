#coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PlotUtils
import sys

def is_country(x, fields):
  for field in fields:
    if field in x.encode("utf-8"):
      return False
  return True

def main():
  # 读取数据
  gdp = pd.read_excel("API_NY.GDP.MKTP.CD_DS2_zh_excel_v2_103680.xls")

  # 筛选：去掉世界、一些地区性的数据
  fields = ["世界", "收入国家", "地区", "南亚", "组织成员", "人口","北美", "联盟", "IBRD", "IDA", "重债穷国"]
  gdp["is_country"] = gdp.apply(lambda x: is_country(x["Country Name"], fields), axis = 1)
  gdp = gdp[gdp["is_country"] == True]

  datas = []
  for year in range(1960, 2019):
    year = str(year)
    gdp.sort_values(year, inplace = True, ascending = False)
    print(year,"==========================================")
    print(gdp[0:15][["Country Name", year]])

    data = gdp[0:15] #排序，取前15名
    data.sort_values(year, inplace = True, ascending = True)
    data[year] = data[year] / 10 ** 11

    datas.append([year, data[year].tolist(), data["Country Name"].tolist()])

  # 绘制动态图
  plot = PlotUtils.Plot(datas)
  plot.showGif("gdp.gif")

if __name__ == '__main__':
  main()
