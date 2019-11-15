"""
http://project.fdi.gov.cn/bbsinfo/s_1_0_96.html?style=1800000091-1-10000106&q=field39^%B6%D4%CD%E2%CD%B6%D7%CA&r=&t=ichk=0&starget=1
商务部投资项目信息库 对外投资项目
抓取首页的投资名称


"""

import requests
from bs4 import BeautifulSoup
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()

for s in range(1,97):
    url='http://project.fdi.gov.cn/bbsinfo/s_1_0_{}.html?style=1800000091-1-10000106&q=field39^%B6%D4%CD%E2%CD%B6%D7%CA&r=&t=ichk=0&starget=1'.format(s)
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Cookie':'ASP.NET_SessionId=2bbxqt55svxmp345comacr55; syncSessionID=2bbxqt55svxmp345comacr55'
    }
    con = requests.get(url,headers=headers).text
    # print(con)
    soup = BeautifulSoup(con,'html5lib') # 不能使用 lxml 否则会造成html页面内容丢失
    # print(soup)
    table = soup.find('table',class_='idModule21')
    # print(table)
    tbody =table.find('tbody')
    trs = tbody.find_all('tr')
    datas = []
    for i in range(len(trs)) :
        try:

            content = []
            nameA = trs[i].find('td',class_='zsyzlb-fmk1').text.replace('�C','-') # 项目名称
            tds = trs[i].find_all('td',class_='zsyzlb-fmk2')
            hangye = tds[0].text #行业
            diqu = tds[1].text  #地区
            # print(nameA,hangye,diqu)
            content.append(nameA)
            content.append(hangye)
            content.append(diqu)
            if i % 2==1:
                datas.append(content)
        except:
            pass
    print(len(datas))
    print(datas)
    for data in datas:
        sql_2 = """
                                INSERT IGNORE INTO duiwaitouziREA  (nameA,hangye,diqu )VALUES('{}','{}','{}' )
                                    """ \
            .format(
            pymysql.escape_string(data[0]),
            pymysql.escape_string(data[1]),
            pymysql.escape_string(data[2]),
        )
        # print(sql_2)
        cursor.execute(sql_2)  # 执行命令
        db.commit()  # 提交事务