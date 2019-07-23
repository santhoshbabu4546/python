import sys, string, math
x,y = map(int,input().split())
i = math.sqrt(x * y)

if i == int(i) : print('yes')
else :           print('no')
