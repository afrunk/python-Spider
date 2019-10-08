"""
监测微博固定用户是否发微博 如果有发微博的话久发邮件
未实现
下面实现的是抓取固定人的照片墙的所有照片存在本地

"""

# -*- coding: utf-8 -*-

import requests
import json
import time
import random
import pymysql.cursors
headers={
    'cookie':'ALF=1573049716; SUB=_2A25wnzglDeRhGeBG6VQU-S3KzTiIHXVQYFhtrDV6PUNbktANLVnYkW1NRghPOXtvPiMTOz7Npqu2jbwPTP3Gv-jE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWEyZCWwwVjLzRO6UuWa1TH5JpX5KzhUgL.FoqReoqf1KecSoB2dJLoI7qNC-4CUcRt; SUHB=0oU4sfsoBGtt95; SSOLoginState=1570457717; MLOGIN=1; _T_WM=41045288633; WEIBOCN_FROM=1110006030; XSRF-TOKEN=f02a8d; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1078036363234241%26featurecode%3D20000320%26fid%3D1078036363234241_-_photoall%26uicode%3D10000012',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# 莫名其妙的找到的可以下载图片的链接
# 主链接：https://m.weibo.cn/p/second?containerid=1078036363234241_-_photoall&page=1&count=24&title=%E5%9B%BE%E7%89%87%E5%A2%99&luicode=10000011&lfid=1078036363234241&featurecode=20000320

# 修改page 可以翻页 每页24张图片
url='https://m.weibo.cn/api/container/getSecond?containerid=1078036363234241_-_photoall&page=4&count=24&title=%E5%9B%BE%E7%89%87%E5%A2%99&luicode=10000011&lfid=1078036363234241&featurecode=20000320'
ren=requests.get(url,headers=headers)
ren.encoding = ren.apparent_encoding # 转换编码避免乱码
# print(ren.text)# 乱码
json_text = json.loads(ren.text)
# print(json_text)# 乱码没问题了
datas=json_text['data']['cards']
# print(datas)
path_1='J:\\资料库\\zy\\'
x=49
for data in datas:
    # print(data,'\n')
    # 一个data里有3张图片
    # data里仍然是嵌套
    datu1=data['pics'][0]['pic_big'] # 大图片
    print(datu1)

    text1=data['pics'][0]['mblog']['text'] # 文本
    print(text1)
    img = requests.get(datu1, headers=headers).content
    path=path_1+str(x)+'.jpg'
    with open(path, 'wb') as f:
        f.write(img)
        time.sleep(1)
        print("正在下载第{}张图片".format(x))
        x += 1

    datu2 = data['pics'][1]['pic_big']  # 大图片
    print(datu2)
    text2 = data['pics'][1]['mblog']['text']  # 文本
    print(text2)
    img = requests.get(datu2, headers=headers).content
    path = path_1 + str(x) + '.jpg'
    with open(path, 'wb') as f:
        f.write(img)
        time.sleep(1)
        print("正在下载第{}张图片".format(x))
        x += 1

    datu3 = data['pics'][2]['pic_big']  # 大图片
    print(datu3)
    text3 = data['pics'][2]['mblog']['text']  # 文本
    print(text3)
    img = requests.get(datu3, headers=headers).content
    path = path_1 + str(x) + '.jpg'
    with open(path, 'wb') as f:
        f.write(img)
        time.sleep(1)
        print("正在下载第{}张图片".format(x))
        x += 1

