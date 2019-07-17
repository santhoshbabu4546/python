u=int(input())
word=list(map(str,input().split()[:u]))
word.sort()
word.sort(key=len)
for j in word:
    print(j,end=" ")
