# 引入两个库
# # requests 库是请求
# # beautifulsoup 是分析html结构的库
import requests
from bs4 import BeautifulSoup
# 请求头部 用于网站验证你的请求是否合理 再requests.get方法中使用
headers ={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Referer':'http://www.jianlaixiaoshuo.com/'
}
# 目标网站链接
url='http://www.jianlaixiaoshuo.com/book/694.html'
# 使用requests 库请求 html，将请求到的html存入到我们定义的变量html中 这里使用到了上面的头部
html = requests.get(url,headers=headers)
# 如果 reqests.get().status_code ==200 的话就是请求成功了
if html.status_code == 200:
	# 因为网站的字符使用的是非 utf-8 编码 将其修改为 utf-8
    html.encoding='utf-8'
    # 使用BeautifulSoup库来分析我们获取到的HTML 文件，将html转成text形式只需要再上面的html变量后加.text即可 ，lxml是分析方法 默认即可
    soup = BeautifulSoup(html.text,'lxml')
    # 这是使用Beatifulsoup 库的 find()方法来找寻HTML文件中我们要抓取的小说内容 后加text是去掉HTML文件的标签
    content = soup.find('div',id='BookText').text
    # 输出我们匹配到的正文
    print(content)
    # 打开jianlai.txt文本，w是写入的意思，encoding='utf-8'和上面一样进行字符转换成我们可以正常浏览的字符格式 
    # as f 是将打开的文本用f来代替
    with open('jianlai2.txt','w+',encoding='utf-8') as f:
        # 将content写入jianlai.txt
        f.write(content)
        # 关闭文本
        f.close()