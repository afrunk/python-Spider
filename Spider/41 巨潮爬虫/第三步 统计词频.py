"""
参考文章
https://www.cnblogs.com/insane-Mr-Li/p/9092619.html

读取txt的 所有统计的词按照每行一个的形式写入到txt 所有词汇之后写入到列表
然后读取 excle的第三列的表格数据
使用词汇去遍历然后统计词频 然后写入到 csv

操作excle表格

使用方法：
将你的xlsx的路径进行修改 然后修改 keywords里面的关键词即可 每行一个

"""

import xlrd
import jieba
import jieba.analyse
import csv


# 读取关键词文本 返回列表
def getKeyWords():
    # 读取关键词文本
    filename='keywords.txt'
    with open(filename,encoding='utf-8')  as f: # 遍历 存入列表
        txt_list=[content.rsplit() for content in f ]
    #   # print(txt_list[0])
    # 返回列表
    return txt_list

# 主函数
if __name__ == '__main__':

    # 打开读取文件名为threekingdoms.txt的三国演义文档
    txt = open('G:\\finalpage\\2010.TXT', 'r', encoding='utf-8').read()
    # 读取txt
    keywordlist = getKeyWords()
    # 读取关键词得列表，来获取字典里所匹配到得值
    for i in keywordlist:
        #  使用结巴分词对文本进行分词，cut_all 开启 否则会导致缺失
        seg_list = jieba.lcut(txt,cut_all=True)
        # 构建字典为后续存储做准备
        counts = {}
        # 遍历分词列表 进行统计
        for word in seg_list:
            # print(word)
            counts[word] = counts.get(word, 0) + 1

        # 赋值
        dict_items =counts.items()
        # print(dict_items)

        keyWord ={}
        # 赋值给字典
        for (k,v) in dict_items:
            # print(k,v)
            keyWord[k]=v
        print(i[0])
        # 判断所要查询的关键词是否在
        if (i[0] in keyWord):
            print(keyWord[i[0]])
            # 追加写入到csv
            file = open("test.csv",'a+')
            reader = csv.reader(file)
            original = list(reader)
            file1 = open("test.csv", "a+", newline="")
            content = csv.writer(file1)
            for row in original:
                content.writerow(row)
            content.writerow([i[0], keyWord[i[0]]])
            file.close()
            file1.close()
        else:
            file = open("test.csv", 'a+')
            reader = csv.reader(file)
            original = list(reader)
            file1 = open("test.csv", "a+", newline="")
            content = csv.writer(file1)
            for row in original:
                content.writerow(row)
            content.writerow([i[0], 0])
            file.close()
            file1.close()


