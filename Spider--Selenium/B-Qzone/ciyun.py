#coding:utf-8
"""
使用结巴分词生成词云图

"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

def create_word_cloud(filename):
    text=open("{}.txt".format(filename)).read()
    #结巴分词
    wordlist=jieba.cut(text,cut_all=True)
    wl=" ".join(wordlist)

    #设置词云
    wc=WordCloud(
        #设置背景颜色
        background_color="white",
        #设置最大显示的词云数
        max_words=2000,
        #设置一种电脑的字体
        font_path="C:\Windows\Fonts\simfang.ttf",
        height=1200,
        width=600,
        #设置这种字体最大值
        max_font_size=100,
        #设置有多少种随机生产状态，即多少配色方案
        random_state=30,
    )
    myword=wc.generate(wl)
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file("py_book.png")#保存下来
if __name__=='__main__':
    create_word_cloud('qq_word-陈佳音')