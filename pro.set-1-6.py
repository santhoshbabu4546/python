f1=int(input())
x=list(map(int,input().split()))
d=0
for o in range(0,f1-2):
	for p in range(1,f1-1):
		for y in range(2,f1):
			if(x[o]<x[p] and x[p]<x[y]):
				d+=1
print(d)
