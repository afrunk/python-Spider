"""
http://www.caec.org.cn/index.php?m=content&c=index&a=lists&catid=39

公司名，人名字，电话和手机号，邮箱
"""

import requests
from bs4 import BeautifulSoup
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
    div = soup.find('div',id='zxpage')
    # print(div)
    # 人名
    name = div.find('span',style='font-family: 宋体;').text
    # print(name)
    # 公司名 电话 手机号 邮箱
    spans = div.find_all('span',style='color: black; font-family: 宋体;')

    # print(spans)
    del spans[2]
    # for span in spans:
    #     print(span.text)
    company = spans[0].text # 公司名
    telephone = spans[1].text # 电话
    iphone = spans[2].text # 手机号
    email = spans[3].text #邮箱
    contentList = [name,company,telephone,iphone,email]
    # print(contentList)
    return contentList

if __name__=='__main__':
    url = 'http://www.caec.org.cn/index.php?m=content&c=index&a=lists&catid=39'
    caeccontenturl = getPageUrl(url)
    for a in caeccontenturl:
        print(a)
        try:
            listContent = getConet(a)
            print(listContent)
        except:
            pass