d=input()
s1=len(d)
count=0
for j in range(0,s1):
    if(d[j]=="("):
        count=count+1
    elif(d[j]==")"):
        count=count-1
if(count==0):
    print("yes")
else:
    print("no")
