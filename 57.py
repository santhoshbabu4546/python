s1,f1=map(int,input().split())
s1+=1
for u in range(s1,f1):
	j=u
	l=[]
	q=list(str(u))
	while(0<j):
		k=j%10
		l.append(k)
		i=j//10
	r=(pow(l[0],3)+pow(l[1],3)+pow(l[2],3))
	if(r==u):
		print(r,end=' ')
