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
    as_2s = soup.find_all('a',class_='c-media--v1_0_0 c-padding-top-l c-padding-bottom-l zp-list-item zp-list-item-show c-flex c-flex-center-y')
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
        # try:
        if '月' in time:
            # print("当前正在更新")
            print(name+' ' +title + ' ' + time)
        else:
            # print("几年前的")
            time=str(time).replace('年前','')
            time = 2019-int(time)
            print(name+' '+title + ' ' + str(time))
            # except:
            #     pass
    except:
        print("当前作品无法抓取到时间")

# 将作家的名字写入
def readexcleTosql():
    pass

if __name__=='__main__':
    name = '骁骑校'
    url = 'https://so.m.sm.cn/s?q={}&uc_param_str=dnntnwvepffrgibijbprsv&from=ucdh'.format(name)
    booklist = getUrls(url)
    for i in range(0,len(booklist)):
        # print(i)
        getTimeAndTitle(name,booklist[i])

