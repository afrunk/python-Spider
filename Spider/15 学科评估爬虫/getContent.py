"""
链接：http://www.cdgdc.edu.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp?yjxkdm=0812&xkdm=08

"""

import requests
from bs4 import BeautifulSoup
headers ={
    'Host': 'www.cdgdc.edu.cn',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Cookie': 'scrolls=100; JSESSIONID=C4DE594329CA70164226AE384500CD4C; sto-id-20480-web_80=CAAKBAKMJABP; sto-id-20480-xww_webrms=CAAKBAKMEJBP; UM_distinctid=16c9345a3d541f-00b76cbb71f716-7373e61-1fa400-16c9345a3d6699; CNZZDATA2328862=cnzz_eid%3D975432557-1565838353-null%26ntime%3D1570710318'


}
def getContent():
    con=requests.get('http://www.cdgdc.edu.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp?yjxkdm=0812&xkdm=08',headers=headers)
    # print(con.text)
    soup = BeautifulSoup(con.text,'lxml')
    # print(soup)
    div = soup.find('div',style='height:510px; overflow:scroll;')
    # print(div)
    tbodys = div.find_all('tr')[0:-1]
    # print(tbodys)
    with open('school.txt', 'a+', encoding='utf-8') as f:  # a+才可追加 不知为何
        for tr in tbodys:
            print(tr.text)
            f.write(tr.text+'\n')
    f.close()

if __name__=='__main__':
    getContent()