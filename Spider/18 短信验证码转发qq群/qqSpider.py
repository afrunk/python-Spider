"""

抓取平台的短信通知 转发到qq群
- 技术点
    读写csv文件监测数据是否被抓到过：这个方法等到数据量越来越大得时候就会导致不及时 所以改为抓取短信后得时间是否为5分钟内 如果是则发送到qq群

"""

import requests
from bs4 import BeautifulSoup
import csv


headers ={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=3mebt02pn1q53h7sraujlll3a6',
        'Host': '47.96.101.22:9999',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',

    }

# 抓取数据存入本地csv
def getContent():
    infos = [] # 存储最新抓取到得数据

    url = 'http://47.96.101.22:9999/index.php?g=cust&m=smscust&a=receive'
    con = requests.get(url,headers=headers).text
    # print(con)
    soup = BeautifulSoup(con,'lxml')
    # 定位到电话和验证码地区
    table = soup.find('table',class_='table table-hover table-bordered table-list')
    # print(table)
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    for tr in trs:
        content = tr.text.rsplit(' ')[1:3] # 将电话和验证码匹配出来
        content[1]=content[1].replace('\t','')[:18] # 处理获取到得信息只获取我们所需要得信息
        # print(content)
        infos.append(content) # 将处理好得数据结构存入列表


    print(infos)
    # 第一次跑必须有 跑完之后注释掉 原始数据以便对照是否新数据进入
    with open("data.csv", 'a+', newline='',encoding='utf-8') as f:  # 写入到本地csv中 a+会自动创建文件 newline解决中间有空行的问题
        for data in infos:
            write = csv.writer(f)
            write.writerow(data)


if __name__=='__main__':
    getContent()


