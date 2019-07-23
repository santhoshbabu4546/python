import sys, string, math
h = int(input())
G = []
while h :
    b = h%10
    if b%2 == 1 : G.append(b)
    h //= 10
G = G[::-1]
print(*G)
