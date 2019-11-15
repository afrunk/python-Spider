import requests
from bs4 import BeautifulSoup
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='data',
                     charset='utf8')
cursor = db.cursor()

headers={
    'Cookie':'JSESSIONID=0DCC8BBBD58C98C5917996090A70E2C5'
}
for i in range(10,2641):
    print("正在抓取第{}页的数据请继续等待..".format(i))
    url='http://172.29.100.1:8080/sms-web/report/list?bizSend.sms_type=1&bizSend.send_channel=5&bizSend.status_=%E5%8F%91%E9%80%81%E6%88%90%E5%8A%9F&startDate=2019-10-01&endDate=2019-10-31&pageNo={}&bizSend.shop_no=1005&activityName=&bizSend.phone='.format(i)
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
        iphone = tds[1].text #手机号码
        leixing = tds[2].text # 短信类型
        reqtime = tds[7].text # 发送时间
        print(iphone,leixing,reqtime)

        sql_2 = """
                                INSERT IGNORE INTO data1 (iphone,leixing,reqtime)VALUES('{}','{}','{}')
                                    """ \
            .format(
            pymysql.escape_string(iphone),
            pymysql.escape_string(leixing),
            pymysql.escape_string(reqtime),
        )
        # print(sql_2)
        cursor.execute(sql_2)  # 执行命令
        db.commit()  # 提交事务
