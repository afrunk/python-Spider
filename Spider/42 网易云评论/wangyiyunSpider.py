"""
亦是此间少年评论
参考代码：https://blog.csdn.net/weixin_36605200/article/details/82318308

json数据接口，需要两个参数，offset和limit，offset的增量为20，
limit的固定为20刚好和每一页的20条评论相对应，刚好抓取网页评论的20条评论
http://music.163.com/api/v1/resource/comments/R_SO_4_1299557768?offset=40&limit=20
"""
# 网页请求
import requests ##网页请求
import json#格式转换
import csv#数据保存
import time#延时操作
import jieba#分词处理
import numpy#图片的转换
from PIL import Image#图片处理
from wordcloud import WordCloud#词云制作
 
# 获取数据
def get_one_comment(offset):
	# 设置请求头
	headers={
	'Cookie':'_ntes_nuid=c967dbdbd887c2217a4e01569ce1f855; _ntes_nnid=f20c49a8db5414aad483dd704b5baaa4,1563267203812; __oc_uuid=2b48d040-a7a7-11e9-8172-6fedeb22786f; mail_psc_fingerprint=1cf81d9a80bffc88d54167d95971e440; ne_analysis_trace_id=1568786016268; s_n_f_l_n3=05602af691253daa1568786016272; _antanalysis_s_id=1568786016668; vinfo_n_f_l_n3=05602af691253daa.1.0.1568786016271.0.1568786062869; usertrack=ezq0ZV3KS0aQeHqoA9E+Ag==; _ga=GA1.2.1455721911.1573538634; hb_MA-BFF5-63705950A31C_source=www.baidu.com; JSESSIONID-WYYY=rYBS3GsMktXjC1UNYTeEygdvbRCZh5EfePVj3Y%2FIkv8q%2F%5Cy%5Cw3B9Ph5%5CZfx7UzRFGkJktufMzbOSug1g%2BmrAYmbjQRPH3x4I0RZKJa2JHq27ag5O4Z8XgIC7jRxCrog76A2npaxUbBjg%5CtvDAtRSAewQWVW8blOOvJ70M8koC8aS6JQV%3A1575996243067; _iuqxldmzr_=32; WM_TID=Kx3BbLhA0O5FEBUQFRJ98AUxiVkHI%2F8M; WM_NI=V%2FVTy8GP%2BoELH0SuNhAtUtbeEYMRoARpnsOyu70gVtICHflwKh4qYRtUYY4%2BTlLG7JTKfX5HtnM0Yx%2BE6fggAG3K0kaMhrzBH2ZbLh1QjHsz5zbkHiJ0L%2FJbf89bu%2BNlQTE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed3d53aa8eef9ccb570adac8ba7d15f979b8b84ee7fa2eb8e8ded62a9e7a682e82af0fea7c3b92a96f19ab5fc348590e590c8488cf09d96cd6483ac9b95e16f878783b3ee4b92b0a294ce73b7e90088d5808b9d8887ef7d89b8fc92dc5ab88b97bab72198b484a8b6429895aab9b844b8b283d1dc74e99bfa87e66d8399fdacb361a393a893f94a8cee9683cf64f38fa6a9f272f7a6ae8ccb638af084d0c96aa6e8f783f8218eb49fb5c837e2a3; playerid=48052324',
	'Referer':'https://music.163.com/song?id=1299557768',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
	}
	# 字符串拼接
	url='http://music.163.com/api/v1/resource/comments/R_SO_4_1299557768?offset='+str(offset)+'&limit=20'
	try:
		time.sleep(2)
		response=requests.get(url,headers=headers)
		# 状态码判断
		if response.status_code == 200:
			return response.content
	except Exception as e:
		print('出错啦！')
		return None

# 解析数据
def parse_json_data(contents):
	if contents:
		# 编码格式转换
		contents=contents.decode('utf-8')
		# api接口返回的数据是json格式，把json格式转换为字典结构，获取评论信息
		comments=json.loads(contents)['comments']
		for comment in comments:
			content=comment['content']
			nickname=comment['user']['nickname']
			timeArray=time.localtime(comment['time']/1000)
			style_time=time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
			yield{
			'time':style_time,
			'nickname':nickname,
			'comment':content
			}
			# print(nickname+','+content+','+style_time)

# csv保存数据
def save_csv_comments(messages,i):
	# encoding=utf_8_sig只能转换中文乱码和字母乱码，不能支持数字的乱码
	with open('comment_csv.csv','a',encoding='utf_8_sig',newline='')as f:
		csvFile=csv.writer(f)
		if i == 0:
			csvFile.writerow(['评论时间','昵称','评论内容'])
		csvdatas=[]
		for message in messages:
			csvdata=[]
			csvdata.append(message['time'])
			csvdata.append(message['nickname'])
			csvdata.append(message['comment'].replace('\n',''))
			csvdatas.append(csvdata)
		csvFile.writerows(csvdatas)
# 读取csv文件的评论内容的一列
def read_csvFile(fileName):
	with open(fileName,'r') as f:
		# 因为此csv文件并非二进制文件， 只是一个文本文件
		readerCSV=csv.reader(f)
		comment_column=[row[2] for row in readerCSV]
		return comment_column

# 词云生成
def make_word_cloud(text):
	# 先把列表数据转换成字符串，再用jieba来分割字符串
	comment_text=jieba.cut(''.join(text[1:]))
	# list类型转换为str类型
	comment_text=''.join(comment_text)
	# 打开图片并转换为数组形式
	animal=numpy.array(Image.open('timg_meitu_1.jpg'))
	# 指定字体、背景颜色、宽高、词量、指定的背景图
	wc=WordCloud(font_path='C:/Windows/Fonts/simsun.ttc',background_color="white",width=913,height=900, max_words=2000, mask=animal)
	# 生成词云
	wc.generate(comment_text)
	#保存到本地
	wc.to_file("animal.png")

if __name__ == '__main__':
    # offset 就是网易云上的id
    con = get_one_comment(1385646451)
    # print(con)
    parse_json_data(con)