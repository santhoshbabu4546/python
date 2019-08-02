#a
mm=list(map(int,input().split()))
o=mm[len(mm)-1]
u=[j for j in input().split()]
for j in u:
	if u.count(str(j))==o:
		print(j)
		break
