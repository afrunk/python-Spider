#time:2018-7-25 10:42
#_author:afrunk
#python36 requests
import requests
import json
import io
import time
import random
#获取html
def get_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None
#提取json文件
def parse_page(html):
    data=json.loads(html)['cmts']
    for item in data:
        yield{
            'comment':item['content'],#评论
            'data':item['time'],#时间
            'rate':item['score'],#评分
            'city':item['cityName'],#城市
            'nickName':item['nickName']#昵称
        }
#保存数据
def save_to_txt():
    for i in range(301,400):
        url='http://m.maoyan.com/mmdb/comments/movie/1200486.json?_v_=yes&offset='+str(i)
        html=get_page(url)
        print("正在保存第%d页"%i)
        for item in parse_page(html):
            with io.open('yaoshen301-400.txt','a',encoding='utf-8')as f:
                f.write(item['data']+','+item['nickName']+','+item['city']+','+str(item['rate'])+','+item['comment']+'\n')
        time.sleep(5+float(random.randint(1,100))/20)

if __name__=='__main__':
    save_to_txt()