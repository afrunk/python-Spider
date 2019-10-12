"""
目标链接：http://10.2.3.67/moodle/course/view.php?id=995

"""
headers ={

		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Cookie': 'MoodleSession=uici0mebgkbo8v5qbbs0ddpa76; MOODLEID1_=%25FC%25A3%2513%25D6%25CA%2505%25C0%2513%25EC%25D4%2596%2514Z%250A%25BD'

}

import requests
from bs4 import BeautifulSoup
# 获取测试题链接
def getIndex():
    headers = {

        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'MoodleSession=uici0mebgkbo8v5qbbs0ddpa76; MOODLEID1_=%25FC%25A3%2513%25D6%25CA%2505%25C0%2513%25EC%25D4%2596%2514Z%250A%25BD'

    }
    url ='http://10.2.3.67/moodle/course/view.php?id=995'
    con = requests.get(url,headers=headers).text
    print(con)

# 获取测试题内容
def getPrograms():
    headers = {
        'Host': '10.2.3.67',
        'Referer': 'http: // 10.2.3.67 / moodle / mod / quiz / attempt.php?attempt = 323112',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'MoodleSession=uici0mebgkbo8v5qbbs0ddpa76; MOODLEID1_=%25FC%25A3%2513%25D6%25CA%2505%25C0%2513%25EC%25D4%2596%2514Z%250A%25BD'

    }
    url='http://10.2.3.67/moodle/mod/quiz/attempt.php?attempt=323112'
    con = requests.get(url, headers=headers).text
    # print(con)
    soup =BeautifulSoup(con,'lxml')
    questions= soup.find_all('div',class_='formulation clearfix')
    # print(questions)
    with open('1.txt', 'a+', encoding='utf-8') as f:  # a+才可追加 不知为何
        for i in range(len(questions)):
            img = questions[i].find('img').get('src')
            print(img)
            print(questions[i].text, '\n')
            f.write(questions[i].text+'\n')
    f.close()



if __name__=='__main__':
    # 获取首页测试题链接函数
    # getIndex()
    getPrograms()