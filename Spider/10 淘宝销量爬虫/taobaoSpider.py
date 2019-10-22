"""
已知80家淘宝店铺名
需要抓取店铺的所有宝贝价格极其销量存入数据库 计算每月的销售额

- 获取80家店铺的列表链接：不能拼接 直接获取html页面链接 拼接成页数
    - 即便是使用休眠也会被抓 大概是15页左右就会被暂停
- 抓取HTML的销售和价格

换一家店铺需要修改三处：
    - 换一家店铺需要修改的地方0（店铺名）
    - 换一家店铺需要修改的地方1（链接）
    - 换一家店铺需要修改的地方2（链接）

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
        'cookie' : 'tk_trace=1; _tb_token_=3e0b3e1e31ed8; cookie2=18574660a3cd17cd81297811ef777349; hng=CN%7Czh-CN%7CCNY%7C156; t=bd0a39c7ebb49640d55e865b9dc89f22; cna=EjzNFcjlwBgCAW41PyFszgpg; dnk=tb711720904; uc1=existShop=false&cookie14=UoTbnVA9Qk0A6w%3D%3D&tag=8&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&lng=zh_CN&pas=0&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie21=URm48syIYn73; uc3=vt3=F8dByuDg%2BZfTc02ENqE%3D&id2=UUphyuFCFnCCXvrq5Q%3D%3D&lg2=URm48syIIVrSKA%3D%3D&nk2=F5RCZIyPD2jwAMM%3D; tracknick=tb711720904; lid=tb711720904; uc4=nk4=0%40FY4JikEC%2F4ed8p%2FwI0te0Ucl8cOvJw%3D%3D&id4=0%40U2grEadKyKZ%2BnRbthvVVrPgYgt5F%2BvOF; lgc=tb711720904; csg=731dc922; enc=UgKk2g9%2FoIvvsWRx7%2FcNSqXeO5bm08%2BP1D4SoyfKza5%2FkD85FT%2FWNPimEA%2Fr6AHUqynRUnrpQ1Yq5j06sR8ZfQ%3D%3D; sm4=620100; _m_h5_tk=bcf27ba4f23fdfbe88b0e7c42833af75_1571511609711; _m_h5_tk_enc=88eb7edb109111ee6fe2a50ab3eb0df5; pnm_cku822=; cq=ccp%3D1; l=dB_G4zXuqYHDP-qEBOCNhsl0Bvb9sIRAgurDmBVyi_5Bf1Ls497OkMPnfep6cfWfGIYB4NSLzt29-etktEpTY-DJl8r0mxDc.; isg=BPHxq0svCC6epqTRcBMDgYv0AH3viiSJyERs5NMG7LjX-hFMGytNIAYQHMY5Mv2I',
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
    url='https://nikekids.tmall.com/i/asynSearch.htm?_ksTS=1571504096126_588&callback=jsonp589&mid=w-18225450466-0&wid=18225450466&path=/category.htm&spm=a1z10.5-b-s.w4011-18225450466.427.2ec410752p259Q&search=y&pageNo=1' # 第一页的链接
    # 获取HTML页面
    # 第一页不需要查看是否被反爬 肯定可以运行 不判断
    OnePageHtml=getHtml(url)
    # print(OnePageHtml)
    # print(OnePageHtml)
    page=OnePageHtml.find('b',class_='\\"ui-page-s-len\\"').text.replace("1/","") # class_='\"ui-page-s\"' 里面要加反斜杠 否则匹配不到 转换成text后 替换掉前面的当前页面 获取总页数
    print(page)
    details = OnePageHtml.find_all('a',class_='\\"item-name') # 商品名
    cPrices = OnePageHtml.find_all('span',class_='\\"c-price\\"') # 价格
    saleNUms= OnePageHtml.find_all('span',class_='\\"sale-num\\"') # 销量
    title = OnePageHtml.find_all('div',class_='\\"title\\"') # 评论
    # 前60为正常 获取这60个数据切片
    details =details[:60]
    cPrices = cPrices[:60]
    saleNUms = saleNUms[:60]
    tt= title[:60]
    for num,i,j,k,p in zip(range(1,len(details)+1),details,cPrices,saleNUms,tt): # 60为正常的 后续的为推荐
        thingname = i.text.strip() # 商品名
        price = j.text # 价格
        sale = k.text #销量
        title = p.text.replace('|评价:' ,'') # 评价
        print(str(num)+'\t'+thingname,price,sale,title) # 输出
        data = [thingname,price,sale,title]
        # 存入csv
        import csv
        with open("NewData.csv", 'a+', newline='') as f:  # 写入到本地csv中 a+会自动创建文件 newline解决中间有空行的问题
            write = csv.writer(f)
            write.writerow(data)




        # 插入数据库
        # try:
        #     sql_2 = """
        #                 INSERT IGNORE INTO taobao (thingname,price,sale,shopName)VALUES('{}','{}','{}','{}' )
        #                 """ \
        #         .format(
        #                 pymysql.escape_string(thingname),
        #                 pymysql.escape_string(price),
        #                 pymysql.escape_string(sale),
        #                 pymysql.escape_string(shopName),)
        #     # print(sql_2)
        #     cursor.execute(sql_2)  # 执行命令
        #     db.commit()  # 提交事务
        # except:
        #     print("当前sql语句出错")
    # 随机睡眠1-5s
    # sleepTime= random.randint(20,30)
    # print("随机休眠{}秒".format(sleepTime))
    # time.sleep(sleepTime)


    # 循环Page数 有多少页商品就循环多少页
    for i in range(2,10):
        # 每十页中间间隔一个比较长的时间段 看看能不能将这个店铺全部抓取下来
        # if i%10==0:
        #     sleepTime = random.randint(150, 300)
        #     print("随机休眠{}秒".format(sleepTime))
        #     time.sleep(sleepTime)

        print("当前正在输出的是第{}页数据:\n".format(i))

        # 换一家店铺需要修改的地方2（链接）
        # url='https://hm.tmall.com/i/asynSearch.htm?_ksTS=1570435935932_129&callback=jsonp130&mid=w-17871033836-0&wid=17871033836&path=/category.htm&spm=a1z10.5-b-s.w4011-17871033836.421.11b36a4fdZlBbN&scene=taobao_shop&pageNo={}'.format(i)
        url='https://nikekids.tmall.com/i/asynSearch.htm?_ksTS=1571504096126_588&callback=jsonp589&mid=w-18225450466-0&wid=18225450466&path=/category.htm&spm=a1z10.5-b-s.w4011-18225450466.427.2ec410752p259Q&search=y&pageNo={}'.format(i)
        print(url)
        # 可以返回HTML和 False 判断是否被反爬
        OnePageHtml = getHtml(url)
        # print(OnePageHtml)
        #返回的不是 False即可运行
        if OnePageHtml:
            details = OnePageHtml.find_all('a', class_='\\"item-name')  # 商品名
            cPrices = OnePageHtml.find_all('span', class_='\\"c-price\\"')  # 价格
            saleNUms = OnePageHtml.find_all('span', class_='\\"sale-num\\"')  # 销量
            title = OnePageHtml.find_all('div', class_='\\"title\\"')  # 评论
            tt = title[:60]
            # 前60为正常 获取这60个数据切片
            details = details[:60]
            cPrices = cPrices[:60]
            saleNUms = saleNUms[:60]
            for num, i, j, k, p in zip(range(1, len(details) + 1), details, cPrices, saleNUms, tt):  # 60为正常的 后续的为推荐
                thingname = i.text.strip()  # 商品名
                price = j.text  # 价格
                sale = k.text  # 销量
                title = p.text.replace('|评价:', '')  # 评价
                print(str(num) + '\t' + thingname, price, sale, title)  # 输出
                data = [thingname, price, sale, title]
                # 存入csv
                import csv
                with open("NewData.csv", 'a+', newline='') as f:  # 写入到本地csv中 a+会自动创建文件 newline解决中间有空行的问题
                    write = csv.writer(f)
                    write.writerow(data)

                # 将数据插入数据库 出去价格  销量 商品名 多添加一个店铺名
                # 后续第二次抓取的时候可以考虑使用更新的语句来更新后面的销量和价格
                '''
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
                '''

            # 每次抓取后随机睡眠时间
            # sleepTime = random.randint(20,30)
            # print("随机休眠{}秒".format(sleepTime))
            # time.sleep(sleepTime)
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
    shopName = 'nike'
    floge=getPages(shopName)
    if floge==False:
        print("该店铺没有抓取完成！")

