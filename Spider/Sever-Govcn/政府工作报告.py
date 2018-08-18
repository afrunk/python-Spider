import requests
from bs4 import BeautifulSoup
import jieba
import jieba.analyse
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
#获取文本内容
def get_content(url):
    list=''
    content=requests.get(url)
    content.encoding=content.apparent_encoding
    html=BeautifulSoup(content.text,'lxml')
    div=html.find('div','article oneColumn pub_border')
    title=div.find('h1').text

    page=div.find('div','pages_content').text
    # print(title)
    # with open('2016国家工作报告.txt','a',encoding='utf-8')as f:
    #     f.write(title+'\n')
    #     f.write(page)
    #     f.close()
    # print(page)

    return page

#对文本内容进行清洗和分词
def word_frequnency(text):
    words=[word for word in jieba.cut(text,cut_all=True) if len(word)>=2]
    # 要求词超过2的才可以通过分词
    # print(words)
    exclude_words=[
        "中国","推进","全面","提高","工作","坚持","推动",
        "支持", "促进", "实施", "加快", "增加", "实现",
        "基本", "重大", "我国", "我们", "扩大", "继续",
        "以上", "取得", "地方", "今年", "加大", "优化",
    ]
    for word in words:
        if word in exclude_words:
            words.remove(word)
    c = Counter(words)
    for word_freq in c.most_common(20):
        word,freq=word_freq
        print(word,freq)
    exclude_words_file = '停用词.txt'
    jieba.analyse.set_stop_words(exclude_words_file)
    #获取关键词频率
    tags=jieba.analyse.extract_tags(text,topK=100,withWeight=True)
    for tag in tags:
        print(tag)
#对文本进行词云生成可视化输出
def word_cloud(filename):
    text = open("{}.txt".format(filename)).read()
    # 结巴分词
    wordlist = jieba.cut(text, cut_all=True)
    wl = " ".join(wordlist)

    # 设置词云
    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
        # 设置最大显示的词云数
        max_words=2000,
        # 设置一种电脑的字体
        font_path="C:\Windows\Fonts\simfang.ttf",
        height=1200,
        width=600,
        # 设置这种字体最大值
        max_font_size=100,
        # 设置有多少种随机生产状态，即多少配色方案
        random_state=30,
    )
    myword = wc.generate(wl)
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file("py_book.png")  # 保存下来

if __name__=='__main__':
    word_cloud('2016国家工作报告')
    # url='http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'
    # 使用正则替换符号和数字
    # re.sub实现正则的替换
    # pattern = re.compile('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？“”、~@#￥%……&*（）(\d+)]+')
    # result = pattern.sub("", get_content(url))
    # word_frequnency(result)
