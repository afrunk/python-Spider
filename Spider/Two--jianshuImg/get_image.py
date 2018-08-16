import requests
from lxml import etree
import time
from bs4 import BeautifulSoup
import os
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

def get_url(url):
    res=requests.get(url,headers=headers)
    print(res)
    html = etree.HTML(res.text)
    infos = html.xpath('//ul[@class="note-list"]/li')#文章列表模块
    for info in infos:
        root = 'https://www.jianshu.com'
        url_path = root + info.xpath('div/a/@href')[0]
        print(url_path)#获取到每一个页面的详情页
        get_img(url_path)
    time.sleep(3)

def get_img(url_path):
    folder_path = './Photo'
    res=requests.get(url_path,headers=headers).text
    html=BeautifulSoup(res,'lxml')
    # print(html)
    title=html.find_all("h1","title")[0].text
    name=html.find("span","name").string
    infos=html.find_all("div","image-view")
    i=1
    if os.path.exists(folder_path)==False:
        os.makedirs(folder_path)
    for info in infos:
        try:
            img=info.find('img')
            src=img.get('data-original-src')
            print(src)
            data=requests.get('http:'+src,headers=headers)
            try:
                fp=open('photo\\'+title+name+'+'+str(i)+'.jpg','wb')
                fp.write(data.content)
                fp.close()
            except OSError:
                fp=open('photo\\'+name+'+'+str(i)+'.jpg','wb')
                fp.write(data.content)
                fp.close()
        except:
            pass
        i=i+1
    # print(title)
    # print(name)
    # print(infos)


if __name__ == '__main__':
    urls = ['https://www.jianshu.com/c/bd38bd199ec6?order_by=added_at&page={}'.format(str(i)) for i in range(161,201)]#201
    for url in urls:
        get_url(url)