import requests
import re
import csv

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

}
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=113298088'

response = requests.get(url,headers=headers)

html_doc = response.content.decode('utf-8')
format = re.compile('<d p="(.*?)">(.*?)</d>')
danmu = format.findall(html_doc)
# print(danmu)
for i in danmu:
    with open('danmu.csv','a',newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        danmu = []
        # print(i)
        iList = str(i).split(',')
        # print(iList)
        for j in iList:
            j=j.replace('(\'','').replace('\'','').replace(')','')
            danmu.append(j)
        # print(danmu)
        # break
        writer.writerow(danmu)
