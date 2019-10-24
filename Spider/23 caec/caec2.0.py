"""
http://www.caec.org.cn/index.php?m=content&c=index&a=lists&catid=39

公司名，人名字，电话和手机号，邮箱

2.0 匹配text中的目标内容
"""

import requests
from bs4 import BeautifulSoup
import re
# 获取HTML页面
def getHtml(url):
    con = requests.get(url).text
    # print(con)
    soup = BeautifulSoup(con,'lxml')
    return soup

#获取所有地区的链接
def getallpage(url):
    soup = getHtml(url)
    div = soup.find('div', class_='hyzq_box')
    # print(div)
    ass = div.find_all('a')
    # print(ass)
    urlAllPage = []
    for a in ass:
        url_1 = a.get('href')
        # print(url_1)
        urlAllPage.append(url_1)
        break  # 测试代码添加一个方便后续测试
    return urlAllPage

# 获取每个地区的公司链接
def getPageUrl(url):
    caeccontenturl = []
    urlAllPage = getallpage(url)
    for urlList in urlAllPage:
        html = getHtml(urlList)
        # print(html)
        div = html.find('div',id='zx')
        # print(div)
        lis = div.find_all('li')
        # print(lis)
        for li in lis:
            he=li.find('a').get('href')
            # print(he)
            caeccontenturl.append(he)
    return caeccontenturl

# 获取具体的信息
def getConet(url):
    contentList =[]
    soup = getHtml(url)
    # print(soup)
    div = soup.find('div',id='zxpage').text
    # print(div)
    pattern = r"单位名称:(.*)公司"
    compy = re.search(pattern, div).group(1)+'公司'
    print(compy)

    pattern = r'主要负责人：(.*)职务'
    name= re.search(pattern, div).group(1)
    if name:
        print(name)

    pattern =r'电话：(.*)传真'
    telephone = re.search(pattern, div)
    if telephone:
        print(telephone.group(1).rsplit())

    pattern = r'手机：(.*)邮箱:(.*).com'
    iphone = re.search(pattern, div)
    if iphone:
        print(iphone.group(1,2))


def reTest():
    s = '单位名称:北京华开建筑装饰工程有限公司'
    pattern = r"单位名称:(.*)公司"
    m = re.search(pattern, s)
    print(m.group())

if __name__=='__main__':
    url = 'http://www.caec.org.cn/index.php?m=content&c=index&a=lists&catid=39'
    caeccontenturl = getPageUrl(url)
    for a in caeccontenturl:
        print(a)
        listContent = getConet(a)

        # print(listContent)
        # break
    # reTest()
