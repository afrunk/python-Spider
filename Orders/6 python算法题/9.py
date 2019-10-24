from math import sqrt
s = input()
s = s.split(' ')
a = float(s[0])
b = float(s[1])
c = float(s[2])
eps=10e-6
if  abs(b**2-4*a*c) < eps:
    x1 = (-b+sqrt(b*b-4*a*c))/(2*a)
    print("x1=x2=%.5f" %x1)
elif b**2-4*a*c>0:
    x1 = (-b+sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-sqrt(b*b-4*a*c))/(2*a)
    print("x1=%.5f;x2=%.5f,"%(x1,x2))
else :
    shi = (-b/(2*a))
    if abs(shi-0) < eps:
        shi=0
    xu = sqrt(4*a*c-b*b)/(2*a)
    print("x1=%.5f+%.5fi;x2=%.5f-%.5fi"%(shi,xu,shi,xu))



