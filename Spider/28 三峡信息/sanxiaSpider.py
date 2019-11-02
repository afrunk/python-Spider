"""
post 获取三峡的数据 20000101-20181231 的数据


"""

import requests
import json
url ='https://www.ctg.com.cn/eportal/ui?moduleId=50c13b5c83554779aad47d71c1d1d8d8&&struts.portlet.mode=view&struts.portlet.action=/portlet/waterFront!getDatas.action'
headers ={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
   'Connection': 'keep-alive',
    'Content-Length': '15',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=848779509D7FB154F856E1B322920480',
    'Host': 'www.ctg.com.cn',
    'Origin': 'https://www.ctg.com.cn',
    'Referer': 'https://www.ctg.com.cn/sxjt/sqqk/index.html',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
data={
    'time':'2018-11-12'
}
con = requests.post(url,headers=headers,data=data).json()
print(con['ckList'])