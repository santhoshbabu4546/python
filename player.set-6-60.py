n=list(input().split())
x=n[0]
y=n[1]
for j in x:
  if(j in y):
    print("yes")
    exit()
print("no")
