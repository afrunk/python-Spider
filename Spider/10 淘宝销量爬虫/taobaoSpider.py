"""
已知80家淘宝店铺名
需要抓取店铺的所有宝贝价格极其销量存入数据库 计算每月的销售额

- 获取80家店铺的列表链接：不能拼接 直接获取html页面链接 拼接成页数
    - 即便是使用休眠也会被抓 大概是15页左右就会被暂停
- 抓取HTML的销售和价格

"""
import requests
from bs4 import BeautifulSoup
# 链接数据库的部分
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root', #用户名
                     password='password', #密码
                     db='world', # 数据库名
                     charset='utf8')
cursor = db.cursor()
import time
import random # 随机函数

# get请求头部 淘宝只需要cookies即可
headers={
        'cookie' : 'tk_trace=1; _tb_token_=3e0b3e1e31ed8; cookie2=18574660a3cd17cd81297811ef777349; dnk=%5Cu592A%5Cu9633%5Cu6253%5Cu8FC7%5Cu59293; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=%5Cu592A%5Cu9633%5Cu6253%5Cu8FC7%5Cu59293; lid=%E5%A4%AA%E9%98%B3%E6%89%93%E8%BF%87%E5%A4%A93; lgc=%5Cu592A%5Cu9633%5Cu6253%5Cu8FC7%5Cu59293; t=bd0a39c7ebb49640d55e865b9dc89f22; enc=VzyS%2BmqVmwlmIA6h8I0eXxP1CwT2iMskiEDKaqdocSn2spzIguuiALxldjR64RHWCBhcuPKTGfkxpEsZ8JzkuQ%3D%3D; cna=EjzNFcjlwBgCAW41PyFszgpg; pnm_cku822=; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=U%2BGCWk%2F7owY3j65jYmvyog%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=true&pas=0&cookie14=UoTbnVwKwZ85dA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByuDkNyFGxYwDSYA%3D&nk2=r%2F6VoYQWefKUHyg%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=UUGgrBMupDJ2Ow%3D%3D; uc4=nk4=0%40rRwWs36JPEMAsBoASUwEUhQ%2FYmj3Iw%3D%3D&id4=0%40U2OXlsSGhXw1xkzEhLjc7lPzPBDA; _l_g_=Ug%3D%3D; unb=2921647573; cookie1=BxJPuBc4luAo%2B2V2c7IOo2fvwTvX80L91cAbBWuzm0w%3D; login=true; cookie17=UUGgrBMupDJ2Ow%3D%3D; _nk_=%5Cu592A%5Cu9633%5Cu6253%5Cu8FC7%5Cu59293; sg=333; csg=30c3bfb1; cq=ccp%3D0; x5sec=7b2273686f7073797374656d3b32223a223461616230326262623065623336316536633362663935343563336661633232434b5470362b774645494c6736366675694d664938774561444449354d6a45324e4463314e7a4d374d673d3d227d; l=cB_G4zXuqYHDPthXBOCwourza77OSIRAguPzaNbMi_5I86LsdWbOkOrBJFp6VfWdtZYB4tm2-g29-etkiZLJJei8uxDc.; isg=BJmZtctUIJIQu_zZGFvbGWMsqIUXcmVAmatt-LtOFUA_wrlUA3adqAfUxM4R-iUQ',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
# 请求HTML页面的函数
def getHtml(url):
    # 标记 是否被反爬
    flag=True
    con=requests.get(url,headers=headers)
    if con.status_code==200:
        con.encoding = con.apparent_encoding # 转换编码避免乱码
        soupText=BeautifulSoup(con.text,'lxml') # con.text Bs4库才好解析 可替换为con.content
        return soupText
    else:
        flag= False
        return flag

# 获取宝贝信息写入数据库
def getPages(shopName):
    # 换一家店铺需要修改的地方1（链接）
    # 第一次获取HTML得到循环Page数 为后续的循环做准备
    url='https://hm.tmall.com/i/asynSearch.htm?_ksTS=1570435935932_129&callback=jsonp130&mid=w-17871033836-0&wid=17871033836&path=/category.htm&spm=a1z10.5-b-s.w4011-17871033836.421.11b36a4fdZlBbN&scene=taobao_shop&pageNo=1' # 第一页的链接
    # 获取HTML页面
    # 第一页不需要查看是否被反爬 肯定可以运行 不判断
    OnePageHtml=getHtml(url)
    # print(OnePageHtml)
    page=OnePageHtml.find('b',class_='\\"ui-page-s-len\\"').text.replace("1/","") # class_='\"ui-page-s\"' 里面要加反斜杠 否则匹配不到 转换成text后 替换掉前面的当前页面 获取总页数
    print(page)
    details = OnePageHtml.find_all('a',class_='\\"item-name') # 商品名
    cPrices = OnePageHtml.find_all('span',class_='\\"c-price\\"') # 价格
    saleNUms= OnePageHtml.find_all('span',class_='\\"sale-num\\"') # 销量
    # 前60为正常 获取这60个数据切片
    details =details[:60]
    cPrices = cPrices[:60]
    saleNUms = saleNUms[:60]
    for num,i,j,k in zip(range(1,len(details)+1),details,cPrices,saleNUms): # 60为正常的 后续的为推荐
        thingname = i.text.strip() # 商品名
        price = j.text # 价格
        sale = k.text #销量
        print(str(num)+'\t'+thingname,price,sale) # 输出
        # 插入数据库
        try:
            sql_2 = """
                        INSERT IGNORE INTO taobao (thingname,price,sale,shopName)VALUES('{}','{}','{}','{}' )
                        """ \
                .format(
                        pymysql.escape_string(thingname),
                        pymysql.escape_string(price),
                        pymysql.escape_string(sale),
                        pymysql.escape_string(shopName),)
            # print(sql_2)
            cursor.execute(sql_2)  # 执行命令
            db.commit()  # 提交事务
        except:
            print("当前sql语句出错")
    # 随机睡眠1-5s
    sleepTime= random.randint(20,30)
    print("随机休眠{}秒".format(sleepTime))
    time.sleep(sleepTime)

    # 循环Page数 有多少页商品就循环多少页
    for i in range(70,int(page)+1):
        # 每十页中间间隔一个比较长的时间段 看看能不能将这个店铺全部抓取下来
        if i%10==0:
            sleepTime = random.randint(150, 300)
            print("随机休眠{}秒".format(sleepTime))
            time.sleep(sleepTime)

        print("当前正在输出的是第{}页数据:\n".format(i))

        # 换一家店铺需要修改的地方2（链接）
        url='https://hm.tmall.com/i/asynSearch.htm?_ksTS=1570435935932_129&callback=jsonp130&mid=w-17871033836-0&wid=17871033836&path=/category.htm&spm=a1z10.5-b-s.w4011-17871033836.421.11b36a4fdZlBbN&scene=taobao_shop&pageNo={}'.format(i)
        # 可以返回HTML和 False 判断是否被反爬
        OnePageHtml = getHtml(url)
        #返回的不是 False即可运行
        if OnePageHtml:
            details = OnePageHtml.find_all('a', class_='\\"item-name')  # 商品名
            cPrices = OnePageHtml.find_all('span', class_='\\"c-price\\"')  # 价格
            saleNUms = OnePageHtml.find_all('span', class_='\\"sale-num\\"')  # 销量
            # 前60为正常 获取这60个数据切片
            details = details[:60]
            cPrices = cPrices[:60]
            saleNUms = saleNUms[:60]
            for num, i, j, k in zip(range(1, len(details) + 1), details, cPrices, saleNUms):  # 60为正常的 后续的为推荐
                thingname = i.text.strip()  # 商品名
                price = j.text  # 价格
                sale = k.text  # 销量
                print(str(num) + '\t' + thingname, price, sale)  # 输出
                # 将数据插入数据库 出去价格  销量 商品名 多添加一个店铺名
                # 后续第二次抓取的时候可以考虑使用更新的语句来更新后面的销量和价格
                try:
                    print(id)
                    sql_2 = """
                                INSERT IGNORE INTO taobao (thingname,price,sale,shopName)VALUES('{}','{}','{}','{}' )
                                """ \
                        .format(
                                pymysql.escape_string(thingname),
                                pymysql.escape_string(price),
                                pymysql.escape_string(sale),
                                pymysql.escape_string(shopName), )
                    # print(sql_2)
                    cursor.execute(sql_2)  # 执行命令
                    db.commit()  # 提交事务

                except:
                    print("当前sql语句出错")
            # 每次抓取后随机睡眠时间
            sleepTime = random.randint(20,30)
            print("随机休眠{}秒".format(sleepTime))
            time.sleep(sleepTime)
        else:
            # 如果返回else则将当前抓取到的页数记录下来 并终止程序
            content="{} 抓取到第{}页失败 ".format(shopName,i)
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(content + '\n')
                f.close()
            return False

if __name__=='__main__':

    # 存入数据库 方便后续计算每月销售额
    # 换一家店铺需要修改的地方0（店铺名）
    shopName = 'HM'
    floge=getPages(shopName)
    if floge==False:
        print("该店铺没有抓取完成！")

