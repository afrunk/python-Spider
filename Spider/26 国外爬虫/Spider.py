"""
https://www.google.com/gen_204?atyp=i&ei=uCC5XZifJJOB-QaSupOYAQ&ct=slh&v=2&s=2&pv=0.8175337222841332&me=6:1572413632854,V,0,0,0,0:11226,U,11226:0,V,0,2588,1920,301:5497,e,B&zx=1572413649580

"""
import requests
import json
url ='https://www.google.com/gen_204?atyp=i&ei=uCC5XZifJJOB-QaSupOYAQ&ct=slh&v=2&s=10&pv=0.8175337222841332&me=41:1572416274200,V,0,0,0,0:67278,U,67278:0,V,0,7108,1920,301:3614,e,B&zx=1572416345093'

headers = {
    'authority':'www.google.com',
    'method': 'POST',
    'path': '/gen_204?atyp=i&ei=uCC5XZifJJOB-QaSupOYAQ&ct=slh&v=2&s=12&pv=0.8175337222841332&me=47:1572416462714,U,117621:0,V,0,7108,1920,301:6631,e,H&zx=1572416469348',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'content-length': '0',
    'content-type': 'text/plain;charset=UTF-8',
    'cookie': 'CONSENT=YES+CN.zh-CN+20170212-13-0; SID=mAdpeNJhjreetAFwVSZTsA1EkbZWXvARHj0tBW0SYguGmhVTfZoaUwYTL0E2kdlLrtbWKA.; HSID=AMf5rqkj9TX19211H; SSID=A7Tm6XKZnrzgLICmn; APISID=8A_5BxIPw1bD3jIe/A59PBclV7sogYRx7D; SAPISID=yPF-L_e-tM8bxsnu/ADf-OTtddDz7al36N; SEARCH_SAMESITE=CgQIs40B; NID=190=Fd69tYHC0mrv_zobS3sl0MW3PBlGArATvXqnUNGiIsmWfFKu5E1lPoid3Ld1HFDWGe7FckRmCbwaq4Tes_2qtUQ2Xdn4TOCUa6mSxRCcW6CaiJvjzAWvBJsMlDNoBQHYC8Wi1lWZ6gTu4AfHkT-xSB2uCMBhUJUcO9ou0sId2-IDBYZnAdDSHyC2_EdyhvoDLAcprqh6yQ8NeWuPcv0w7o161MOEa7m-LFdrukVr9YTzdn3A; 1P_JAR=2019-10-30-5; SIDCC=AN0-TYtnrgkm4LE7O1Iqdrq4BYn-swzu3rJajpdETGLGLsLp0dMiY33NR9KiiH788RUcsp-nqFA',
    'origin': 'https://www.google.com',
    'referer': 'https://www.google.com/',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'x-client-data': 'CLO1yQEIhrbJAQiitskBCMG2yQEIqZ3KAQjiqMoBCMqvygEIzrDKAQj3tMoB'
}

data = {
        'atyp': 'i',
        'ei': 'uCC5XZifJJOB-QaSupOYAQ',
        'ct': 'slh',
        'v': '2',
        's': '10',
        'pv': '0.8175337222841332',
        'me': '41:1572416274200,V,0,0,0,0:67278,U,67278:0,V,0,7108,1920,301:3614,e,B',
        'zx': '1572416345093'
    }
print(data)

con = requests.post(url=url,headers=headers,data=data).text
print(con)