s=input()
s=s.split(' ')
r=int(s[1])
h=int(s[0])
Pi=3.14159
v= Pi*r*r*h
data = int(20000/v)
if data*v<20000:
    data += 1
print(data)









