import requests
from bs4 import BeautifulSoup
import os
import time
import random

def get_urls(url):
    res=requests.get(url)
    # print(res.text)
    s=1
    html=BeautifulSoup(res.text,'lxml')
    div=html.find_all('div','showindex__children')
    for i in range(len(div)):
        # print(div[i])
        url='http://qcr0122.x.yupoo.com'+div[i].find('a','album__main').get('href')
        title=div[i].find('a','album__main').get('title')
        # print(url)
        print(title)
        get_img(url,title)
        rtime = float( random.randint(1, 50) / 20)
        print("请让我休息%d秒钟" % rtime)
        print("接下来将要爬取" + "第%d款" % (i + 1))
        s+=1
        time.sleep(rtime)


def get_img(url,title):
    res=requests.get(url)
    html=BeautifulSoup(res.text,'lxml')
    divs=html.find('div','showalbum__parent showalbum__nor nor')
    # print(divs)
    div=divs.find_all('div','showalbum__children image__main')
    i=1
    for i in range(len(div)):
        img='http://photo.yupoo.com'+div[i].find('img').get('data-path')
        #发现的img连接是假的
        print(img)
        get_img_content(img,title,i)
        i+=1


def get_img_content(url,username,i):
    folder_path='./'+username
    if os.path.exists(folder_path)==False:
        os.makedirs(folder_path)
    res=requests.get(url)
    try:
        fp = open(folder_path+'\\' +str(i)+'.jpg', 'wb')
        fp.write(res.content)
        print("Sucessful"+username)
        fp.close()
    except:
        print("Failed"+username)
        pass

if __name__=='__main__':
    for i in range(11,19):#19
        url='http://qcr0122.x.yupoo.com/albums?tab=gallery&page='+str(i)
        get_urls(url)
        rtime = float(5 + random.randint(1, 50) / 20)
        print("请让我休息%d秒钟" % rtime)
        print("接下来将要爬取" + "首页第%d页" % (i+1))
        time.sleep(rtime)