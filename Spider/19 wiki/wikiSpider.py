"""
爬取内容写入数据库

"""




import requests
from bs4 import BeautifulSoup
import pymysql
# 数据库链接设置
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root', #账号
                     password='password',#密码
                     db='world',#库名
                     charset='utf8')
cursor = db.cursor()


# 主链接
url ='https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E4%BA%BA%E6%B0%91%E8%A7%A3%E6%94%BE%E5%86%9B%E7%A9%BA%E5%86%9B'
con = requests.get(url).text
# print(con)
soup = BeautifulSoup(con, 'lxml')
table = soup.find('table',class_='toccolours')
# print(table)
trs = table.find_all('tr')
del trs[0] # 删去头部的无用链接
# print(trs)
urlsList = []
for tr in range(len(trs)): # 遍历每个tr获取我们所需要的飞机的具体的信息链接
    if tr == 0 or tr == 9 or tr == 10 or tr == 15 or tr == 18 or tr == 21 :# 有的链接在第二个td下 有的在第一个td下 这里需要查看具体的页面
        try:
            tds = trs[tr].find_all('td')
            urlReal = 'https://zh.wikipedia.org/'+tds[1].find('a').get('href') # 将链接拼接称为我们所需要的可以直接访问的
            # print(urlReal)
            urlsList.append(urlReal)#添加到访问列表中
        except:
            pass
    else:
        try:
            tds =  trs[tr].find_all('td')
            urlReal='https://zh.wikipedia.org/'+tds[0].find('a').get('href')
            # print(urlReal)
            urlsList.append(urlReal)
        except:
            pass

for i in range(len(urlsList)):#构造遍历
    pageurl = urlsList[i] # 拼接链接

    con = requests.get(pageurl).text # 转换为text 否则不能为 BeautifulSoup
    # print(con)
    soup = BeautifulSoup(con, 'lxml')
    try:
        stringLis =''# 将所有的内容都拼接到链接中
        table = soup.find('table', class_='infobox').find('tbody')
        if(len(table)>0): # 如果没有信息的话就获取不到数据 所以判断一下
            print("可以抓取到信息的链接 "+pageurl)
            # print(table)
            trs = table.find_all('tr')
            # print(trs)
            try:
                for tr in trs:
                    ss=tr.text.strip() #转为text 去掉空格和回车
                    # print(ss)
                    stringLis +=ss #拼接成一个字符串
                print(stringLis)
                print('\n')
                # 插入数据
                # try:
                # 数据库语句
                sql_2 = """
                                        INSERT IGNORE INTO aircraft ( pageurl,stringLis)VALUES('{}','{}'  )
                                            """ \
                    .format(
                    pymysql.escape_string(pageurl),
                    pymysql.escape_string(stringLis),
                )
                # print(sql_2)
                #执行数据库语句
                cursor.execute(sql_2)  # 执行命令
                # 更新
                db.commit()
                # except:
                #     pass
            except:
                pass
    except:
        pass

