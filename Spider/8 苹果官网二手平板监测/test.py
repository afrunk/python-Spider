# author:affrunk
# time:2019/5/24
import requests
from bs4 import BeautifulSoup
import re
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
#存储标题和价格
all_content_title=[]
all_content_price=[]
my_sender='2226846894@qq.com'    # 发件人邮箱账号
my_pass = 'cyeykinkooacebce'              # 发件人邮箱密码(当时申请smtp给的口令)
my_user='1740384737@qq.com'      # 收件人邮箱账号，我这边发送给自己

#发送邮件
def mail(content):
    ret=True
    try:
        msg=MIMEText(content,'plain','utf-8')
        msg['From']=formataddr(["IpadSpider",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["aff",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']='Apid 官网翻新检测提醒脚本'+content               # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

#获取页面当前ipad的属性判断是否有我们想要的
def get_content():
    data={}
    s=''
    url='https://www.apple.com/cn/shop/refurbished/ipad'
    content=requests.get(url).text
    bs=BeautifulSoup(content,'lxml')
    ipads_title=bs.find_all('h3')
    ipads_price=bs.find_all('div',class_='as-price-currentprice as-producttile-currentprice')
    # 保存上新时间
    rush_time = open('rushtime.txt', 'a')
    for ipad,price in zip(ipads_title,ipads_price):
        # print(ipad)
        title = ipad.text.strip()
        price = price.text.strip()
        data[title]=price
        flage=True
        #判断在存储数据的表格中是否有完全相同的 如果有的话不重复添加
        for i in range(len(all_content_title)):
            if(title==all_content_title[i] and price == all_content_price[i]):
                flage=False
        if(flage):
            print("有上新哦！")
            import datetime
            #打印当前时间到txt中保存记录
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            rush_time.write(nowTime+'\n')
            all_content_title.append(title)
            all_content_price.append(price)
    rush_time.close()
    print(data)
    for key, value in data.items():
        p=re.compile(r'10.5\s英寸\siPad Pro')
        if(p.search(key)):
            # print(key, value)
            print("匹配成功！")
            content=key+value
            ret = mail(content)
            if ret:
                print("邮件发送成功")
            else:
                print("邮件发送失败")



if __name__=='__main__':
    while(1):
        get_content()
        data=random.randint(55,65)
        #创建log.txt文件 w换成a之后就可以实现不替换原有内容而写入在文档最后
        f = open('log.txt', 'w')
        #输出整体列表 进行判断
        for i in range(len(all_content_title)):
            print(all_content_title[i],all_content_price[i])
            #将整体列表的数据覆盖的形式写入到txt运行日志中
            #参考文章 https://www.cnblogs.com/hackpig/p/8215786.html
            f.write(all_content_title[i])
            f.write(all_content_price[i]+'\n')
        f.close()
        print("休眠时间：",data)
        time.sleep(data)
