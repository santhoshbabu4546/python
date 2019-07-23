h = int(input())
for j in range(2,h) :
    if h%j == 0 :
        print('no')
        break
else :
    print('yes')
