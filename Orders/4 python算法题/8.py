s=int(input())
a=int(s%10) # 个位
b=(int(s/10))%10
c=int(s/100)
print(a*100+b*10+c)
