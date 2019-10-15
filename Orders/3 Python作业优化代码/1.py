"""
urls 列表进行简化
不要重复下载
将重复的封装成函数
将图片运行出来
"""

import os
import us
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

urls = ['https://www.ncdc.noaa.gov/cag/statewide/time-series/1-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/1-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/2-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/2-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/3-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/3-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/4-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/4-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/5-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/5-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/6-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/6-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/7-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/7-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/8-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/8-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/9-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/9-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/10-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/10-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/11-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/11-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/12-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/12-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/13-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/13-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/14-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/14-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/15-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/15-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/16-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/16-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/17-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/17-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/18-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/18-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/19-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/19-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/20-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/20-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/21-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/21-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/22-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/22-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/23-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/23-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/24-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/24-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/25-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/25-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/26-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/26-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/27-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/27-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/28-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/28-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/29-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/29-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/30-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/30-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/31-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/31-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/32-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/32-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/33-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/33-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/34-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/34-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/35-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/35-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/36-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/36-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/37-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/37-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/38-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/38-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/39-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/39-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/40-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/40-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/41-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/41-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/42-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/42-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/43-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/43-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/44-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/44-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/45-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/45-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/46-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/46-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/47-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/47-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/48-tavg-1-1-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        'https://www.ncdc.noaa.gov/cag/statewide/time-series/48-tavg-1-8-1895-2019.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000']

for url in urls:
    response = requests.get(url)

    state, measure, month = response.text.split('\n')[0].split(', ')

    with open(os.path.join(r'weather', state+'_'+month+'.csv'), 'w') as ofile:
        ofile.write(response.text)

weather_data = os.listdir(r'weather')

dfs = []
for f in weather_data:
    st, month = f.split('_')
    df = pd.read_csv(os.path.join(r'weather', f), skiprows=4)
    df['State'] = st
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m')
    dfs.append(df)

df = pd.concat(dfs)
df = df.sort_values(['State', 'Date'])

#plot 1
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

#plot 2
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
