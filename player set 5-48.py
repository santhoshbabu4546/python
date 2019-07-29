numa=int(input())
list1=[]
for j in range(1,numa+1):
    if(numa%j==0):
        list1.append(j)
for num in list1:
    if(num%2!=0):
        print(num,end=" ")
