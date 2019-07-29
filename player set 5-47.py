ru1,ru2,ru3=map(int,input().split(" "))
if(ru1!=0 and ru2!=0 and ru3!=0):
    r=ru1+ru2+ru3
else:
    r=0
if(r==180):
    print("yes")
else:
    print("no")
