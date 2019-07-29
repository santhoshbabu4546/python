x1=int(input())
if(x1>=-2**15+1 and x1<=2**15+1):
  print('INT')
elif(x1>=-2**31+1 and x1<=2**31+1):
  print('LONG')
else:
  print('LONG LONG')  
