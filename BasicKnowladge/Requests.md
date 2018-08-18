# requests
python最为常用的http请求库。Requests是用python语言编写，基于urllib，采用Apache2 Licensed开源协议的HTTP库。
## 0.安装：
通过pip安装：
pip install requests
或者通过pycharm安装：直接在setting中找到当前环境，选择+号输入requests选择install即可安装。
## 1.响应和编码：
import requests
url='http://www.baidu.com'
r=requests.get(url)
print(type(r))        文本的标签类型
print(r.encoding)     文本的编码类型
print(r.cookies)      文本的cookies
print(r.status_code)  访问的状态：200的话证明访问正常
得到：
<class 'requests.models.Response'>
ISO-8859-1
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
200
print(r.text)
得到：
html页面（这个在sublime text中也存在区别，如果是在sublime中输出的话，就是报错，如果是使用框架输出在
cmd的话，可以实现但是会出现乱码的问题）
print(r.content)
得到：
一个二进制的html页面（中间的文本全部是二进制的文本。）
响应什么的都很简单，问题是requests使用之后总是会碰到乱码问题。
如何解决Requsts中文乱码问题？
方法一：使用r.content，得到的是bytes，再转为str。
import requests
url='http://www.baidu.com'
r=requests.get(url)
code=r.content
html=str(code,'utf-8')
print(html)
方法二：使用r.text，requestst会自动解码来自服务器的内容。大多数的unicode字符集都能被无缝地解码，请求发出后，requests会基于HTTP头部对响应的编码作出有根据的推测。并且可以通过使用r.encoding属性来改变他。
import requests
url='http://www.baidu.com'
r=requests.get(url)
r.encoding='utf-8'
print(r.text)
以上的两种方法可以解决绝大部分的问题 。如果仍然有问题的话可以参考参考文章的终极方法：链接地址http://blog.chinaunix.net/uid-13869856-id-5747417.html
if req.encoding == 'ISO-8859-1':
    encodings = requests.utils.get_encodings_from_content(req.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = req.apparent_encoding
# encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    global encode_content
    encode_content = req.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；
但是上面这个方法还是有点难受哈，所以我最后发现，这样子好像可以解决问题。因为这样子输出的代码并并不是乱码而且都是正常的代码来的。
import requests
res=requests.get("http://m.yikanxiaoshuo.net/2/2867/2218121.html")
print(res.headers['content-type'])
print(res.encoding)
print(res.apparent_encoding)
# print(requests.utils.get_encoding_form_cotent(page_content.text))
# res.encoding='GB2312'
res.encoding=res.apparent_encoding
print(res.text)
如何判断响应是否正确：
url = 'http://www.baidu.com'
r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.status_code)
    print(r.headers)
    print(r.headers.get('content-type'))#推荐用这种get方式获取头部字段
else:
    r.raise_for_status()
使用上述的方法可以避免被反扒之后报错，千篇一律的使用try\except的方法来避免报错真的是有点不好意思。
## 2.Get方法：
payload={'page':'1','per_page':'10'}
r=requests.get('http://httpbin.org/get',params=payload)
print(r.url)
get方法本来是直接拿来请求页面内容的，但是有些情况下，url会带参数，我们可以使用合并字符串的方法来构造url，不过requests提供了params关键字参数允许我们以一个字典来提供这些参数。需要注意的是字典里值为None的键不会被添加到url的查询字符串中。
## 3.POST方法：
使用requests发送POST请求也很简单，如下：
import requests
r=requests.post("http://ttpbin.org/post")
print(r)
发送编码为表单形式的数据：但是一般情况下，如果页面需要使用post来提取信息的话是不会这么简单的，要不然为什么不使用get方法呢？基本上都会需要我们发送编码为表单形式的数据。它能够过data参数传递一个dict，我们的数据字典在发送请求时会被自动编码为表单形式。
payload={'page':1,'per_page':10}
r=requests.post("http://httpbin.org/post",data=payload)
发送编码为JSON形式的数据：可是一般比较难的网站都是需要传递的JSON参数，万丈高楼平地起啊,想当初为了爬一个基金的网站，虽然也有300+的钱，可是就是数据是很简单的post就把我给难住了，不过如果不是经过了这么多的困难和代码的磨练，现在对于这样的基础的东西还是不会去主动接触和熟悉的。
import json
payload={'page':1,'per_page':10}
r=requests.post("http://httpbin.org/post",data=json.dumps(payload))
当时看康康找出来这样的写法还一脸蒙蔽，自己寻找文章的关键词都不知道，现在想起来也确实汗颜。不过，再回头看那个大牛其实也就这样吧。大家都在进步，这样的话自然而然很多东西就可以很清晰的看到了。当时康康写出来三种写法，确实是上面这种也被我采用了，看极客学院的文档发现还有一种方法应该也很简单。这种做法和上面的做法是等价的而且不需要导入json库，数据在发出时会被自动编码。
payload={'page':1,'per_page':10}
r=requests.post("http://httpbin.org/post",json=payload)
## 4.请求头headers处理：
import requests
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
url = 'https://github.com/afrunk'
r = requests.get(url,headers=header)
print(r.content)
我们可以通过print(r.request.headers)来输出我们发送到服务器的请求的头部。服务器返回给我们的头部信息可以通过r.headers访问。
## 5.HTTP响应：
• 普通响应：使用r.text获取，基本上可以读取大部分的网页数据，但是会存在部分的问题,所以需要使用到之前我们所说的方法。
import requests

