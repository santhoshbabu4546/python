o=int(input())
t=str(input())
t=list(t)
for j in t:
    if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
        t.remove(j)
r=t[::-1]
print("".join(r))
