#a
rss=int(input())
god=list(map(int,input().split()))
for h in range(len(god)-1):
   if(god[h]>god[h+1]):
      print(h)
