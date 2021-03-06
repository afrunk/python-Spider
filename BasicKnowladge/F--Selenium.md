# Selenium
[selenium-DOC](https://selenium-python.readthedocs.io/getting-started.html)<br>
[中文文档](https://selenium-python-zh.readthedocs.io/en/latest/api.html)
Selenium是模拟测试工具，在开发基于Selenium的Task时应该遵循模拟用户的操作这一原则。比如在抓取网络数据时，通常的思路是通过嗅探headers字段，构造http请求并解析返回结果，但是在selenium中需要模拟的是用户的输入、下滑、翻页等操作，然后通过driver的page_source拿到网页源码然后解析。
## 零：浏览器操作
### 1.控制浏览器
```python
#设置浏览器宽480高800显示
driver.set_window_size(480, 800)
#刷新当前页面
driver.refresh()
```
### 2.点击和输入
```python
driver.find_element_by_id("kw").clear()#清除文本
driver.find_element_by_id("kw").send_keys("selenium")#模拟按键输入
driver.find_element_by_id("su").click()#单击元素
#提交表单
search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()
```
### 3.鼠标事件
```python
perform() 执行所有ActionChains中存储的行为
context_click() 右击
double_click() 双击
drag_and_drop()	 拖动
move_to_elements()  鼠标悬停
```
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
获取元素的各个属性
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
# 申明一个浏览器对象
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element(By.ID,'zh-top-link-logo')
# 获取属性
print(logo.get_attribute('class'))
#获取文本值
print(logo.text)
#获取id
print(logo.id)
#获取位置
print(logo.location)
#获取标签名称
print(logo.tag_name)
#获取大小
print(logo.size)
# browser.close()
```
### 4.Frame元素的切换
```python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
# 将操作的响应数据换成iframeResult
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
print(source)
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
# 切换成父元素
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
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
实战项目：虎嗅拖拽验证码的通过
### 3.选项卡操作
在第一个选项卡打开百度 在第二个选项卡打开淘宝 在返回第一个选项卡打开python官网
```python
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 打开一个选项卡
browser.execute_script('window.open()')
print(browser.window_handles)
# 选择第二个选项卡
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')

driver.current_window_handle 获取当前窗口handle
driver.window_handles 获取所有窗口的handle，返回list列表
driver.switch_to.window(handle) 切换到对应的窗口
driver.close() 关闭当前窗口
```
### 4.文件上传
`driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')`
## 三：katalon Recorder傻瓜式操作
这个在[莫烦的教学视频](https://morvanzhou.github.io/)里面有，虽然是在一个公众号里面看到的方法，但是之前也是没有上心的，今天发现，我的天，怎么这么好用。可以很简单迅速的实现selenium的python程序代码输出实现一个页面的操作，但是仅仅限制在一个页面。<br>
### 第一步：安装FireFox的katalon Recorder插件
直接打开扩展中心，然后输入katalon Recorder即可找到插件，安装之后即可。
### 第二步：使用FireFox的插件来实现自动化操作
在FireFox中打开插件，然后点击下图的第一个标志Record，等到当前目标弹到浏览器之后再进入目标网站，需要注意的是这一步必须预先复制好目标网站的url。然后我们在当前网站进行的点击等等一系列操作，都可以看到插件给出的提示，而且在插件的页面也会有不停的添加Command的变化，等到所有的都完成之后点击Stop即可停止，再点击play即可观看浏览器自动化模拟我们之前的操作，这中间的速度都比较快，这些都需要我进一步处理代码的时候尽可能的使其变得像人的操作。如果没有问题，只需要点击Export即可看到代码块，我们只需要复制红色框内的代码和头文件即可。这就是一种最适合新手的傻瓜式的操作。
![操作页面](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/imgs/Katalon%20%20Recorder.png)
![代码复制页面](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/imgs/Katalon2.png)

## 可应用方向
- 知乎：在selenium中打开这个连接：https://www.zhihu.com/explore 是可以不需要登陆的查看问题和回答，经过一番测试，只需要经过一系列的点击和下拉即可获取到全部内容，不过这样子确实比较繁琐。
