#coding:utf-8

import time
from selenium import webdriver
from lxml import etree

import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')

# friend='1094470534'
friend='3303536393'
user='2226846894'
pw='tengxunsima7!'

#获取浏览器驱动
web=webdriver.Chrome(executable_path='source/chromedriver.exe')

#窗口最大化
web.maximize_window()

#浏览器地址定向为qq登录页面
web.get('http://i.qq.com')

#这里需要选中一下frame，否则找不到下面的需要的网页元素
web.switch_to.frame('login_frame')
web.find_element_by_id("switcher_plogin").click()

#账号输入框输入已知qq号
web.find_element_by_id('u').send_keys(user)

#密码输入框输入密码
web.find_element_by_id('p').send_keys(pw)

#点击自动登录按钮
web.find_element_by_id('login_button').click()

#让webdriver操纵当前页
web.switch_to.default_content()

#调到说说的url，friend你可以修改成你想要访问的任何空间
web.get('http://user.qzone.qq.com/'+friend+'/311')

next_num=0 #初始下一页的id

while True:
    for i in range(1,6):
        height=20000*i
        strWord="window.scrollBy(0,"+str(height)+")"
        web.execute_script(strWord)
        time.sleep(4)
    web.switch_to.frame("app_canvas_frame")
    #写入本地时编码问题
    # web.page_source.encoding=web.page_source.apparent_encoding
    # (web.page_source).encode('utf-8')
    selector = etree.HTML(web.page_source)
    divs = selector.xpath('//*[@id="msgList"]/li/div[3]')

    # 这里使用 a 表示内容可以连续不清空写入
    with open('qq_word-陈佳音.txt', 'a') as f:
        for div in divs:
            qq_name = div.xpath('./div[2]/a/text()')
            qq_content = div.xpath('./div[2]/pre/text()')
            qq_time = div.xpath('./div[4]/div[1]/span/a/text()')
            qq_name = qq_name[0] if len(qq_name) > 0 else ''
            qq_content = qq_content[0] if len(qq_content) > 0 else ''
            qq_time = qq_time[0] if len(qq_time) > 0 else ''
            print(qq_name, qq_time, qq_content)
            try:
                f.write(qq_time)
                f.write(qq_content + "\n")
            except:
                pass

    # 当已经到了尾页，“下一页”这个按钮就没有id了，可以结束了
    if web.page_source.find('pager_next_' + str(next_num)) == -1:
        break

    # 找到“下一页”的按钮，因为下一页的按钮是动态变化的，这里需要动态记录一下
    web.find_element_by_id('pager_next_' + str(next_num)).click()

    # “下一页”的id
    next_num += 1

    # 因为在下一个循环里首先还要把页面下拉，所以要跳到外层的frame上
    web.switch_to.parent_frame()