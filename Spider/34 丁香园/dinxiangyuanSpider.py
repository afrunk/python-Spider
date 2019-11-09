import requests
from bs4 import BeautifulSoup
url='http://www.dxy.cn/bbs/board/87?order=2&tpg=3'
headers={
    'Cookie':'route_bbs=d183b59af94599ac5496eae0a79bc70f; JUTE_SESSION_ID=81045d45-bd4a-4338-b59c-bb7b4c20bf1c; dxy_da_cookie-id=fd58703f-88e8-4bc8-bf18-c4438fd82344; JUTE_TOKEN=f9600241-27ed-476b-975b-22d6dd5063f8; DXY_USER_GROUP=92; __asc=4527ef8d16e4e27a4481a3ccb40; __auc=4527ef8d16e4e27a4481a3ccb40; Hm_lvt_8a6dad3652ee53a288a11ca184581908=1573269251; __utma=1.470313737.1573269251.1573269251.1573269251.1; __utmc=1; __utmz=1.1573269251.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lpvt_8a6dad3652ee53a288a11ca184581908=1573269454; __utmb=1.7.9.1573269770768; JUTE_SESSION=3f20a1f0884c15ec425f6fa1fbc6e18e79bb5890fb1125c6be97c1dc40ecb34bea66f723a53cec82'
}

con = requests.get(url,headers=headers).text
# print(con)
soup = BeautifulSoup(con,'lxml')
div = soup.find('div',id='col-2')
table = div.find('table',class_='post-table')
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    a= tds[1].find('a')
    title = a.text # 文章标题
    urlPage = a.get('href') #文章链接
    print(title,urlPage)

    print(tds[2])
    nameAuthor = tds[2].find('a').text
    dateA = tds[2].find('em').text.replace('进展 javascript:;','')
    print(nameAuthor,dateA)
