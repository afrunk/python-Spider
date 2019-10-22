"""
没问题的爬虫代码 10-22

"""



from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
browser = webdriver.Firefox()   #初始化浏览器
wait = WebDriverWait(browser, 30)   #指定延时时间
def search():#获取首页数据
    try:
        browser.get('https://www.taobao.com')
        input=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#q'))
        )
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input.send_keys('水杯')
        #time.sleep(10)
        submit.click()
        total=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()
def next_page(page_number):#翻页
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)
def get_products():#获取商品信息
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html=browser.page_source
    doc=pq(html)
    items=doc('#mainsrp-itemlist .items .item').items()#items可以返回所有的内容
    for item in items:
        product={
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product['price'],product['deal'],product['title'],product['shop'],product['location'],)
        sql_2 = """
                        INSERT IGNORE INTO sousuotaobao (name1,price,dealcnt,shop_name,location)VALUES('{}','{}','{}','{}','{}' )
                        """ \
            .format(
            pymysql.escape_string(product['price']),
            pymysql.escape_string(product['deal']),
            pymysql.escape_string(product['title']),
            pymysql.escape_string(product['shop']),
            pymysql.escape_string(product['location']), )
        # print(sql_2)
        cursor.execute(sql_2)  # 执行命令
        db.commit()  # 提交事务

def main():
    try:
        total=search()
        total=int(re.compile('(\d+)').search(total).group(1))
        for i in range(2,total+1):
            next_page(i)
    except Exception:
        print('出错了')
    finally:
        browser.close()
if __name__ == '__main__':
    main()
