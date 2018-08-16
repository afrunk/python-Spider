#-*-coding:utf-8-*-
# __author__='afrunk'
# chromedriver||selenium
from bs4 import BeautifulSoup
from selenium import webdriver

def get_zhuanye(url):
	print url
	driver=webdriver.Chrome(executable_path='C:\Users\Administrator.USER-20161101EP\AppData\Local\Google\Chrome\Application\chromedriver.exe')
	driver.get(url)
	data=driver.page_source
	driver.close()
	content=BeautifulSoup(data,'lxml')
	
	zhuanye=content.find_all('tbody','lin-seachtable')[0].find_all('tr')
	# print zhuanye
	for zy in zhuanye:
		# print zy
		zyin = zy.find_all ('td')
		# 学校名称
		name = zyin[0].find_all ('a')[0].get ('title')
		# 专业名称
		zhuanyename = zyin[1].text
		# 是否重点专业
		vip = zyin[2].text
		# 院校属性
		if zyin[3].get ('style'):
			shuxing = '非教育部直属'.decode ('utf8')
		else:
			shuxing = zyin[3].text
		# 985大学
		if zyin[4].get ('style'):
			a985 = '非985大学'.decode ('utf8')
		else:
			a985 = zyin[4].text
		# 211大学
		if zyin[5].get ('style'):
			a211 = '非211大学'.decode ('utf8')
		else:
			a211 = zyin[5].text
		unilink = str (zyin[1].find_all ('a')[0].get ('href'))
		print name, zhuanyename,vip,shuxing, a985, a211,unilink
		files = open (r'zhuanye.txt', 'a+')
		files.write (('%s,%s,%s,%s,%s,%s,%s' % (name, zhuanyename, vip, shuxing, a985, a211, unilink)).encode ('utf8') + '\n')


for i in range(1,23):#23
	try:
		link='http://gkcx.eol.cn/soudaxue/querySchoolSpecialty.html?&argspecialtyname=%E7%89%A9%E8%81%94%E7%BD%91&argzycengci=\u4e13\u79d1&page='+str(i)
		get_zhuanye(link)
	except Exception,e:
		print e