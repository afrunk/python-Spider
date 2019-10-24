s=input()
s=s.split(' ')
weight=int(s[0])
biaozhi =s[1]
sum = 0
if weight<=1000:
    sum+=8
else:
    shang = (weight-1000)/500
    if int(shang)< shang:
        sum = sum +8 +(int(shang)+1)*4
    else:
        sum = sum + 8 + shang*4

if biaozhi=='y':
    sum += 5

print(sum)