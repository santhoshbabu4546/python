d=input()
s1=0
for j in range(len(d)):
    if (d[j].isalpha() or d[j].isnumeric() or d[j]==" "):
      continue
    s1=s1+1
else:
    print(s1)
   
