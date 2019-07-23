import sys, string
h = int(input())
if h==2 : print('no')
else :
    flag = 0
    for j in range(2,h) :
        if h%j == 0 :
           print('yes')
           break
    else :
        print('no')
