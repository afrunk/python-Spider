"""
抓取地震的信息写入text
目标网站链接：http://www.ceic.ac.cn/speedsearch?time=1
json数据抓取链接：
    - http://www.ceic.ac.cn/ajax/speedsearch?num=1&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545914834  24小时内地震数据
    - http://www.ceic.ac.cn/ajax/speedsearch?num=2&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545944509  48小时内地震数据
    - http://www.ceic.ac.cn/ajax/speedsearch?num=3&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545961203  七天内地震数据
    - http://www.ceic.ac.cn/ajax/speedsearch?num=4&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545980766  最近30天内地震数据
    - http://www.ceic.ac.cn/ajax/speedsearch?num=6&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570546000818  最近一年内地震数据

需要字段:经纬度 位置 utc时间 震级
写入到txt,按照时间顺序来写 重复的不要

技术点：
    - json 分析

"""

import requests
import json

def GetContent():
    url='http://www.ceic.ac.cn/ajax/speedsearch?num=1&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545914834'
    con=requests.get(url)
    print(con.text)
    content=json.dumps(con.text)
    print(content)

if __name__=='__main__':
    GetContent()
