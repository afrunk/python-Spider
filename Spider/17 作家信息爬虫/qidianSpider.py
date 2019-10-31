import requests
from bs4 import BeautifulSoup
url = 'https://my.qidian.com/author/4362305'
con = requests.get(url).text
# print(con)
soup = BeautifulSoup(con,'lxml')
# 作家名
name = soup.find('h3').text
print(name)

# 全部作品
div = soup.find('ul',class_='author-work')
lis = div.find_all('li',class_='author-item')
for li in lis:
    print(li.text)