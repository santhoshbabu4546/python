def fac(i):
  if i==0:
    return 1
  else:
    return i*fac(i-1)
i=int(input())
print(fac(i))
