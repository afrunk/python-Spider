import requests
from bs4 import BeautifulSoup
# import pymysql


headers={
    'Cookie':'JSESSIONID=0DCC8BBBD58C98C5917996090A70E2C5'
}

url = 'http://172.29.100.1:8080/sms-web/report/list?bizSend.shop_no=1005&bizSend.status_=%E5%8F%91%E9%80%81%E6%88%90%E5%8A%9F&startDate=2019-10-01&endDate=2019-10-31&bizSend.sms_type=1&bizSend.send_channel=5'
con = requests.get(url,headers=headers).text
# print(con)
soup = BeautifulSoup(con,'lxml')
table = soup.find('table',class_='sui-table table-zebra table-bordered')
# print(table)
tbody =table.find('tbody')
trs = tbody.find_all('tr')
for tr in trs:
    # print(tr.text)
    tds = tr.find_all('td')
    mendian = tds[0].text #门店
    iphone = tds[1].text #手机号码
    leixing = tds[2].text # 短信类型
    zhuangtai = tds[4].text #发送状态
    jifeitiaoshi = tds[5].text # 计费条数
    baosong = tds[6].text # 报送状态
    reqtime = tds[7].text # 发送时间
    print(mendian,iphone,leixing,zhuangtai,jifeitiaoshi,baosong,reqtime)
