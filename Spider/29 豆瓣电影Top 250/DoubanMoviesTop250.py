"""
目标网站：https://movie.douban.com/top250?qq-pf-to=pcqq.c2c
问题：
1.添加请求头部之后返回不会得到正确得内容
2.抓取内容得时候碰到第一个元素
"""
import requests
from bs4 import BeautifulSoup

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Cache-Control':'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'bid=P_ZKV9BVHfE; __utmc=30149280; ll="118271"; __utmc=223695111; _vwo_uuid_v2=D5F6301CCA0BA1F403310BBDB612A50A8|a7920ac816b0fa2e758cd41c10b386ce; viewed="4254271"; gr_user_id=c45f1875-a6e0-43d9-aa34-cd019cf81e6b; __utmv=30149280.18622; douban-fav-remind=1; __utmz=30149280.1571395852.15.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1571395855.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1572684498%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=555643563131c871.1564294504.5.1572684498.1571395965.; __utma=30149280.696154547.1563276061.1571395852.1572684498.16; __utma=223695111.56962199.1564294504.1571395855.1572684498.4',
    'Host': 'movie.douban.com',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}

def get_html(url):
    filename ='data.txt' # 文件名
    con = requests.get(url)#requests请求然后获取HTML内容
    con = con.text # 转换成文本
    soup = BeautifulSoup(con,'lxml')#将其转换为Bs4库可以解析的内容
    # print(soup) # 测试是否请求到HTML页面
    titles = soup.find_all('div',class_='hd')#提取标题等内容
    # print(titles)
    pds = soup.find_all('div', class_='bd')[1:] #提取导演国家等内容
    pjias = soup.find_all('p', class_='quote')#提取精选评价

    for title,pd,pjia in zip(titles,pds,pjias): #for循环整个页面内容的列表将标题、导演、评价等内容对应起来进行拼接然后写入txt

        title = title.text.replace('\n','').strip() # 去掉text的回车 空格
        print(title)
        content = pd.text.replace('\n', '').strip()
        print(content)
        pingjia = pjia.text.replace('\n', '').strip()
        print(pingjia)
        data = title+'/'+content+'/'+pingjia
        with open(filename,'a+', encoding='utf-8')  as f:  # 遍历 存入列表
            f.write(data+'\n')

# 拼接请求链接列表
def get_urlList():
    urlList = [] #存储请求链接列表
    for i in range(0,250,25):#每页翻页增加25 然后以此为间隔进行递增
        url='https://movie.douban.com/top250?start={}&filter='.format(i) # 将该链接添加到url中然后将其添加到列表中
        urlList.append(url)
    return urlList #将该列表返回给调用该函数的部分


def main():
    urlList = get_urlList()#调用函数得到请求链接列表
    print(urlList)
    for url in urlList:#遍历链接列表
        get_html(url)#调用该链接然后请求页面

if __name__=='__main__':
    main()#调用主函数运行项目
