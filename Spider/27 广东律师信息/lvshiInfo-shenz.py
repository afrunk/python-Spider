"""
- post 请求获取链接即可 修改data的值即可获取到所有数据
该数据的显示意义挺大的 回头拿来整理下坐下可视化看一下整个广东得律所的可视化效果分析

以后可以用数据库写入数据就不要用csv 一个愿意是慢 一个是容易丢失

"""

import pymysql
import requests
import json
import csv
import time
import random
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()

def getid(num):
    idList =[]
    diqus =[]
    # url='https://cucc.tazzfdc.com/reisPub/pub/preSaleBuildingStatist' # 预售
    url ='https://gd.12348.gov.cn/portal/legalserviceresources/legalserviceresourcesAction!searchOrgPager.action' # 现售
    headers ={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '119',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'HttpOnly; UM_distinctid=16e1ba3dcb0241-097d7afb21347b-b363e65-1fa400-16e1ba3dcb125d; USER_KEY=1f375172-dd8b-46b8-8372-7c27ea972f45; CNZZDATA1273207381=976185462-1572420108-%7C1572521995',
        'Host': 'gd.12348.gov.cn',
        'Origin': 'https://gd.12348.gov.cn',
        'Referer': 'https://gd.12348.gov.cn/jsp/web/legalserviceres/legalserviceorg.jsp?fwOrgType=100&flag=org',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    # 需要修改两个字段
    data = {
        'pagerOrgParam.tbOrgLsglJgjbxxVo.fwxzqh': '440300000000',
        'pagerOrgParam.tbOrgLsglJgjbxxVo.obiOrgtype':'',
        'pagerOrgParam.tbOrgLsglJgjbxxVo.obiOrgname':'',
        'pagerOrgParam.tbOrgLsglJgjbxxVo.tbOrgLsglLsjgzyxxVo.creditcode':'',
        'pagerOrgParam.tbOrgLsglJgjbxxVo.tbOrgLsglLsjgzyxxVo.opiLeadername':'',
        'obiProvince': '440000000000',
        'obiCity': '440300000000',
        'obiDistrict':'',
        'pagerOrgParam.fwOrgType': '100',
        'pagerOrgParam.currentPage': '1',
        'pagerOrgParam.pageSize': '10',
        'pagerOrgParam.sign': '1',
        'dqdp_csrf_token':''
    }
    data['pagerOrgParam.currentPage'] = num
    print(data)
    # con = requests.post(url=url,data=data)
    con = requests.post(url=url,data=data,headers=headers).text
    con = json.loads(con)
    allListInfoobiIds=con['data']['data']['data']['searchOrgPager']
    for obiid in allListInfoobiIds:
        obiidId =obiid['obiId']
        diqu = obiid['fwxzqhDesc']
        idList.append(obiidId)
        diqus.append(diqu)
    # print(idList)
    # print(diqus)
    return idList,diqus

def getLvsuoInfo(oid,diqu1,page1):
    url = 'https://gd.12348.gov.cn/portal/legalserviceresources/legalserviceresourcesAction!loadOrgDetail.action'  # 现售

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '24',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'HttpOnly; UM_distinctid=16e1ba3dcb0241-097d7afb21347b-b363e65-1fa400-16e1ba3dcb125d; CNZZDATA1273207381=976185462-1572420108-%7C1572521995; USER_KEY=f345e516-38f3-4a2c-bca4-e344cebf35d7',
        'Host': 'gd.12348.gov.cn',
        'Origin': 'https://gd.12348.gov.cn',
        'Referer': 'https://gd.12348.gov.cn/portal/legalserviceresources/legalserviceresourcesAction!searchOrgDetail.action?fwOrgType=100&orgid=1899',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'fwOrgType': '100',
        'orgid': '1899'
    }
    data['orgid'] = oid
    # print(data)
    # con = requests.post(url=url,data=data)
    con = requests.post(url=url, data=data, headers=headers).text
    con = json.loads(con)
    # print(con)
    data = con['data']['data']['data']['tbOrgLsglJgjbxxVo']
    #获取数据 写入数据库
    obiOrgname=data['obiOrgname'] #律所名
    # obiManagerlevelDesc = data['obiManagerlevelDesc']  # 主管机关
    opiOorganformDesc = data['tbOrgLsglLsjgzyxxVoList'][0]['opiOorganformDesc'] #组织形式['0']['opiOorganformDesc']
    # print(opiOorganformDesc)
    # obiOrgtypeDesc = data['obiOrgtypeDesc'] # 机构类型
    obiOfficeused = data['obiOfficeused'] #设立资产
    obiFounddate =data['obiFounddate'] #成立时间
    opiLeadername = data['tbOrgLsglLsjgzyxxVoList'][0]['opiLeadername'] #负责人
    # opiCheckyear = data['tbOrgLsglLsjgzyxxVoList']['opiCheckyear']  # 最新考核年份
    creditcode ="'"+str(data['tbOrgLsglLsjgzyxxVoList'][0]['creditcode'])# 统一社会信用代码
    # obiEmail = data['obiEmail'] # 邮箱
    # obiPostal = data['obiPostal'] # 邮政编码
    obiAddress =data['obiAddress'] # 地址
    proplenum = str(len(data['tbOrgLsglLsryjbxxVo'])) # 人数

    data = obiOrgname+','+opiOorganformDesc+','+obiOfficeused+','+obiFounddate+','+creditcode+','+obiAddress+','+proplenum+','+diqu1
    print(obiOrgname,opiOorganformDesc,obiOfficeused,obiFounddate,creditcode,obiAddress,proplenum,diqu1)
    sql_2 = """
        INSERT IGNORE INTO shenzheng (obiOrgname,opiOorganformDesc,obiOfficeused,obiFounddate,creditcode,obiAddress,proplenum,diqu,page)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}'  )
                        """ \
        .format(
        pymysql.escape_string(obiOrgname),
        pymysql.escape_string(opiOorganformDesc),
        pymysql.escape_string(obiOfficeused),
        pymysql.escape_string(obiFounddate),
        pymysql.escape_string(creditcode),
        pymysql.escape_string(obiAddress),
        pymysql.escape_string(proplenum),
        pymysql.escape_string(diqu1),
        page1,
    )
    # print(sql_2)
    cursor.execute(sql_2)  # 执行命令
    db.commit()  # 提交事务


if __name__=='__main__':
    for j in range(1, 95):
        idList,diqus = getid(j)
        print(len(idList),len(diqus))
        time.sleep(random.randint(1,5))
        print("名字  组织形式  设立资产（单位万） 成立时间  统一社会信用码 地址 人数 地区 ")
        for i in range(len(idList)):
            # time.sleep(random.randint(1,2))
            getLvsuoInfo(idList[i],diqus[i],j)

        # getLvsuoInfo(1,1)