"""
date:2019-10-6
author_:afrunk
KnowladgePoints: requests beautoful PythonEmail
Target website:http://www.tom61.com/ertongwenxue/shuiqiangushi/

爬取睡前故事 4000多个存入数据库 然后每天定时从数据库读取未发送过的故事给指定邮件

"""

# 封装好的requests.get()获取HTMl文件的函数
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

def getHtml(url):
    con=requests.get(url)
    con.encoding = con.apparent_encoding # 转换编码避免乱码
    soupText=BeautifulSoup(con.text,'lxml') # con.text Bs4库才好解析 可替换为con.content
    return soupText


# 获取每个故事的url存入列表
def getUrlLists():
    urlPages =[] # 故事翻页链接列表 总70页
    urlList = [] # 具体故事内容列表 总4900个故事
    # http: // www.tom61.com / ertongwenxue / shuiqiangushi / index_70.html
    # 总共70页 第一页的index后无_1
    for i in range(1,71):
        if i<2:
            urlPages.append('http://www.tom61.com/ertongwenxue/shuiqiangushi/index.html') # 第一页的链接添加到列表
        else:
            pageReallyUrl = 'http://www.tom61.com/ertongwenxue/shuiqiangushi/index_{}.html'.format(i) #拼接故事链接列表页url
            # print(pageReallyUrl)
            urlPages.append(pageReallyUrl) # 将拼接链接添加到列表
    # print(urlPages) # 输出首页链接列表查看链接是否正确
    for i in range(0,70): # 70个链接
        print("当前抓取的首页是： "+urlPages[i])
        soupText = getHtml(urlPages[i]) # 将传过去的链接获取到的bs4解析后的页面传回来
        # print(soupText)
        # 所有的链接都存放在dd列表中 dl的class=text_box 匹配它
        dl_real=soupText.find('dl',class_='txt_box')
        dds_real=dl_real.find_all('dd') # 匹配dl下所有dd链接 url存放在dd标签下的a标签中
        # print(dds_real)
        for dd_real in dds_real:
            story_real='http://www.tom61.com/'+dd_real.find('a',target='_blank').get('href') # 匹配dd下的a标签 获取其中的href链接
            # print(story_real)
            urlList.append(story_real) # 存入故事链接列表中
    print(len(urlList))
    return urlList

# 读取故事链接 获取故事标题和正文存入数据库
def getStroyTextToMysql():
    urlList = getUrlLists()  # 将每个故事的链接传回以便for循环遍历
    try:
        for i in range(4051,len(urlList)):
            storyHtml = getHtml(urlList[i])  # 调用获取html页面的函数获取具体的故事页面内容
            t_news = storyHtml.find('div', class_='t_news')  # 匹配有标题和故事正文的div标签
            titleStory = t_news.find('h1').text  # 标题
            t_news_txt = t_news.find('div', class_='t_news_txt').text  # 正文
            print(titleStory)
            print(t_news_txt + '\n')
            # pymysql 插入数据到数据库的语句
            # try 避免插入时报错导致程序停止
            try:
                sql_2 = """
                            INSERT IGNORE INTO storys (title,storyText)VALUES('{}','{}')
                                        """ \
                    .format(
                    pymysql.escape_string(titleStory),
                    pymysql.escape_string(t_news_txt),
                )
                print(sql_2)
                cursor.execute(sql_2)  # 执行命令
                db.commit()  # 提交事务
            except:
                pass
    except:
        pass
# 从数据库读取故事每日固定时间发送邮件
# 邮件组件设置
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='2226846894@qq.com'    # 发件人邮箱账号
my_pass = 'cyeykinkooacebce'              # 发件人邮箱密码(当时申请smtp给的口令)
my_user='1740384737@qq.com'      # 收件人邮箱账号，我这边发送给自己

def SendStoryToEmail():
    try:
        # 从数据库读取未被发送的故事
        sql='select * from storys where num=0 limit 1'
        cursor.execute(sql)
        # print(cursor.fetchall())
        for i in cursor.fetchall(): # 读取数据库获取到的cursor是一个嵌套列表 需要使用该方法来读取内容
            title=i[0]
            text=i[1]
            print(title)
            print(text)
            try:
                msg = MIMEText(text, 'plain', 'utf-8')
                msg['From'] = formataddr(["最爱汐希的主人", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                msg['To'] = formataddr(["汐希小母狗", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                msg['Subject'] = "每日睡前小故事"+ title # 邮件的主题，也可以说是标题

                server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
                server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
                server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.quit()  # 关闭连接
                # 发送该故事之后将其num值修改为 1 即被发送了
                sql_2="update storys  set num = 1 where title = '%s'" % (title)
                try:
                    cursor.execute(sql_2)  # 执行命令
                    db.commit()  # 提交事务
                except:
                    db.rollback()  # 回滚
            except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
                ret = False

    except:
        pass

if __name__=='__main__':
    # getStroyTextToMysql()
    SendStoryToEmail()

