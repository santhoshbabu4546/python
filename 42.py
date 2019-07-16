s,b=map(int,input().split())
w=d
r=b
if(s>b):
    while(s>0):
        if((s%b)==0 and (s%w)==0):
            print(o)
            break
        else:
            s=s+1
    
else:
    while(b>0):
        if((b%o)==0 and (b%r)==0):
            print(b)
            break
        else:
            b=b+1
