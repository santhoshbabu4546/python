s=list()
t=input()

s=list(map(int,input().split()))
y=set(s)
for j in y:
    if(s.count(j)<2):
        print(j)
