n=input()
for j in n:
    if(j.islower()):
        print(j.upper(),end="")
    else:
        print(j.lower(),end="")
