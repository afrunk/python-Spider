import requests
import json
url ='http://api.map.baidu.com/directionlite/v1/riding?origin=39.1428487200,117.2014880400&destination=39.1339832700,117.1736891900&ak=lIS08xVAukbIURPaRxrGdaDqO97NtGSt&qq-pf-to=pcqq.c2c'
con = requests.get(url).text
content_list = []
con = json.loads(con)
# print(con['result']['routes'][0]['steps'])
contents =con['result']['routes'][0]['steps']
for i in contents:
    # print(i['path'])
    print(i)
    list_num = i['path'].split(';')
    print(list_num)
    # print(list_num)
    for j in list_num:
        content_list.append(j)

print("去除重复元素前：",len(content_list))
content_list =set(content_list)
print("去除重复元素后：",len(content_list))
print(content_list)
with open("NewData.txt",'a+',newline='') as f: # 写入到本地csv中 a+会自动创建文件 newline解决中间有空行的问题
    for data in content_list:
        f.write(data)
        f.write('\n')
f.close()