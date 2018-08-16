import requests
import re
def getHTMLText (url):
	try:
		r = requests.get (url, timeout=30)
		r.raise_for_status ()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePage (ilt, html):
	try:
		plt = re.findall (r'\"view_price\"\:\"[\d\.]*\"', html)
		# 首先引入了一个双引号 然后来获取这个价格
		tlt = re.findall (r'\"raw_title\"\:\".*?\"', html)
		# .*?最小匹配
		for i in range (len (plt)):
			price = eval (plt[i].split (':')[1])
			title = eval (tlt[i].split (':')[1])
			ilt.append ([price, title])
	except:
		print ("")

def printGoodsList (ilt):
	tplt = "{:4}\t{:8}\t{:16}"	#给出的输出的格式分别为长度为4 长度为8 和长度为16
	print (tplt.format ("序号", "价格", "商品名称"))
	count = 0			#count表明商品的序号 g表示的是ilt的顺序输出
	for g in ilt:
		count = count + 1
		print (tplt.format (count, g[0], g[1]))

# 	try except 提高了代码的鲁棒性 使得程序的运行更加的稳定和有效
def main ():
	goods = '书包'
	depth = 4					#爬取的页数
	start_url = 'http://s.taobao.com/search?q=' + goods
	infoList = []
	for i in range (depth):
		try:
			url = start_url + '&s=' + str (44 * i)
			html = getHTMLText (url)
			parsePage (infoList, html)
		except:
			continue
	printGoodsList (infoList)

main ()

