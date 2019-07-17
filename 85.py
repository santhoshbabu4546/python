x=input()
y=x.lstrip('-').replace('.','',1).isdigit()
if(y==True):
  print("Yes")
else:
  print("No")
