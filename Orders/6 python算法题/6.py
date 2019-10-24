n = float(input())
y=0
if n>=0 and n <5:
    y = -n + 2.5
elif n>=5 and n<10:
    y = 2-1.5*(n-3)*(n-3)
else:
    y= n/2 -1.5

print("%.3f"%y)