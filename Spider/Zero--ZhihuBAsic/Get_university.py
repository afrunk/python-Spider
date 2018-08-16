#-*-coding:utf-8-*-
#__author__:afrunk
#chromedriver || selenium
from bs4 import BeautifulSoup
from selenium import webdriver

def get_university(url):
	print url
	driver = webdriver.Chrome (executable_path=r'C:\Users\Administrator.USER-20161101EP\AppData\Local\Google\Chrome\Application\chromedriver.exe')
	driver.get(url)
	data=driver.page_source
	# print data
	driver.close()
	bfcontent=BeautifulSoup(data,'lxml')
	
	biao1=bfcontent.find_all('tr','lin-gettr')
	for uni1 in biao1:
		uni11=uni1.find_all('td')
		# print str(uni1).decode('utf8')
		# print uni1.find_all('td')
		# 高校名称
		name1=uni11[0].text
		print name1
		# 所在省份
		shengfen1 = uni11[1].text
		print shengfen1
		# 学历层次
		cengci1 = uni11[2].text
		print cengci1
		# 全国热度排名
		hot1 = uni11[3].text
		print hot1
		# 所属类别
		leibie1 = uni11[4].text.split (' ')[0]
		print leibie1
		# 所属类别排名
		leibiepm1 = uni11[4].text.split (' ')[1]
		print leibiepm1
		# 高校链接
		link1 = 'http://gkcx.eol.cn' + str (uni11[0].find_all ('a')[0].get ('href')).strip ()
		print link1
		files=open(r'university.txt','a+')
		files.write(('%s,%s,%s,%s,%s,%s,%s'%(name1,shengfen1,cengci1,hot1,leibie1,leibiepm1,link1)).encode('utf-8')+'\n')
	
	"""if bfcontent.find_all ('tr', 'getJsXmlTr '):
		biao2 = bfcontent.find_all ('tr', 'getJsXmlTr ')
		for uni2 in biao2:
			uni22 = uni2.find_all ('td')
			# print str(uni2).decode('utf8')
			# print uni2.find_all('td')
			# 高校名称
			name2 = uni22[0].find_all ('a')[0].text
			print name2
			# 所在省份
			shengfen2 = uni22[1].text
			print shengfen2
			# 学历层次
			cengci2 = uni22[2].text
			print cengci2
			# 全国热度排名
			hot2 = uni22[3].text
			print hot2
			# 所属类别
			leibie2 = uni22[4].text.split (' ')[0]
			print leibie2
			# 所属类别排名
			leibiepm2 = uni22[4].text.split (' ')[1]
			print leibiepm2
			# 高校链接
			link2 = 'http://gkcx.eol.cn' + str (uni22[0].find_all ('a')[0].get ('href')).strip ()
			print link2
			# files = open (r'C:\Users\Esri\Desktop\university.txt', 'a+')
			# files.write (
			# 	('%s,%s,%s,%s,%s,%s,%s' % (name2, shengfen2, cengci2, hot2, leibie2, leibiepm2, link2)).encode ('utf-8') + '\n')
	"""

for i in range(64,94):
	try:
		link='http://gkcx.eol.cn/soudaxue/queryschool.html?&page='+str(i)
		get_university(link)
		files=open(r'university.txt','a+')
		files.write(('='*30).encode('utf-8')+'\n')
	except  Exception ,e:
		print e
		continue