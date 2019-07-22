num=int(input())
h=input().split(" ")
list1=[]
if(len(h)==num):
    for j in sorted(h):
        list1.append(j)
if(list1==h):
    print("yes")
else:
    print("no")
