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
