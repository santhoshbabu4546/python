import sys, string, math
a = int(input())
T = list(map(int,input().split()))
T2 = []
sep1 = len(T)
for f in range(0,sep1-2) :
    for u in range(f+1,sep1-1) :
        for o in range(u+1,sep1) :
            if T[f]+T[u] == L[o] :
                print(T[f],T[u],T[o] )
