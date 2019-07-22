m1,v1=map(int,input().split())
power=0
check=0
sbd=0
while power<m1:
    power=v1**inc
    if power==m1:
        check=1
    sbd+=1
if check==1:
    print("yes")
else:
    print("no")
