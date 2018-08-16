# coding:utf-8
import requests
from bs4 import BeautifulSoup
import time

n = 1
for p in range(1,5):
    list_url = 'http://opinion.people.com.cn/GB/8213/353915/353916/index{0}.html'.format(p)
    list_wbdata = requests.get(list_url).content
    list_soup = BeautifulSoup(list_wbdata,'lxml')
    list_link = list_soup.select("td.t11 > a")
    for l in list_link:
        page_href = l.get('href')
        page_title = l.get_text()
        print(page_title,page_href)
        page_url = 'http://opinion.people.com.cn'+ page_href
        page_wbdata = requests.get(page_url).content
        page_soup = BeautifulSoup(page_wbdata,'lxml')
        content = page_soup.select_one("div.box_con")
        with open('{0}.txt'.format(page_title),'a+', encoding='utf-8',newline='') as files:
            files.writelines(content.get_text())
            print("写入完成！",n)
        n += 1
        time.sleep(3)
