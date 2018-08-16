#encoding:utf-8
# Interation 迭代
import requests
from bs4 import BeautifulSoup
import json
import time


def main():
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token':None,
        'X-Requested-With':'XMLHttpRequest'
    }
    for x in range(1,31):
        form_data = {
            'first': 'false',
            'pn': 'x',
            'kd': 'python'
        }

        result = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0',headers=headers,data=form_data)
        json_result= result.json()
        positions = json_result['content']['positionResult']['result']
        print('-'*40)
        print(positions)
        time.sleep(30)

    line = json.dumps(positions, ensure_ascii=False)
    with open('lagou_all.json', 'wb') as fp:
        fp.write(line.encode('UTF-8'))

if __name__ == '__main__':
    main()