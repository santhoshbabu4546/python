g=int(input())
if g%2!=0:
    print("1")
else:
    y=True
    for j in range(2,g):
        if g%j==0 and int(g/j)%2!=0:
            y=False
            print(j)
            break
    if y:
        print(g)
