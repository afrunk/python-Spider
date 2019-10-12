"""
date:2019-10-11
author:afrunk
KnowladgePoint:request Bs4
目标：获取荆楚网 http://www.cnhubei.com/?spm=zm1033-001.0.0.1.cjv8MN&tdsourcetag=s_pcqq_aiomsg
        和长江日报 http://cjrb.cjn.cn/search/adsearch.jsp
    从2015-7到现在得所有有关制造关键字的新闻

荆楚网：静态 总页数456
长江日报：动态 210


缺少长江日报部分
"""
import requests
from bs4 import BeautifulSoup

def getSoupHtml(url):
    con = requests.get(url)
    con.encoding = con.apparent_encoding # 避免乱码
    soup =BeautifulSoup(con.text,'lxml')
    # print(soup)
    return soup

# 获取长江日报
def getChangjiangNews():
    pass

# 荆楚网
def getJCNews():

    pageUrls=[] # 文章具体链接列表
    for i in range(2,457): # 457 循环获取得到搜索关键字得列表里所有可以查看到得文章得具体链接存入列表中
        url='http://www.cnhubei.com/s?alias=&wd=%E5%88%B6%E9%80%A0&page={}'.format(i)
        print("当前访问得列表页数为：",url)
        content = getSoupHtml(url) # 获取HTML
        div=content.find('div',id='mainContent') # 匹配div id为 mainContent
        # print(div)
        h2s = div.find_all('h2') # 匹配所有含有文章链接得 h2 标签得到一个列表
        # print(h2s)
        for h2 in h2s: # for循环遍历每一个标签 得到文章得链接添加到列表中
            print(h2.text) # 输出标题
            urlIndex = h2.find('a').get('href') # 获取链接
            print(urlIndex)
            pageUrls.append(urlIndex)
    print(len(pageUrls))
    # 遍历文章链接列表 获取正文和标题写入txt中
    for i in range(633,len(pageUrls)):
        print("正在抓取第{}篇文章".format(i))
        PageHTMl = getSoupHtml(pageUrls[i]) # 遍历链接来获取文章得HTML 然后筛选出来正文和标题存入txt中
        try:
            title = PageHTMl.find('h1').text  # 标题
            zhengwen = PageHTMl.find('div',class_='article_w').text.replace('.wzy_zw_img{ max-width:680px!important;} ','').replace('a.wzy_zw_imga{ height:130px; width:320px; position:absolute; left:0; top:0; display:block;}','').replace('.wzy_zw_img{ max-width:680px!important;margin-top:20px;} ','').replace('.wzy_zw_img_box{ width:680px; position:relative; overflow:hidden; margin-top:20px;}','').strip().replace('\n','') # 正文 替换和去掉换行以及空格
            # print(title,zhengwen)
            with open('JC.txt', 'a+', encoding='utf-8') as f:  # a+才可追加 不知为何
                f.write(title + '\n') # 标题一行
                f.write(zhengwen + '\n')#正文一行
            f.close()
        except:
            pass

if __name__=='__main__':
    getJCNews()