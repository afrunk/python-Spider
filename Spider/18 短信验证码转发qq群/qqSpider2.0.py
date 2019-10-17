"""

抓取平台的短信通知 转发到qq群
- 技术点
    读写csv文件监测数据是否被抓到过：这个方法等到数据量越来越大得时候就会导致不及时 所以改为抓取短信后得时间是否为5分钟内 如果是则发送到qq群
    修改为数据库 存储数据 然后设置手机号和时间为主键 如果同时重复则不写入
    查询数据库数据 然后将当前获取到得10个数据进行遍历 查询是否已经存在数据库中 如果存在则不写入数据库 并且不发送qq群 如果不存在则写入和发送qq群
    import win32con,win32gui
    使用win32调用窗口来实现qq群信息发送：参考文章https://www.cnblogs.com/xiaohe520/p/10973307.html
"""

import requests
from bs4 import BeautifulSoup
import win32con,win32gui,time
import win32clipboard as w #剪贴板
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()

headers ={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=3mebt02pn1q53h7sraujlll3a6',
        'Host': '47.96.101.22:9999',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',

    }

# 将数据发送到qq群

def sendQ(telephone,code):
    # 设置部分
    windowtitle = '骑着码去嗨'  # 窗口名
    hwnd = win32gui.FindWindow(None, windowtitle)


    # 设置剪贴板文本
    aString = telephone +" "+ code  # 需要发送得信息
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)

    # 测试剪贴板文本
    w.CloseClipboard()
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    print(d)

    # 发送部分
    win32gui.PostMessage(hwnd,win32con.WM_PASTE, 0, 0)  # 向窗口发送剪贴板内容(粘贴) QQ测试可以正常发送
    time.sleep(0.3)
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 向窗口发送 回车键
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


    # 实现功能部分
    print('找到%s' % windowtitle)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 窗口获取坐标
    print(left, top, right, bottom)
    print('窗口尺寸', right - left, bottom - top)
    win32gui.MoveWindow(hwnd, 20, 20, 405, 756, True)  # 改变窗口大小
    time.sleep(6)
    win32gui.SetBkMode(hwnd, win32con.TRANSPARENT)  # 设置为后台

# 主函数
# 获取数据 查询是否再数据库中 不存在则写入数据库 发送qq群 存在则跳过
def getContent():
    infos = [] # 存储最新抓取到得数据
    # 从数据库查询数据 然后去遍历


    url = 'http://47.96.101.22:9999/index.php?g=cust&m=smscust&a=receive'
    con = requests.get(url,headers=headers).text
    # print(con)
    soup = BeautifulSoup(con,'lxml')
    # 定位到电话和验证码地区
    table = soup.find('table',class_='table table-hover table-bordered table-list')
    # print(table)
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    for tr in trs:
        content = tr.text.rsplit(' ')[1:6] # 将电话和验证码匹配出来
        del content[2] # 删除无用信息
        del content[2] # 删除无用信息
        content[1]=content[1].replace('\t','')[:18] # 处理获取到得信息只获取我们所需要得信息
        # print(content)
        infos.append(content) # 将处理好得数据结构存入列表
    # print(infos)
    sql_1 = 'select * from message'
    cursor.execute(sql_1)
    already =cursor.fetchall() # 必须存下来否则只执行一次
    # 因为高峰期 一分钟 50条 那么就需要5s一次请求
    for info in range(len(infos)): # 遍历获取到得数据
        biaozhifu =1 # 标识符 如果已经存在数据库中了就修改为0 这样就不再发送和写入数据库
        print(infos[info])
        # 首先查看是否存在数据库中了
        for j in already:
            if j[0]==infos[info][0] and j[1]==infos[info][1] and j[2]==infos[info][2]:
                print("已存在")
                biaozhifu = 0
                # tel1=infos[info][0][:3]
                # tel2=infos[info][0][6:]
                # infos[info][0] = tel1+'**'+tel2
                # sendQ(infos[info][0], infos[info][1], ) # 测试qq是否可以转发
            else:
                # print("NO")
                pass

        if(biaozhifu): # 如果不存在 则写入数据库

            # 将数据插入到数据库 手机号 验证码 时间
            # try:
            #     sql_2 = """
            #                             INSERT IGNORE INTO message ( telephone,code,date1)VALUES('{}','{}','{}'  )
            #                                 """ \
            #         .format(
            #         pymysql.escape_string(infos[info][0]),
            #         pymysql.escape_string(infos[info][1]),
            #         pymysql.escape_string(),
            #     )
            #     # print(sql_2)
            #     cursor.execute(sql_2)  # 执行命令
            #     db.commit()  # 提交事务
            # except:
            #     pass

            # 将数据发送到 qq 群
            tel1 = infos[info][0][:3]
            tel2 = infos[info][0][7:]
            infos[info][0] = tel1 + '****' + tel2 # 隐藏号码 拼接之后发送到qq群
            # print(infos[info][0])
            infos[info][1] = infos[info][1].replace('【滴滴出行】','') # 去掉滴滴出行
            sendQ(infos[info][0],infos[info][1])

if __name__=='__main__':
    getContent() # 主函数
    # telephone, code, timed = '1', '1', '1'
    #
    # sendQ(telephone,code,timed) # 测试发送qq信息


