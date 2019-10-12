"""
date:2019-10-11
author:afrunk
KnowladgePoint:request Bs4
目标：获取荆楚网 http://www.cnhubei.com/?spm=zm1033-001.0.0.1.cjv8MN&tdsourcetag=s_pcqq_aiomsg
        和长江日报 http://cjrb.cjn.cn/search/adsearch.jsp
    从2015-7到现在得所有有关制造关键字的新闻

荆楚网：静态 总页数456 get()
长江日报：动态 210 post()

完整代码

"""
import requests
import re
from bs4 import BeautifulSoup

def getSoupHtml(url):
    con = requests.get(url)
    con.encoding = con.apparent_encoding # 避免乱码
    soup =BeautifulSoup(con.text.replace('<h2></h2>','').replace('<h4></h4>',''),'lxml')
    # print(soup)
    return soup

# 获取长江日报
def getChangjiangNews():
    PageUrlList = []
    for i in range(1,211): # 210 页
        data = {
            "page": '',
            "data_start": '2015-07-01',
            "data_end": '2019-10-11',
            "title": '',  # 极限就是61
            "context": '制造',
            'author':'',
            'orderMethod':'dateDesc'
            }
        data['page']=i
        url='http://cjrb.cjn.cn/search/adsearch.jsp'
        con = requests.post(url,data=data).text
        # print(con)
        soup = BeautifulSoup(con,'lxml')
        tbodys = soup.find('table',class_='bian1').find_all('tr')
        # print(tbodys)
        # print(len(tbodys))
        for j in range(0,len(tbodys)+1,2): # 因为列表相邻得两个是相同得 所以以2为间隔进行跳转
            try:
                a=tbodys[j].find(href=re.compile('content')) # re来匹配href链接 官方文档 find_all keyword 参数 可以查看
                indexUrl = a.get('href') # 获取链接
                print(indexUrl) #
                PageUrlList.append(indexUrl) # 存入列表中
            except:
                pass
    print(len(PageUrlList))
    for  i in range(len(PageUrlList)):
        print("正在抓取第{}篇文章".format(i))
        con = getSoupHtml(PageUrlList[i]) # 遍历列表获取具体地内容 标题正文
        try:
            content = con.find('div',class_='text_c')
            zhengwen = content.text.replace('/*	if(picResCount>0){','').replace('document.getElementById("picres").style.display="block";','').replace('document.write("<br />");','').replace('}*/','').strip().replace('\n','').rstrip()
            # print(zhengwen)
            with open('CJ.txt', 'a+', encoding='utf-8') as f:  # a+才可追加 不知为何
                f.write(zhengwen + '\n') # 标题一行
            f.close()
        except:
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

    # 遍历文章链接列表 获取正文和标题写入txt中
    for i in range(len(pageUrls)):
        print("正在抓取第{}篇文章".format(i))
        PageHTMl = getSoupHtml(pageUrls[i]) # 遍历链接来获取文章得HTML 然后筛选出来正文和标题存入txt中
        title = PageHTMl.find('h1').text  # 标题
        zhengwen = PageHTMl.find('div',class_='article_w').text.replace('.wzy_zw_img{ max-width:680px!important;} ','').replace('a.wzy_zw_imga{ height:130px; width:320px; position:absolute; left:0; top:0; display:block;}','').replace('.wzy_zw_img{ max-width:680px!important;margin-top:20px;} ','').replace('.wzy_zw_img_box{ width:680px; position:relative; overflow:hidden; margin-top:20px;}','').strip().replace('\n','') # 正文 替换和去掉换行以及空格
        # print(title,zhengwen)
        with open('JC.txt', 'a+', encoding='utf-8') as f:  # a+才可追加 不知为何
            f.write(title + '\n') # 标题一行
            f.write(zhengwen + '\n')#正文一行
        f.close()


if __name__=='__main__':
    getChangjiangNews()