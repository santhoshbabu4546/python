chatc=int(input())
kc=[]
dog=0
for i in range (0,chatc+1):
    dog=abs((2**i)-chatc)
    kc.append(dog)
kall=min(kc)
print(kall)
