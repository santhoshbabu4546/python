chaa=int(input())
choa=[int(q) for q in input().split(" ")]
chea=0
for t in range(chaa):
      for r in range(t):
           if(choa[r]<choa[t]):
                chea+=choa[r]
print(chea)
