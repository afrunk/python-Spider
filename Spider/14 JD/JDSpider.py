# -*- coding:utf-8 -*-

"""
CloneUrl: https://github.com/wanglegedong/jingdongscrapy/blob/master/%E4%BA%AC%E4%B8%9C%E7%88%AC%E8%99%AB2.0.py
抓取某个关键词下的所有商品信息 可以使用

- 技术点
    - 类

"""
# 搜索京东商品  使用动态数据抓取
import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import random
# from pymongo import MongoClient
import datetime
class JD():
    def __init__(self):
        # client = MongoClient()  # 与MongDB建立连接（这是默认连接本地MongDB数据库）
        # db = client['jingdong']  # 选择或创建一个数据库
        # self.jingdong_collection = db['ximiannai']  # 在meizixiezhenji这个数据库中，选择一个集合
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        self.iplist = [
            "123.163.96.88",
            "163.204.246.48",
            "183.129.244.16",
            "120.79.203.1",
            "114.113.222.131",
            "180.118.135.18",
            "120.25.203.182",
            "163.204.245.203",
            "59.37.33.62",
            "43.248.123.237",
            "175.44.156.198",
            "120.236.178.117",
            "183.158.202.222",
            "221.1.200.242",
            "61.176.223.7"
        ]  # 这是IP池

    def req(self, url):
        # 解析京东搜索首页地址
        with open('jingdong.csv', 'a', newline='',encoding='gbk') as csvfile:  # 保存到CSV列表里
            writer = csv.writer(csvfile)
            writer.writerow(['商品ID', '商品', '商品标题', '链接地址', '价格'])
        soup1 = self.requests_utf(url)
        allcount = soup1.find('span', id='J_resCount').get_text()  # 找到商品总数
        print('共有', allcount, '件商品')
        print('**************************************************************************')
        # 查询搜索的商品总页数
        page = int(soup1.find('span', class_='fp-text').i.get_text())
        print(page)

        for i in range(1, page * 2, 2):
            url_star = url[:-2] + str(i)
            print(url_star)
            # 根据商品页数解析搜索地址
            soup = self.requests_utf(url_star)
            # 定位商品信息
            li_all = soup.find_all('li', class_='gl-item')
            for i in li_all:
                try:
                    # 商品标题
                    title = i.a['title']

                    # 商品实际地址
                    href = i.a['href']
                    if href[:4] == 'http':
                        pass
                    else:
                        href = 'https:' + href
                    print(href)
                    print('价格是：',i.i.get_text())
                    try:
                        price = float(i.i.get_text())
                        print(price)
                    except:
                        price=0
                    # 解析商品实际地址
                    soup_href = self.requests_gbk(href)
                    real_href = soup_href.find('link', rel="canonical")['href']
                    real_href = 'https:' + real_href
                    # 定位商品名称并去空格
                    sku_name = soup_href.find('div', class_='sku-name')
                    product_name = str(sku_name.get_text()).strip()
                    # 产品Id
                    search_ID = re.search('\d+', real_href)
                    product_ID = search_ID.group()
                    post = {  ##这是构造一个字典，里面有啥都是中文，很好理解吧！
                        '标题': title,
                        '商品ID': product_ID,
                        '商品': product_name,
                        '商品标题': title,
                        '链接地址：': real_href,
                        '价格': price,
                        '获取时间': datetime.datetime.now()
                    }
                    print(post)
                except:
                    pass
                # if price != 0:  # 清洗s数据
                #     if self.jingdong_collection.find_one({'商品ID': href}):  ##判断这个主题是否已经在数据库中、不在就运行else下的内容，在则忽略。
                #         print(u'这个页面已经爬取过了')
                #     else:
                #         post = {  ##这是构造一个字典，里面有啥都是中文，很好理解吧！
                #             '标题': title,
                #             '商品ID': product_ID,
                #             '商品': product_name,
                #             '商品标题': title,
                #             '链接地址：': real_href,
                #             '价格': price,
                #             '获取时间': datetime.datetime.now()
                #         }
                #         self.jingdong_collection.save(post)  ##将post中的内容写入数据库。
                #         print(u'插入数据库成功')
                #         print('商品ID：', product_ID)
                #         print('商品：', product_name)
                #         print('商品标题：', title)
                #         print('链接地址：', real_href)
                #         print('价格：', price)
                #         print('*************************************************************************')
                #         with open('jingdong.csv', 'a', newline='', encoding='gbk') as csvfile:  # 保存到CSV列表里
                #             writer = csv.writer(csvfile)
                #             writer.writerow([product_ID, product_name, title, real_href, price])
                #         time.sleep(1)
                # else:
                #     continue

    # 解析网页utf-8
    def requests_utf(self, url):
        UA = random.choice(self.user_agent_list)  # 随机选择请求头部
        headers = {'User-Agent': UA}
        try:
            content = requests.get(url, headers=headers, timeout=3)
            content.encoding = 'utf-8'  # 设置content为utf-8，否则会出现乱码
            soup = BeautifulSoup(content.text, 'lxml')
            return soup
        except:
            print(u'开始使用代理')
            time.sleep(10)
            IP = ''.join(str(random.choice(self.iplist)).strip())  ##下面有解释哦
            proxy = {'http': IP}
            try:
                content = requests.get(url, headers=headers, proxies=proxy, timeout=3)
                content.encoding = 'utf-8'
                soup = BeautifulSoup(content.text, 'lxml')
                return soup
            except:
                time.sleep(10)
                IP = ''.join(str(random.choice(self.iplist)).strip())
                proxy = {'http': IP}
                print(u'正在更换代理，10S后将重新获取')
                print(u'当前代理是：', proxy)
                return self.requests_utf(url=url)

    # 解析网页gbk
    def requests_gbk(self, url):
        UA = random.choice(self.user_agent_list)  # 随机选择请求头部
        headers = {'User-Agent': UA}
        try:
            content = requests.get(url, headers=headers, timeout=3)
            content.encoding = 'gbk'  # 设置content为utf-8，否则会出现乱码
            soup = BeautifulSoup(content.text, "html.parser", from_encoding="gbk")
            return soup
        except:
            print(u'开始使用代理')
            time.sleep(10)
            IP = ''.join(str(random.choice(self.iplist)).strip())  ##下面有解释哦
            proxy = {'http': IP}
            try:
                content = requests.get(url, headers=headers, proxies=proxy, timeout=3)
                content.encoding = 'gbk'
                soup = BeautifulSoup(content.text, "html.parser", from_encoding="gbk")
                return soup
            except:
                time.sleep(10)
                IP = ''.join(str(random.choice(self.iplist)).strip())
                proxy = {'http': IP}
                print(u'正在更换代理，10S后将重新获取')
                print(u'当前代理是：', proxy)
                return self.requests_gbk(url=url)


jd = JD()
search_word = '洗面奶'
url = 'https://search.jd.com/Search?keyword=' + search_word + '&enc=utf-8'
jd.req(url)
# -*- coding:utf-8 -*-
