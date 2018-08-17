import xlrd
import os
import requests
import time
import random

folder_path='./Photo'

def read_excle():
    if os.path.exists(folder_path)==False:
        os.makedirs(folder_path)
    workbook=xlrd.open_workbook(r'郭源潮.xls')
    sheet=workbook.sheet_by_index(0)
    cols=sheet.col_values(3)
    for i in range(6890,65535):
        # print(cols[i])
        print("第%d张图片下载完成"%i)
        html=requests.get(cols[i])
        file_name='photo\\'+str(i)+'.jpg'
        f=open(file_name,'wb')
        f.write(html.content)
        f.close()
    rtime=3+float(random.randint(1,100))/20
    time.sleep(rtime)


if __name__=='__main__':
    read_excle()