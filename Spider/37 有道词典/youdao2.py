import requests
from bs4  import BeautifulSoup
url = 'http://www.youdao.com/w/data/'
con = requests.get(url).text
# print(con)
soup = BeautifulSoup(con,'lxml')
content = soup.find('div',id='transformToggle')
# print(content)
divs = content.find_all('div')
# 词组短语
duanyuList = []
ps = divs[0].find_all('p')
print("===词组短语===")
for p in ps:
    list = p.text.split()
    cizuduanyu = list[0]+list[1]+list[2]
    # print(cizuduanyu)
    duanyuList.append(cizuduanyu)
print(duanyuList)

try:
    print("===同义词===")
    nextdivs = content.find_all('div',class_='trans-container tab-content hide')
    # print(nextdivs[0])
    # 同义词
    tongyicilist = []
    ul = nextdivs[0].find('ul')
    pls = ul.find_all('p')
    lis = ul.find_all('li')
    for i,j in zip(pls,lis):
        tongyici = i.text.replace('\n','')+j.text.strip()
        # print(tongyici)
        tongyicilist.append(tongyici)
    print(tongyicilist)
except:
    pass
# 同根词
print("\n===同根词===")
tongbuci = []
ps = nextdivs[1].find_all('p')
for p in ps :
    tonggenci = p.text.replace('\n','')
    # print(tonggenci)
    tongbuci.append(tonggenci)
print(tongbuci)

# 词语辨析
print("\n===词语辨析===")
ciyubianxi = [] #词语辨析列表
divs_1 = nextdivs[2].find_all('div')
for p in divs_1 :
    tonggenci = p.text.replace('\n','')
    # print(tonggenci)
    ciyubianxi.append(tonggenci)
print(ciyubianxi)