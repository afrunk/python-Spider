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
    bar=Bar("总人口","动态可视化")
    bar.add('城镇人口',year,chenzheng_datavalue,mark_point=['average'])
    bar.add('乡下人口',year,xiangcun_datavalue,mark_line=['min','max'])
    bar.add('总人口',year,zong_datavalue,)
    line=Line("城镇人口占比")
    line.add("城镇人口占比",year,chenzhengzb_datavalue,is_smooth=True,mark_line=['max','average'])
    line.render()
    # bar.render()

if __name__=='__main__':
    url='http://spcx.www.gov.cn/ZFW-AccessPlatform/gov/np/getGYValue.do'
    get_json(url)