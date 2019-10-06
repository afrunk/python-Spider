# https://api.bilibili.com/x/v1/dm/list.so?oid=115528948
'''
author:afrunk
time:9/11/2019
方法：
- 首先寻找到弹幕得xml文件链接:检查-ctrl f 输入 oid即可查到链接 右键转入查看到存放评论得xml文件
- 爬取xml文件并使用xpath匹配 然后拼接字符串 结巴分词 然后词云

参考链接：
- https://blog.csdn.net/weixin_36605200/article/details/82848020 简单的完成了该完成的任务 针对某一个视频
- https://www.write-bug.com/article/1959.html  进化体 针对某一系列视频
- https://www.jianshu.com/p/f628679883e3 抓取大量的数据存入数据库 分析b站视频的弹幕数量逐年增长速度
- https://www.jianshu.com/p/c52efef63518 上面那篇文章的进化版 实现了情感分析等效果
'''
import time #延时操作
import requests#网页请求
import jieba#分析请求
import numpy as np
from wordcloud import WordCloud as wc #词云制作
from lxml import etree

headers ={
    'Host': 'api.bilibili.com',
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Cookie': 'finger=edc6ecda; LIVE_BUVID=AUTO1415378023816310; stardustvideo=1; CURRENT_FNVAL=8; buvid3=0D8F3D74-987D-442D-99CF-42BC9A967709149017infoc; rpdid=olwimklsiidoskmqwipww; fts=1537803390'

}
# 获取信息
def get_page(url):
    try:
        # 延时操作，防止太快爬取
        time.sleep(0.5)
        response = requests.get(url,headers=headers)
    except Exception as e:
        print("获取xml内容失败，%s" %e)
    else:
        if response.status_code == 200:
            # 下载xml文件
            with open('bilibili.xml','wb') as f:
                f.write(response.content)
            return True
        else:
            return False
#解析网页
def param_page(url):
    time.sleep(1)
    get_page=1
    # if get_page(url):
    if get_page:
        # 文件路径 html解析器
        html = etree.parse('bilibili.xml',etree.HTMLParser())
        # xpath 解析 获取当前所有的d标签下的所有文本内容
        results = html.xpath('//d//text()')
        print(results)
        return results

# 弹幕去中重 重复计算和词云的制作
def remove_double_barrage(url):
    '''
    double_arrage:所有重复弹幕的集合
    results:去重后的弹幕
    barrage:每种弹幕内容都存储一遍
    '''
    results = param_page(url)
    double_barrage = []
    results_new = []
    barrages = set()
    for result in results:
        if result  not in results_new:
            results_new.append(result)
        else:
            double_barrage.append(result)
            barrages.add(result)
    # print(barrage)
    # 重复计数 结果写入txt文件
    with open('barrages.txt','w',encoding='utf-8')as f:
        for barrage in barrages:
            # 数量的统计
            amount = double_barrage.count(barrage)
            f.write(barrage+':'+str(amount+1)+'\n')
    # 设置停用词
    stop_words =['【','】',',','.','?','!','。']
    words = []
    if results_new:
        for result in results_new:
            for stop in stop_words:
                # 去除上面的停用词再拼接成字符串
                result =''.join(result.split(stop))
            words.append(result)
        # 列表拼接成字符串
        words=''.join(words)
        words=jieba.cut(words)
        words=''.join(words)
        w = wc(font_path='‪C:/Windows/Fonts/SIMYOU.TTF', background_color='white', width=1600, height=1600,max_words=2000)
        w.generate(words)
        w.to_file('wordcloud.jpg')

# 读取txt文件 然后绘制柱状图
from matplotlib import pyplot as plt

def draw_bar_graph():
    x=[]
    y=[]
    file_obj = open('barrages.txt','r',encoding='utf-8')
    all_lines=file_obj.readlines()
    for line in all_lines:
        xylist = line.strip('\n').split(':')
        x.append(xylist[0])
        y.append(xylist[1])
    # print(x)
    # print(y)
    file_obj.close()

    plt.bar(x,y,color='g',align ='center')
    plt.title('Bar graph')
    plt.ylabel('弹幕')
    plt.xlabel('弹幕数')
    # plt.show()
    plt.savefig('G:\\Python_Data\\ComputerDesig\\b站弹幕爬虫可视化\\data.png') # 保存


if __name__ =='__main__':

    url='https://api.bilibili.com/x/v1/dm/list.so?oid=115528948'
    # 第一步调用获取弹幕存入到xml文件种
    # param_page(url)

    # 第二步 去重 画图 统计
    # remove_double_barrage(url)

    # 绘制柱状图
    draw_bar_graph()
