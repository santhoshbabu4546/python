import sys,string, math,itertools
f = input()
P = [f[0]]
h = len(f)
for j in range(3,h,3) :
    P.append(f[j])
f2 = ''.join(P)
print(f2)
