"""
参考文章
https://www.cnblogs.com/insane-Mr-Li/p/9092619.html

读取txt的 所有统计的词按照每行一个的形式写入到txt 所有词汇之后写入到列表
然后读取 excle的第三列的表格数据
使用词汇去遍历然后统计词频 然后写入到 csv

操作excle表格

"""

import xlrd

def readExcle():
    # 文件路径
    filename ='workrport.xlsx'
    # 打开该文件
    data = xlrd.open_workbook(filename)
    # 打开第一个sheet
    table = data.sheets()[0]

if __name__ == '__main__':
    readExcle()