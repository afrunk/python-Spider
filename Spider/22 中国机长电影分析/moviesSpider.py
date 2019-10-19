"""
没有难点
获取猫眼电影的评论的方法
http://m.maoyan.com/mmdb/comments/movie/1230121.json?_v_=yes&offset=

将这里面的数字串修改为猫眼电影里某个电影的字符串 即可获取
"""




import requests
import time
import random
import json

#获取每一页数据
def get_one_page(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'm.maoyan.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    response = requests.get(url=url,headers=headers)
    # response.encoding = response.apparent_encoding  # 避免乱码
    if response.status_code == 200:
        return response.text
    return None

#解析每一页数据
def parse_one_page(html):

    data = json.loads(html)['cmts']#获取评论内容
    for item in data:
        yield{
        'date':item['time'].split(' ')[0],
        'nickname':item['nickName'],
        'city':item['cityName'],
        'rate':item['score'],
        'conment':item['content']
        }


#保存到文本文档中
def save_to_txt():


    for i in range(1,100):

        print("开始保存第%d页" % i)
        url = 'http://m.maoyan.com/mmdb/comments/movie/1230121.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        # print(html)
        for item in parse_one_page(html):
            print(item)
            with open('中国机长.txt','a',encoding='utf-8') as f:
                f.write(item['date'] + ','+item['nickname'] +','+item['city'] +','
                    +str(item['rate']) +',' +item['conment']+'\n')
                #time.sleep(random.randint(1,100)/20)
                time.sleep(2)

#去重重复的评论内容
def delete_repeat(old,new):
    oldfile = open(old,'r',encoding='utf-8')
    newfile = open(new,'w',encoding='utf-8')
    content_list = oldfile.readlines() #获取所有评论数据集
    content_alread = [] #存储去重后的评论数据集

    for line in content_list:
        if line not in content_alread:
            newfile.write(line+'\n')
            content_alread.append(line)

if __name__ == '__main__':
    # save_to_txt()
    delete_repeat(r'中国机长.txt',r'中国机长_new.txt')