"""
urls 列表进行简化 完成  简化
不要重复下载 完成        你之前说的是不需要重复下载把 你现在又给我一个你们老师得文件  你看看你们老师得文件 和我得有什么区别
将重复的封装成函数  完成
将图片运行出来
"""

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# 构建请求链接列表的函数
def structureUrls():
        urls = []
        for i in range(1,49):
                url_1 = 'https://www.ncdc.noaa.gov/cag/statewide/time-series/1-tavg-{}-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'.format(i)
                url_2 = 'https://www.ncdc.noaa.gov/cag/statewide/time-series/1-tavg-{}-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'.format(i)
                urls.append(url_1)
                urls.append(url_2)
        return urls

# 请求内容得函数
def getContent(urls):
        for url in urls:
                response = requests.get(url)
                state, measure, month = response.text.split('\n')[0].split(', ')
                with open(os.path.join(r'weather', state + '_' + month + '.csv'), 'w') as ofile:
                        ofile.write(response.text)

# 绘制图片得函数
def draw(df):


        # plot 1
        df['Year'] = df['Date'].map(lambda d: d.year)
        df['Jan-Aug Delta'] = df.groupby(['State', 'Year'])['Value'].diff()
        df_delta = df.dropna(subset=['Jan-Aug Delta'])[['State', 'Year', 'Jan-Aug Delta']]

        fig, ax = plt.subplots(4, 1)
        il = df_delta[df_delta['State'] == 'Illinois']
        ax[0].plot(il['Year'], il['Jan-Aug Delta'], 'k-')
        ax[0].set_ylabel('Illinois')
        ax[0].xaxis.tick_top()

        ca = df_delta[df_delta['State'] == 'Illinois']
        ax[1].plot(ca['Year'], ca['Jan-Aug Delta'], 'r-')
        ax[1].set_ylabel('California')
        ax[1].set_label('')
        ax[1].set_xticks([])
        ax[1].xaxis.set_ticks_position('none')

        ny = df_delta[df_delta['State'] == 'New York']
        ax[2].plot(ny['Year'], ny['Jan-Aug Delta'], 'b-')
        ax[2].set_ylabel('New York')
        ax[2].set_label('')
        ax[2].set_xticks([])
        ax[2].xaxis.set_ticks_position('none')

        tx = df_delta[df_delta['State'] == 'Texas']
        ax[3].plot(tx['Year'], tx['Jan-Aug Delta'], 'g-')
        ax[3].set_ylabel('Texas')

        plt.suptitle('Average Jan-Aug Temperature Variation')
        plt.savefig(r'weather\Jan_Aug_Temp_Delta.png')
        plt.show()

def drawPlot2(df):
        # plot 2
        df['Month'] = df['Date'].map(lambda d: d.month)
        df_aug = df[df['Month'] == 8]

        fig, ax = plt.subplots(1, 1)
        il = df_aug[df_aug['State'] == 'Illinois']
        ca = df_aug[df_aug['State'] == 'California']
        ny = df_aug[df_aug['State'] == 'New York']
        tx = df_aug[df_aug['State'] == 'Texas']

        print('Max/Mean/Min for Illinois:', il['Value'].max(), il['Value'].mean(), il['Value'].min())
        print('Max/Mean/Min for California:', ca['Value'].max(), ca['Value'].mean(), ca['Value'].min())
        print('Max/Mean/Min for New York:', ny['Value'].max(), ny['Value'].mean(), ny['Value'].min())
        print('Max/Mean/Min for Texas:', tx['Value'].max(), tx['Value'].mean(), tx['Value'].min())

        ax.plot(il['Year'], il['Value'], 'k-', label='Illinois')
        ax.plot(ca['Year'], ca['Value'], 'r-', label='California')
        ax.plot(ny['Year'], ny['Value'], 'b-', label='New York')
        ax.plot(tx['Year'], tx['Value'], 'g-', label='Texas')

        ax.legend(loc='upper right')
        plt.suptitle('Average August Temperature')
        plt.savefig(r'weather\Aug_Temp.png')
        plt.show()


# 主函数
if __name__=='__main__':
        urls = structureUrls()
        # getContent(urls, states) # 注释掉 ok?

        weather_data = os.listdir(r'weather')
        dfs = []
        for f in weather_data:
                print(f)
                st, month = f.split('_')
                df = pd.read_csv(os.path.join(r'weather', f), skiprows=4)
                df['State'] = st
                df['Date'] = pd.to_datetime(df['Date'], format='%Y%m')
                dfs.append(df)

        df = pd.concat(dfs)
        df = df.sort_values(['State', 'Date'])
        draw(df)
        drawPlot2(df)