r = requests.get("https://github.com/timeline.json")
print r.text
print r.encoding
• JSON响应：使用r.json()获取，一般情况下，这种数据很少见，一般情况下存在json文件中的数据也是字典格式的文本。
import requests

r = requests.get("https://github.com/timeline.json")

if r.status_code == 200:
    print r.headers.get('content-type')
    print r.json()
• 二进制响应：使用r.content获取，我们需要将图片写入到本地的时候，一般先获取到图片的二进制数据，然后写入到本地。
import requests

url = 'https://github.com/reactjs/redux/blob/master/logo/logo.png?raw=true'
r = requests.get(url)
image_data = r.content   # 获取二进制数据

with open('/Users/Ethan/Downloads/redux.png', 'wb') as fout:
    fout.write(image_data)
• 原始响应：使用r.raw获取,暂时没有碰到这样的情况，需要之后可以再来补充下吧。
## 6.重定向与超时设置：
默认情况下，除了HEAD，requestst会自动处理所有重定向，我们可以使用响应的history属性来追踪重定向。如，我们访问下面的链接：https://toutiao.io/k/c32y51，被重定向到了下面的链接：http://www.jianshu.com/p/490441391db6?hmsr=toutiao.io。
import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
r=requests.get('https://toutiao.io/k/c32y51',headers=headers,)
print(r.status_code)
print(r.url)
print(r.history)
print(r.history[0].text)
输出：
200
https://www.jianshu.com/p/490441391db6?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io
[<Response [302]>, <Response [301]>]
<html><body>You are being <a href="http://www.jianshu.com/p/490441391db6?hmsr=toutiao.io&amp;utm_medium=toutiao.io&amp;utm_source=toutiao.io">redirected</a>.</body></html>
我们看到r.history包含了一个response对象列表,我们可以用它追踪重定向。如我们使用get\post方法，可以使用all_redirects参数禁止重定向。
r=requests.get('https://toutiao.io/k/c32y51',headers=headers,allow_redirects=False)
print(r.url)
print(r.history)
print(r.text)
超时： 可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。
连接超时指的是在你的客户端实现到远端机器端口的连接时Request 会等待的秒数。一个很好的实践方法是把连接超时设为比 3 的倍数略大的一个数值，因为 TCP 数据包重传窗口 (TCP packet retransmission window) 的默认大小是 3
r = requests.get('https://github.com', timeout=5)
## 7.Cookie：
官方文档写的不是很好，一般情况下cookie都是放在headers中实现的。（可能是我的浅薄无知导致 的这样的理所当然的想法。）
>>> url = 'http://httpbin.org/cookies'
>>> cookies = dict(cookies_are='working')
>>> r = requests.get(url, cookies=cookies)
>>> r.text
'{"cookies": {"cookies_are": "working"}}'
## 8.会话对象：
会话对象让你能够跨请求保持某些参数。 它也会在同一个 Session 实例发出的所有请求之间保持 cookie， 期间使用 urllib3 的 connection pooling 功能。所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
## 9.代理：
如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求:
import requests
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
requests.get("http://example.org", proxies=proxies)
## 10.身份验证：
这个暂时没有概念。
## 参考文档：
1. python绿色通道的爬虫系列文章
2. requests的极客学院的文档
3. requests官方文档
## 参考文章：
	1. requests的中文乱码问题

