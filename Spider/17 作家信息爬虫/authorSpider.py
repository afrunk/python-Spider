"""
author = afrunk
time = 2019-10-24
技术点：
    requests
    bs4
    pymysql
    xlrd

目的：分析网络作家创造力时变规律
过程：通过对网络作家完成作片的年龄来分析
需要数据：
    网络作家 姓名  出生年月 作品名称 完结时间 是否还在创作（未完结作片）

目标网站：
    起点中文网、创世中文网、小说阅读网、潇湘书院、红袖添香、云起书院、起点女生网、言情小说吧、掌阅文化、纵横中文网、晋江文学城、17K小说网、阿里文学、咪咕数媒、阿里文学、网易文学、逐浪网、红薯网、中版大佳网、凤凰文学、塔读文学、趣阅科技、铁血网、火星小说、不可能的世界小说网、看书网、飞库网、点众科技、磨铁中文网、创别书城、爱读文学网、作客文学网、长江中文网、天涯文学、盛世阅读网、云阅文学、半壁江中文网、书海小说网、蔷薇书院、汉王书城、中国作家网、中国诗歌网、作家在线

"""
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()
import xlrd
import requests
from bs4 import BeautifulSoup

def getSoup(url):

    con = requests.get(url).text
    # print(con)
    soup = BeautifulSoup(con,'lxml')
    return soup


def getUrls(url):
    soup = getSoup(url)

    as_1s = soup.find_all('a',class_='c-media--v1_0_0 c-padding-top-l c-padding-bottom-l zp-list-item c-flex c-flex-center-y')
    # print(as_1s)
    as_2s = soup.find_all('a',class_='c-media--v1_0_0 c-padding-top-l c-padding-bottom-l zp-list-item zp-list-item-show c-flex c-flex-center-y')
    # print(as_2s)
    if len(as_1s) == 0:
        as_1s = soup.find_all('a',class_='dl-container c-cell--v1_0_0 c-block c-text-start c-padding-top-l c-padding-bottom-l')
        as_2s = soup.find_all('a',class_='dl-container c-cell--v1_0_0 c-block c-text-start c-padding-top-l c-padding-bottom-l')

    bookList =[] # 存放当前作家得作品链接
    for i in as_1s:
        BookUrl = i.get('href')
        bookList.append(BookUrl)
        # print(BookUrl)
        # print('\n')
    for j in as_2s:
        BookUrl = j.get('href')
        bookList.append(BookUrl)
        # print(BookUrl)
        # print('\n')
    # print(bookList)
    return bookList

# 获取书的更新时间和名字
def getTimeAndTitle(name,bookurl):
    soup = getSoup(bookurl)
    # print(soup)
    try:
        title = soup.find('div',class_='c-header-title c-line-clamp-1 icon-right c-margin-right-l').text
        time = soup.find('div',class_='c-chapter-extra c-text-s c-margin-left-l').text
        try:
            if '月' in time:
                # print("当前正在更新")
                print(name+' ' +title + ' ' + time)
            else:
                # print("几年前的")
                time=str(time).replace('年前','')
                time = 2019-int(time)
                print(name+' '+title + ' ' + str(time))
        except:
            pass
    except:
        print("当前作品无法抓取到时间")

# 操作表格 获取作家名
def readexcleTosql():

    # 打开文件, 返回一个操作对象
    excel_content = xlrd.open_workbook("data.xlsx")
    '''检查某个工作表是否导入完毕, 参数为工作表的下表'''
    ret_ok = excel_content.sheet_loaded(0)  # True
    # 查询当前表格下有几个sheet
    # names = excel_content.sheet_names()
    # print(names)
    ret1 = excel_content.sheets()[0] # 获取第一个表
    column_data = ret1.col_values(5) # 第6列
    column_datas = column_data[1:] # 存放所有网络作家的网名
    # print(column_datas)
    return column_datas


if __name__=='__main__':
    column_datas = readexcleTosql()
    for name in column_datas:
        print(name)
    # name = '跳舞'
        url = 'https://so.m.sm.cn/s?q={}&uc_param_str=dnntnwvepffrgibijbprsv&from=ucdh'.format(name)
        # print(url)
        booklist = getUrls(url)
        for i in range(0,len(booklist)):
            # print(i)
            getTimeAndTitle(name,booklist[i])

"""
安妮宝贝
紫薇朱槿
千里烟
笑看云起
原名石悦
晴川
紫百合
辰东
携爱再漂流
小鬼儿儿儿
聂昱冰
阿里歌歌
天下尘埃
菜刀姓李
苏小懒
晓月
良木水中游
欲不死
一枚糖果
求无欲
金子
一草
顾七兮
木青
金满
飞天
兰心
琴律
百世经纶
古筝
满城烟火
宝剑锋
意者
冥灵
千幻冰云
阿彩、承九
冷海隐士
妖夜
苏凌素心
猪王
冷得像风
玖伍贰柒
紫月君
明日复明日
白焰
三盅
锐利
常青
善水
蒋离子
青子
希墨
仙人掌的花
罗晓
心在流浪
刘十八
戏剧王者
极品妖孽
流浪的军刀
有熊氏
太山
荆洚晓
洛城东
sky威天下
纳兰若夕
肖锚
骠骑
zenk
雨魔
夜摩
二目
冰可人
李写意
凌眉
魏岳
寒露
天子
雨阳
陨落星辰
乱世狂刀
清扬婉兮
烟毒
喝口小酒
九戈龙
特立独行的猫
紫箫
烈焰滔滔
漠兮
Q点调皮
三棱军刺
七英俊
谷雨
冰蓝纱
大肚鱼
常长笑
"""