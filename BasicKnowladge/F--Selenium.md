# Selenium
[selenium-DOC](https://selenium-python.readthedocs.io/getting-started.html)<br>
Selenium是模拟测试工具，在开发基于Selenium的Task时应该遵循模拟用户的操作这一原则。比如在抓取网络数据时，通常的思路是通过嗅探headers字段，构造http请求并解析返回结果，但是在selenium中需要模拟的是用户的输入、下滑、翻页等操作，然后通过driver的page_source拿到网页源码然后解析。
## 一：获取页面内容
```python
from selenium import webdriver
web=webdriver.Chrome()
try:
	web.get("https://www.baidu.com")
	print(web.title)
	print(web.page_source)
except:
	pass
```
web.get方法会在页面的onload事件触发时立即返回，也就是说如果页面中有很多的ajax请求的话，web.get方法返回可能页面还没有加载完成。web还提供了一些find_element_by_\*方法方便定位到具体的DOm节点进行后续操作。同时selenium.webdriver.common.keys模块中提供了一些特定的键值来模拟用户输入操作。web.close()\web.quit()提供了关闭浏览器标签和关闭浏览器的方法。
### 1.页面等待：针对加载需要一定时间的页面
刚刚说道web.get方法会在onload时立即返回，对于大量使用ajax的页面我们可能无法正确获取目标元素，或者一些页面设置了延时加载策略，针对这种情况我们需要设置一个合理的等待策略，而Selenium提供了两种不同的等待策略：**显示**、**隐式**。<br>
**显示策略**就是自定一个等待时间，如果在指定时间到达时不能顺利获取元素则抛出异常，其本质就是简单的time.sleep，selenium为这种情况封装了更为便捷的语法：
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Chrome()
driver.get('https://translate.google.cn/#en/zh-CN')
try:
    element=WebDriverWait(driver,10)
finally:
    driver.quit()
```
隐式策略则是设置一个固定的等待时间，如果在这个时间之内找到元素返回，如果到时候仍未找到则抛出异常，这个固定的等待时间对driver全局有效。
```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
```
### 2.截图
使用save_screenshot方法保存网页截图。
```python
from selenium import webdriver

web=webdriver.Chrome()
web.get('https://github.com/afrunk')
web.maximize_window()#全屏展示
web.save_screenshot('1.png')
```
为了获取到特定元素的截图，我们可以先从driver中获取到该元素，然后取得元素的位置信息之后通过图片处理工具截取到，通过这样的方法可以轻松的获取到页面中的验证码、二维码等等一些结构信息便于后续的使用。甚至是可以通过实现动态的一个拉动效果实现拼图验证码的实现通过（这个思路在jack的[博客进阶教程](http://cuijiahua.com/blog/2018/03/spider-5.html)里面有体现）
### 3.查找单个元素的方法
```python
find_element_by_name   通过name查找
find_element_by_xpath  通过xpath查找
find_element_by_link_text   通过链接查找
find_element_by_partial_link_text    通过部分链接查找
find_element_by_tag_name   通过标签名称查找
find_element_by_class_name   通过类名查找
find_element_by_css_selector  通过css选择武器查找
```
## 二：元素交互操作
### 1.在页面中进行内容填写
**百度搜索交互**实现并返回搜索结果内容
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 创建一个浏览器对象
browser = webdriver.Chrome()
try:
    # 开启一个浏览器并访问https://www.baidu.com
    browser.get('https://www.baidu.com')
    # 在打开的网页响应中根据id查找元素   获取到查询框
    input = browser.find_element_by_id('kw')
    # 向查询框中输入Python
    input.send_keys('Python')
    # 模拟回车
    input.send_keys(Keys.ENTER)
    # 显示等待， 等待10秒
    wait = WebDriverWait(browser, 10)
    # 显式等待指定某个条件，然后设置最长等待时间。如果在这个时间还没有找到元素，那么便会抛出异常
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    # 输出当前的url
    print(browser.current_url)
    # 输出Cookies
    print(browser.get_cookies())
    # 输出页面响应内容
    print(browser.page_source)
finally:
    pass
    # 关闭浏览器
    # browser.close()
```
**淘宝搜索页面**实现内容的搜索和爬取
```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 申明一个浏览器对象
browser = webdriver.Chrome()
# 使用浏览器访问淘宝
browser.get('https://www.taobao.com')
# 根据ID查找元素
input_search = browser.find_element(By.ID,'q')
# 模拟输入PSV到输入框
input_search.send_keys('PSV')
time.sleep(2)
# 清空输入
input_search.clear()
input_search.send_keys('3DS')
button = browser.find_element(By.CLASS_NAME,'btn-search')
#在最后面的搜索栏点击搜索即可
# 模拟点击
button.click()
print(browser.page_source)
```
### 2.实现内容拖拽效果
`菜鸟编程`html拖拽效果实现
```python
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
# 切换id为iframeResult的frame
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
```

## 可应用方向
- 知乎：在selenium中打开这个连接：https://www.zhihu.com/explore 是可以不需要登陆的查看问题和回答，经过一番测试，只需要经过一系列的点击和下拉即可获取到全部内容，不过这样子确实比较繁琐。
