s=input()
s=s.split(' ')
a=s[0]
b=s[1]
c=s[2]
if c in '+-*/':
    ss =a+c+b
    if c=='/' and b=='0':
        print("Divided by zero!")
    else:
        print(eval(ss))
else:
    print("Invalid operator!")