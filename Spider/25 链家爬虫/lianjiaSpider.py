import requests
from bs4 import BeautifulSoup
url='https://sh.lianjia.com/ershoufang/pg2/'
headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'TY_SESSION_ID=d641e023-69e6-4d8b-8497-760d4fe4407a; select_city=310000; all-lj=c60bf575348a3bc08fb27ee73be8c666; lianjia_uuid=0452fe42-90a4-4442-9476-68f5f67839c5; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1572167793; _smt_uid=5db56071.1f8a764c; UM_distinctid=16e0c80ba27c6-099e22b12cc61c-b363e65-1fa400-16e0c80ba285c3; CNZZDATA1253492439=243955138-1572167245-%7C1572167245; CNZZDATA1254525948=1611143896-1572167287-%7C1572167287; CNZZDATA1255633284=189258364-1572166302-%7C1572166302; CNZZDATA1255604082=1693514715-1572167157-%7C1572167157; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e0c80bc923f6-01371378992808-b363e65-2073600-16e0c80bc933a2%22%2C%22%24device_id%22%3A%2216e0c80bc923f6-01371378992808-b363e65-2073600-16e0c80bc933a2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1066956859.1572167796; _gid=GA1.2.1341751489.1572167796; lianjia_ssid=fab57c27-4ab6-6588-4c60-38d1f2f1246b; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1572171593; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMDRkODI5OTFiOGY5ZGNlZjc0ZTIxZTk0ZDI5MTA0YmU2OGY0MGRkMGIwZWQ1ZDA2NThmZTY0NWE3OWI2MzM2YmQ4NzhhZGFjMzhhMDVjMjg3NzBlZjIxNmVjOGY2NmU0MmZlZTBjZmE4NDE3MTY2NDU5N2ZmODkwYWE4MGNmMTU3MjJiYTk5NGI1ZGRkMDE3NWE3YTkwMzBkMmRiMGQ0NGI4MDcxOTQ3ZmYwZGM1OGM4YTAwMzI5ZmUzZTc3OWVkMDYxNTc4NjcxNDE0MWRjNTZmZmQ4OTk0MWE1NWVlNjNmOTg1MDFlMDliOTQzNDkwNmNhZjljODlhNTU2YjI3M2NlZjdiODM0YjZhY2ZjY2Y5ZmFmNzE4NzEzMGVmZjkzMzZlZDQ1ZmVjODNhNDRlNzQwNjU5YmUwMWM3OGQ0YjZcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiYjdiM2VkODBcIn0iLCJyIjoiaHR0cHM6Ly9zaC5saWFuamlhLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1',
    'Host': 'sh.lianjia.com',
    'Referer': 'https://sh.lianjia.com/ershoufang/107101787273.html',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
con = requests.get(url)
print(con)