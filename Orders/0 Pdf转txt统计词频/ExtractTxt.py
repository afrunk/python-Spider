# -*- coding: UTF-8 -*-
# 是再python2 中使用的 编码规范  再python3中可要可不要的 你再python2中如何不使用这句代码 就会导致中文乱码

"""
1.加载一个指定路径文件夹内的所有pdf文内容
2.解析所有pdf内容并提取指定内容
3.把解析出来的指定内容写入Excel表格
"""

#################
import xlwt  # 写入文件
import xlrd  # 打开excel文件
from xlutils.copy import copy

import os
import re
import sys
import importlib

importlib.reload(sys)
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

import logging

logging.basicConfig(level=logging.ERROR)

# 读取一个文件夹目录下所有PDF文档路径,返回所有PDF文件的绝对路径
# G:\需求文档\202 pdf转txt统计关键词个数\台湾光复初期赴台的福州人群体研究_刘凌斌.pdf   绝对路径
# 台湾光复初期赴台的福州人群体研究_刘凌斌.pdf 路径
def loadPDF(file_path, stock_num_list=None):
    pdf_files = {}  # 保存文件地址和名称：name：path
    # python 的字典形式 就是一种数据类型
    files = os.listdir(file_path)
    # os 是一个操作系统的包 你可以调用各种有关操作系统的方法 比如新建一个文件或者一个文件夹 或者读取某个目录下的所有文件名
    # 使用os.listdir方法 后面的（参数）  是我们要读取的文件路径
    for file in files:
        if os.path.splitext(file)[1] == '.pdf':  # 判断是否为PDF文件
            # print(os.path.splitext(file)[1])
            if stock_num_list is None or (stock_num_list is not None and file[0:6] in stock_num_list):
                abso_Path = os.path.join(file_path, file)
                # os的方法调用拼接绝对路径
                stock_num = file[0:6]
                # print(stock_num)
                pdf_files[file] = (stock_num, abso_Path)
                # 拼接成功后存入到列表 然后我们需要读取整个列表里面的所有pdf的绝对路径
    # print(pdf_files)
    return pdf_files

# 解析PDF文件，转为txt格式
def parsePDF(PDF_path, TXT_path):
    with open(PDF_path, 'rb')as fp:  # 以二进制读模式打开
        praser = PDFParser(fp)  # 用文件对象来创建一个pdf文档分析器
        doc = PDFDocument()  # 创建一个PDF文档
        praser.set_document(doc)  # 连接分析器与文档对象
        doc.set_parser(praser)

        # 提供初始化密码
        # 如果没有密码 就创建一个空的字符串
        doc.initialize()

        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            rsrcmgr = PDFResourceManager()  # 创建PDf 资源管理器 来管理共享资源
            laparams = LAParams()  # 创建一个PDF设备对象
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)  # 创建一个PDF解释器对象

            # 循环遍历列表，每次处理一个page的内容
            for page in doc.get_pages():  # doc.get_pages() 获取page列表
                try:
                    interpreter.process_page(page)
                    layout = device.get_result()  # 接受该页面的LTPage对象
                    # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                    for x in layout:
                        if isinstance(x, LTTextBoxHorizontal):
                            with open(TXT_path, 'a', encoding='UTF-8', errors='ignore') as f:
                                results = x.get_text()
                                # print(results)
                                f.write(results + '\n')
                except:
                    pass

# 加载目标股票代码
def getStackNum(excel_path):
    book = xlrd.open_workbook(excel_path)  # 打开一个wordbook
    sheet_ori = book.sheet_by_name('Sheet1')
    print(sheet_ori.col_values(0, 0, sheet_ori.nrows)) # 返回第一个名称
    return sheet_ori.col_values(0, 0, sheet_ori.nrows)

# 从Excel中加载关键词
def loadKeyWords(excel_path):
    book = xlrd.open_workbook(excel_path)  # 打开一个wordbook
    sheet_ori = book.sheet_by_name('Sheet1')
    print(sheet_ori.row_values(0, 1, sheet_ori.ncols)) # 返回1-3的关键字
    return sheet_ori.row_values(0, 1, sheet_ori.ncols)

# 加载txt列表寻找关键词并保存到excel
def matchKeyWords(txt_folder, excel_path, keyWords, year):
    files = os.listdir(txt_folder)
    words_num = []  # 保存所有文件词频
    for file in files:
        word_freq = {}  # 单词出现频率次：word：num
        if os.path.splitext(file)[-1] == ".txt":
            txt_path = os.path.join(txt_folder, file)
            with open(txt_path, "r", encoding='utf-8', errors='ignore')as fp:
                text = fp.readlines()
                for word in keyWords:
                    num = 0
                    for line in text:
                        num += line.count(word)
                    word_freq[word] = num
                stock_num = file[0:6]
                pdf_name = file.split(".")[0] + "." + file.split(".")[1]
                words_num.append((word_freq, stock_num, pdf_name))
    # 保存到Excel
    book = xlrd.open_workbook(excel_path)  # 打开一个wordbook
    copy_book = copy(book)
    sheet_copy = copy_book.get_sheet("Sheet1")
    for index, one in enumerate(words_num):
        word_f = one[0]
        stock_num = one[1]
        pdf_name = one[2]
        for ind, word in enumerate(keyWords):
            sheet_copy.write(index + 1, ind + 1, str(word_f[word]))
        # sheet_copy.write(index + 1, 0, year)
        # sheet_copy.write(index + 1, 1, stock_num)
        sheet_copy.write(index + 1, 0, pdf_name)
    copy_book.save(excel_path +"."+year + ".xls")


if __name__=='__main__':
    pathLists = loadPDF('G:\\需求文档\\202 pdf转txt统计关键词个数')


    for pathlist in pathLists:
        print(pathlist)
        pdf_to_txt_path = pathlist + ".txt"  # txt路径

        print(pdf_to_txt_path)
        parsePDF(pathlist,pdf_to_txt_path)

    keyWords = loadKeyWords('G:\\需求文档\\202 pdf转txt统计关键词个数\\Sheet1.XLS') # 关键词
    year = '1'
    matchKeyWords('G:\需求文档\\202 pdf转txt统计关键词个数','G:\需求文档\\202 pdf转txt统计关键词个数\Sheet1.XLS', keyWords, year)



"""
操作步骤：
- 打开代码文件，右键 Run - ExtractTxt.py 在下面弹出的对话框中会有pdf转txt的输出提示 ，这就证明正在运行
- 
"""