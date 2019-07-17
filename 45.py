s1=input()
s2=''
s3='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for j in s1:
    if j in s3:
        r=s3.index(j)
        r=r+3
        s2=s2+s3[r]
print(s2
