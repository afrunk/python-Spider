import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
}


# 获取站点名和站点链接
def get_html(url):
    zhandianmings = [] # 站点列表
    zhandianhrefs = [] # 站点链接列表
    con = requests.get(url,headers=headers).text
    soup = BeautifulSoup(con,'lxml')
    div =soup.find('div',class_='list clearfix')
    hrefs = div.find_all('a')
    for href in hrefs:
        zhandianming =href.text
        zhandianhref = 'https://shanghai.8684.cn/'+href.get('href')
        # print(zhandianming,zhandianhref)
        zhandianmings.append(zhandianming)
        zhandianhrefs.append(zhandianhref)
    return zhandianmings, zhandianhrefs
    # print(con)



# 获取上下行站点名
def getSX(zhandianmings,zhandianhrefs):
    for zhandianming,zhandianhref in zip(zhandianmings,zhandianhrefs):
        try:
            shangxinglist = []  # 上行站点总列表
            xiaxinglist = []  # 下行站点总列表
            # print(zhandianhref)
            con = requests.get(zhandianhref).text
            soup = BeautifulSoup(con, 'lxml')
            # 上行
            div = soup.find('div',class_='bus-lzlist mb15')
            ol = div.find('ol')
            lis = ol.find_all('li')
            # print("上行路线站点\n")
            for li in lis :
                data = li.text
                # print(data)
                shangxinglist.append(data)

            # 下行
            div_1 = soup.find_all('div',class_='bus-lzlist mb15')[1]
            # print(div_1)
            ol_1 = div_1.find('ol')
            lis_1 = ol_1.find_all('li')
            # print("下行路线站点\n")
            for li_1 in lis_1 :
                data = li_1.text
                # print(data)
                xiaxinglist.append(data)
            print(zhandianming)
            print("上行站点")
            print(shangxinglist)
            print("下行站点")
            print(xiaxinglist)
        except:
            pass
    # return shangxinglist,xiaxinglist

if __name__ == '__main__':
    url='https://shanghai.8684.cn/line2'
    zhandianmings,zhandianhrefs = get_html(url) # 返回站点名和站点链接列表
    # print(zhandianmings,zhandianhrefs)
    getSX(zhandianmings,zhandianhrefs) # 获取上下行
