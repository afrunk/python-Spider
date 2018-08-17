#_author=afrunk
#time=2018-8-13
#python3.6

import requests
from lxml import html
from bs4 import BeautifulSoup
import time
import random
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

def get_urls():
	for i in range(1,57):
		url='http://m.yikanxiaoshuo.net/2/2867_'+str(i)+'/'
		print(url)
		res=requests.get(url,headers=headers).text
		sel = html.fromstring(res)
		uls=sel.xpath('//ul[@class="chapter"]/li/a/@href')
		for ul in uls:
			# print(ul)
			get_content(ul)
		rtime=5+float(random.randint(1,100)/20)
		print("we wille sleep %d"%rtime)
		time.sleep(rtime)

def get_content(url):
	with open('极道天魔-1.txt','r+',encoding='utf-8')as f:
		f.read()
		res=requests.get('http://m.yikanxiaoshuo.net/'+url,headers=headers)
		print(res.url)
		res.encoding = res.apparent_encoding
		sel=BeautifulSoup(res.text,'lxml')
		title=sel.find('div','nr_title').text
		contents=sel.find('div',"nr_nr")
		content=contents.find('div').text
		print(title)
		print(content)
		f.write(title)
		f.write(content)
		f.close()


if __name__=='__main__':
	get_urls()
	# get_content('2/2867/2218121.html')

