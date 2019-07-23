import sys, string
x,y = map(int,input().split())
z = abs(x-y)
if z % 2 == 1 : print('odd')
else :          print('even')
