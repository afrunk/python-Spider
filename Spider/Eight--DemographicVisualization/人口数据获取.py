import requests
from pyecharts import Bar
from pyecharts import Line
haders={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
data={
    'startYear':2002,
    'endYear':2017
}
def get_json(url):
    year=[]#时间
    chenzheng_datavalue=[]#城镇人口
    chenzhengzb_datavalue=[]#城镇人口占比
    xiangcun_datavalue=[]#乡下人口
    zong_datavalue=[]#总人口
    json=requests.post(url,data=data).json()
    for i in range(0,16):
        print("年份"+json[i]['year']+"城镇人口占比"+json[i]['datavalue'])
        year.append(json[i]['year'])
        chenzhengzb_datavalue.append(json[i]['datavalue'])
    for i in range(48,64):
        # print(json[i])
        print("城镇人口"+json[i]['datavalue']+"万")
        chenzheng_datavalue.append(json[i]['datavalue'])
    for i in range(64,80):
        # print(json[i])
        print("乡下人口"+json[i]['datavalue']+"万")
        xiangcun_datavalue.append(json[i]['datavalue'])
    for i in range(80,96):
        print("年末人zong_datavalue口"+json[i]['datavalue'])
        zong_datavalue.append(json[i]['datavalue'])
    bar=Bar("总人口","江世交")
    bar.add('城镇人口',year,chenzheng_datavalue,mark_point=['average'])
    bar.add('乡下人口',year,xiangcun_datavalue,mark_line=['min','max'])
    bar.add('总人口',year,zong_datavalue,)
    line=Line("城镇人口占比")
    line.add("城镇人口占比",year,chenzhengzb_datavalue,is_smooth=True,mark_line=['max','average'])
    line.render('1.html')
    bar.render('2.html')

if __name__=='__main__':
    url='http://spcx.www.gov.cn/ZFW-AccessPlatform/gov/np/getGYValue.do'
    get_json(url)

"""
网络爬虫的实现步骤：给网站发送请求获取数据，将我们所需要的具体数据字段提取出来存储在列表中方便我们后续可视化调用
分析爬虫所需要的技术：js 计算机网络 python requests pyecharts
准备爬取的网站内容及简单介绍 ： 国务院数据页面，有几个数据可视化的页面，我通过抓取接口的方法来获取数据
爬取数据的准备工作：安装requests、pyecharts库，安装Chrome浏览器通过开发者工具来抓取我们的数据获取链接，更简单的请求我们的数据
编写python代码：一个函数解决所有的问题，将我们抓取数据的链接传入函数中即可获取到数据并进行可视化
爬取数据处理 ： 因为获取到的数据是json格式，所以我们需要提取我们需要的数据的字段，通过for和不断地向下深入来提取具体字段
使用数据分析函数进行简单的数据分析过程：提取到的数据十分地清晰，这里直接进行了数据替换传入，在可视化地时候进行了平均值，和最大最小值地设定，在图表中很清晰地可以看到这三个值
得出结论：城镇人口占比是逐年上升的，乡下人口的占比逐年下降，在2010年之前乡下人口比城镇人口多，之后实现转换。
"""


