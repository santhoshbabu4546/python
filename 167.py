f = input()
g,t = 0,0
for d in f :
    if d.isalpha() : g += 1
    if d.isdigit() : t += 1
if g and t : print('Yes')
else :       print('No')
