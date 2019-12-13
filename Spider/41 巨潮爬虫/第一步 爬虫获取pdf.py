import requests
import json
import os

"""

http://static.cninfo.com.cn/finalpage/2010-01-27/57551093.PDF

"""
# 获取pdf的链接返回给之后的请求函数
def getPdfUrl():
    pdfUrlList = []
    for j in range(1,16):
        url = 'http://www.cninfo.com.cn/new/fulltextSearch/full?searchkey=%E9%87%91%E4%BA%9A%E7%A7%91%E6%8A%80&sdate=2010-01-01&edate=2010-12-31&isfulltext=false&sortName=pubdate&sortType=asc&pageNum={}'.format(j)
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
            'Connection': 'keep-alive',
            'Cookie': 'noticeTabClicks=%7B%22szse%22%3A2%2C%22sse%22%3A0%2C%22hot%22%3A0%2C%22myNotice%22%3A0%7D; tradeTabClicks=%7B%22financing%20%22%3A0%2C%22restricted%20%22%3A0%2C%22blocktrade%22%3A0%2C%22myMarket%22%3A0%2C%22financing%22%3A1%7D; JSESSIONID=5FB98CEA7C049F379C51101A47248900; insert_cookie=37836164; UC-JSESSIONID=C5B682F39F87AC52D964048F20257D9E; _sp_ses.2141=*; cninfo_search_record_cookie=%E9%87%91%E4%BA%9A%E7%A7%91%E6%8A%80; _sp_id.2141=bf2fee56-ed7e-4a11-be9c-109bea97fd60.1571490547.3.1575716773.1572530687.085e8434-be90-4ac3-849b-2e85ffc0c087',
            'Host': 'www.cninfo.com.cn',
            'Referer': 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=%E9%87%91%E4%BA%9A%E7%A7%91%E6%8A%80',
            'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
            'X-Requested-With': 'XMLHttpRequest'
        }
        con = requests.get(url,headers=headers).json()


        for i in con['announcements']:
            pdfUrl = 'http://static.cninfo.com.cn/'+i['adjunctUrl']
            pdfUrlList.append(pdfUrl)
        # print(pdfUrlList)
        # print(con['announcements'][0]['adjunctUrl'])
    return pdfUrlList

# 将之前请求到的pdfurl链接逐个遍历保存到本地
def reqPdf():
    pdfUrlList = getPdfUrl()
    print(pdfUrlList)
    for requests_pdf_url in pdfUrlList:
        # python requests 的pdf 文档
        r = requests.get(requests_pdf_url)
        # print(r.text)
        filename=requests_pdf_url.replace('http://static.cninfo.com.cn/','')[-12:]
        # print(filename)
        path = requests_pdf_url.replace('http://static.cninfo.com.cn/','')[:21]
        path = path.replace('/','\\')[:-1]
        pathfilename = 'G:'+'\\'+path
        print(pathfilename)
        filename =pathfilename+'\\'+filename
        print(filename)
        if not os.path.exists(pathfilename):
            os.mkdir(pathfilename)
        with open(filename, 'wb+') as f:
            f.write(r.content)


if __name__ == '__main__':
    reqPdf()