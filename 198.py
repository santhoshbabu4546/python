#a
import math
s,b=map(int,input().split())
h=math.gcd(s,b)
lcm=(s*b)/h
print(math.ceil(lcm))
