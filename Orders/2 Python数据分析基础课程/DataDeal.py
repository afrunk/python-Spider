

# 第二次作业
Stu_score=['语文80','数学90','英语30','物理70','化学70','生物100']
len_score = len(Stu_score)
print(len_score)
i=0
while i < len_score:
    if int(Stu_score[i][2:])<60:
        print(Stu_score[i][:2]+'不及格'+Stu_score[i][2:])
    i+=1
j=0
total = 0
while j<len_score:
    total = total + int(Stu_score[j][2:])
    j+=1
average = total/6
print("张明平均分是%d" %(average))
print('张明总分是%d'%(total))


'''
# 第一次作业

Stu_score='语文80，数学90，英语30，物理70，化学70，生物10'
len_score = len(Stu_score)
print(len_score)
i=0
while i < len_score:
    if int(Stu_score[i+2:i+4])<60:
        print(Stu_score[i:i+2]+'不及格'+Stu_score[i+2:i+4])
    i+=5
j=0
total = 0
while j<len_score:
    total = total + int(Stu_score[j+2:j+4])
    j+=5
average = total/6
print("张明平均分是%d" %(average))
print('张明总分是%d'%(total))


# 第三次作业

def find_factor(nums):
    i=1
    str1=''
    while i < nums:
        if nums%i==0:
            str1 = str1 +' '+ str(i)
        i+=1
    return str1

numlist =[10,15,18,25]
for i in numlist:
    return_str = find_factor(i)
    print("%d的因数是：%s"%(i,return_str))


# 第四次作业

import numpy as np
a = np.array([[10,11,12,13],[14,15,16,17],[18,19,20,21]])
b = np.array([[30,31,32,33],[34,35,36,37],[38,39,40,41]])
print(a.mean())
a=a/a.mean()
print(a)
print(a+b)


# 第五次作业

import numpy as np
a= np.array([[98,92,93,87,88,88],[84,75,76,77,78,99],[97,95,99,67,88,65]])
print(np.sum(a[0]),np.average(a[0]),np.std(a[0]))
print(np.sum(a[1]),np.average(a[1]),np.std(a[1]))
print(np.sum(a[2]),np.average(a[2]),np.std(a[2]))


# 第六次作业
import pandas as pd
import numpy as np
s1 ={
    '城市':['北京','上海','广州','深圳','沈阳'],
    '环比':[101.5,101.2,101.3,102.0,100.1],
    '同比':[120.7,127.8,119.4,140.9,101.4],
    '定基':[121.4,127.8,129.6,135.5,101.6]
}
s=pd.DataFrame(s1,index=['c1','c2','c3','c4','c5'])
print(s)
'''
