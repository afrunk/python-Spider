s=input()
s=s.split(' ')
a=int(s[0])
b=int(s[1])
c=int(s[2])

if a+b>c and a+c>b and b+c>a and a-b<c and a-c<b and b-a <c and b-c<a and c-a<b and c-b<a:
    print("yes")
else:
    print("no")