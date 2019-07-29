number_gh=int(input())
for j in range(2,number_gh):
    if(number_gh%j==0):
        print("yes")
        break
else:
    print("no")
