p=input()
v=['a','e','i','o','u']
if p.isalpha():
  if p in v:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")

