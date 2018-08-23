# Selenium

Selenium是模拟测试工具，在开发基于Selenium的Task时应该遵循模拟用户的操作这一原则。比如在抓取网络数据时，通常的思路是通过嗅探headers字段，构造http请求并解析返回结果，但是在selenium中需要模拟的是用户的输入、下滑、翻页等操作，然后通过driver的page_source拿到网页源码然后解析。
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
