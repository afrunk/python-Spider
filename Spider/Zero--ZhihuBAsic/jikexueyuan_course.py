#-*-coding:utf8-*-
import requests
import re

class spider(object):
	def __main__(self):
		print("开始爬取内容....")

	def getsource(self,url):
		html=requests.get(url)
		htmlencoding='utf8'
		return html.text

	def changepage(self,url,total_page):
		now_page=int(re.search('pageNum=(\d+)',url,re.S).group(1))
		page_group=[]
		for i in range(now_page,total_page+1):
			link=re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
			page_group.append(link)
		return page_group

	def geteveryclass(self,source):
		everyclass=re.findall('(<li id=.*?</li>)',source,re.S)
		return everyclass

	def getinfo(self,eachclass):
		info={}
		info['title']=re.search('title="(.*?)"',eachclass,re.S).group(1)
		b=re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>',eachclass,re.S).group(1).strip()
		# print(b)
		info['content']=b
		timeandlevel=re.findall('<em>(.*?)</em>',eachclass,re.S)#时间和等级都是在em中间
		info['classtime']=timeandlevel[0]
		info['classlevel']=timeandlevel[1]
		info['learnnum']=re.search('"learn-number">(.*?)</em>',eachclass,re.S).group(1)
		return info
	def saveinfo(self,classinfo):
		f=open('info.txt','a')
		for each in classinfo:
			f.writelines('title:'+each['title']+'\n')
			f.writelines('content'+each['content']+'\n')
			f.writelines('calsstime:'+each['classtime']+'\n')
			f.writelines('classlevel:'+each['classlevel']+'\n')
			f.writelines('learnnum:'+each['learnnum']+'\n')
		f.close()
if __name__=='__main__':
	classinfo=[]
	url='http://www.jikexueyuan.com/course/?pageNum=1'
	af=spider()
	all_links=af.changepage(url,97)
	#起始页和页数总数,将所有要遍历的url保存在page_group中
	for link in all_links:
		print("正在处理页面："+link)
		html=af.getsource(link)
		# print(html)
		#获取当前link的html页面内容
		everyclass=af.geteveryclass(html)
		# print(everyclass)
		#获取当前html页面中的课程的信息
		for each in everyclass:
			info=af.getinfo(each)
			classinfo.append(info)#保存我们提取出来的字典信息
	af.saveinfo(classinfo)	#将爬取到的内容保存在本地

