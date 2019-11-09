"""
目标网站 https://splcgk.court.gov.cn/gzfwww/fgml
POST https://splcgk.court.gov.cn/gzfwww///fgmlList

fyid: 8D14994CAD8E9CD3F2520D2AE2BCB468
fymc: 北京市大兴区人民法院


fyid: A030C5E9F5934E5D494C9246CB80227A
fymc: 北京市第一中级人民法院

"""
import requests
import json
from bs4 import BeautifulSoup

def getCid(sf):
    cnamecidList =[]
    url='https://splcgk.court.gov.cn/gzfwww//getFyLbBySf'
    data={
        'sf':'北京'
    }
    data['sf']=sf
    headers={
        'Cookie':'JSESSIONID=25205F111D1EB4D935CDA2BEDDC44D90; route=c1ca62d122a6a1bdae853ec4786284f9'
    }
    con = requests.post(url,headers=headers,data=data).text
    # print(con)
    con = json.loads(con)
    for i in con:
        content =[]
        cname = i['cname']
        cid=i['cid']
        print(cname,cid)
        content.append(cname)
        content.append(cid)
        cnamecidList.append(content)
    return cnamecidList

def getContent():
    cnamecidList = getCid('北京')[1:]
    url='https://splcgk.court.gov.cn/gzfwww///fgmlList'
    headers={
        'Cookie':'JSESSIONID=25205F111D1EB4D935CDA2BEDDC44D90; route=c1ca62d122a6a1bdae853ec4786284f9; _gscu_125736681=73093045r201lu14; _gscbrs_125736681=1; _gscs_125736681=73093045eyn44z14|pv:1; Hm_lvt_9e03c161142422698f5b0d82bf699727=1573093046; Hm_lpvt_9e03c161142422698f5b0d82bf699727=1573093046'
    }
    for i in cnamecidList:
        data={
            'fyid':'',
            'fymc':'',
        }
        data['fyid']=i[1]
        data['fymc']=i[0]
        con = requests.post(url,headers=headers,data=data)
        # print(con.text)
        soup = BeautifulSoup(con.text,'lxml')
        tbody = soup.find('table',class_='fd-table-03')
        # print(tbody)
        trs = tbody.find_all('tr')[1:]
        for tr in trs:
            contentPeople =[]
            tds = tr.find_all('td')
            for j in tds:
                td=j.text
                contentPeople.append(td)
            print(contentPeople)


if __name__ == '__main__':
    getContent()