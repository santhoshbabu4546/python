s=int(input())
s=list(map(int,input().split()))
for j in range(len(s)):
    if((j%2==0)and(s[j]%2!=0)or(j%2!=0)and(s[j]%2==0)):
        print(s[j],end=" ")
