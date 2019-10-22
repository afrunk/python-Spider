"""
我想要以“水杯”为关键词，淘宝搜索600条商品信息，获取商品的：名称(或代码)、价格、销量、材质、品牌。放到数据库或者Excel都行
不能乱码
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root', #用户名
                     password='password', #密码
                     db='world', # 数据库名
                     charset='utf8')
cursor = db.cursor()

from urllib.parse import quote
browser = webdriver.Firefox()   #初始化浏览器
wait = WebDriverWait(browser, 30)   #指定延时时间


def page_get(page):
    print('正在爬取第',page,'页')
    try:
        time.sleep(random.randint(5, 10))
        url = "https://s.taobao.com/search?q=" + quote('水杯')
        browser.get(url)  #连接淘宝网
        in_put = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))) #输入框
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager .form>.btn')))    #提交按钮
        in_put.clear()     #清空输入信息， 每次都要
        in_put.send_keys(page)  #输入信息
        submit.click()     #点击提交按钮
        print('连接成功')
        item_info()        #调用信息提取页面
    except TimeoutException:
        page_get(page)


def item_info():
    html = browser.page_source  # 获取html
    doc = pq(html)
    print("获取成功")
    items = doc('#mainsrp-itemlist .item').items()  # 形成可迭代列表
    print('这一页商品的的个数是', len(doc('#mainsrp-itemlist .item')), '件')

    # 遍历获取商品的信息
    for item in items:
        items_info = {
            'name': item.find('.row-2').text(),
            'price': item.find('.price>strong').text(),
            'deal-cnt': item.find('.deal-cnt').text(),
            'shop_name': item.find('.row-3 a').text(),
            'location': item.find('.row-3 .location').text(),
        }  # 一件商品的信息提取完毕
        result_save(items_info)  # 存储

def result_save(data):
    # print(data['name'],data['price'],data['deal-cnt'],data['shop_name'],data['location'])
    # try:
    sql_2 = """
                INSERT IGNORE INTO sousuotaobao (name1,price,dealcnt,shop_name,location)VALUES('{}','{}','{}','{}','{}' )
                """ \
        .format(
        pymysql.escape_string(data['name']),
        pymysql.escape_string(data['price']),
        pymysql.escape_string(data['deal-cnt']),
        pymysql.escape_string(data['shop_name']),
        pymysql.escape_string(data['location']),)
    # print(sql_2)
    cursor.execute(sql_2)  # 执行命令
    db.commit()  # 提交事务

    # except:
    #     print("当前sql语句出错")

import time
import random
def main():
    print("working")
    for page in range(2,10):
        page_get(page)


if __name__ == '__main__':
    main()

# tt = p.text # 评价
# print(str(num)+'\t'+thingname,price,sale,tt) # 输出