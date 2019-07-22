jo=str(input())
ab=0
ab1=0
for k in jo:
   if k.isnumeric():
       ab+=1
   else:
        pass
for k in jo:
    if k.isalpha():
        ab1+=1
    else:
        pass
if ab>=1 and ab1>=1 :
    print('Yes')
else:
    print('No')
