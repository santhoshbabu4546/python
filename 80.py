E=int(input())
s=list(map(int,input().split()[:E]))
s.sort()
if E%2==0:
    t=E//2
    print(s[t-1]+s[t])
else:
    t=E//2
    print(s[t])
