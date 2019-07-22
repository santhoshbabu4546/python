check_string = input()
chars = check_string
chk = len(check_string)
for char in char:
   count = check_string.count(char)
   if count>=1:
    if(chk>=count):
     chk=count
 for char in chars:
    count = check_string.count(char)
    if(chk==count):
     print(char,end='')
