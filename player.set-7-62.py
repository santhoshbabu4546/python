g = int(input())
if g %2 == 1 :
    print(1)
    kcs.exit()
for h in range(2,g+1) :
    if g%h == 0 :
        y = g // h
        if y%2 == 1 :
            print(h)
            kcs.exit()
