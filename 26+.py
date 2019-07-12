r,s=map(str,input().split())
if(len(r)!=len(s)):
  print("no")
else:
  a1=[r.count(i) for i in r]
  a2=[s.count(i) for i in s]
  if(e1==e2):
    print("yes")
  else:
    print("no")
