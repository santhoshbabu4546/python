a,b=map(int,input().split())
for k in range (a+1,b):
    for l in range(2,k):
        if (k%l==0):
            break
    else:
        print(k, end=' ')
