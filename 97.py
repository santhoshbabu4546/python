b,t=raw_input().split()
r=abs(len(b) - len(t))
for j in range(len(b)):
     if len(t)==1 and t[j] in b:
            break
     if j>=len(b)  or j>=len(t):
            break
     if t[j]!=t[j] and t[j]:
            r=r+1
print(r)
