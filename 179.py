import sys, string
h = input()
g = len(h)
n = g//2
if g%2 == 1 : h2 = h[:n] + '*' + h[n+1:]
else :        h2 = h[:n-1] + '**' + h[n+1:]
print(h2)
