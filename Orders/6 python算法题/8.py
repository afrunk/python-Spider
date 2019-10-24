s=input()
s=s.split(' ')
n=int(s[0])
x=int(s[1])
y=int(s[2])

if y%x==0:
    biaozhi = n-(y//x)
else:
    biaozhi = n - y//x -1
if biaozhi < 0:
    biaozhi =0
print(biaozhi)