import sys, string
r = input()
flag = 0
for d in r :
    if d =='a' or d=='i' or d=='e' or d=='o' or d=='u' :
        flag = 1
        break
if flag : print('yes')
else :    print('no')
