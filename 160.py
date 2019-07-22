ab,cd=map(int,input().split())
gate=1
for j in range(1,100):
      if(pow(cd,j)==ab):
        print("yes")
        gate=0
        break
if(gate==1):
    print("no")
