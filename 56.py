b1=int(input())
y=b1
sum=0
while b1>0:
    sum+=((b1%10)**3)
    b1=b1//10
if (sum==y):
    print('yes')
else:
    print('no')
