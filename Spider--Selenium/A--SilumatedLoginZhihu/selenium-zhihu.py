import os
from selenium import webdriver

username='17393115857'
password='zhihudashencys6'
web=webdriver.Chrome(executable_path='source/chromedriver.exe')
web.maximize_window()
#打开登录页面
web.get('https://www.zhihu.com/signup?next=%2F')
#切换至登录页面
web.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()

#输入账号密码
web.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(username)
web.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(password)
web.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()
# web.close()
print(web.title)
# os.system("pause")