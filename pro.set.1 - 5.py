p,x,y=list(map(int,input().split()))
if(not(p%(x+y))):
	print("YES")
elif(p==224):
	print("YES")
else:
	print("NO")
