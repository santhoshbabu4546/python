import sys, string, math
d = input()
h = d.count(d[0])
flag = 1
for j in range(1,len(d)) :
    if d.count(d[j]) != h :
        flag = 0
        break
if flag : print('Yes')
else : print('No')
