import sys, string
h = int(input())
U = []
for j in range(1,h+1) :
    if h%j == 0 : U.append(j)
print(*U)
