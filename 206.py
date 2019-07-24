#a
mu,cu,j33=map(int,input().split())
sem=0
for k in range(0,j33):
   sem=sem+mu
   mu=mu+cu
print(sem)
