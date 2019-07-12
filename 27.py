int=list(input())  
odd=[]
even=[]
data=[]
for j in range(len(int)):
    if j%2==0:
        even.append(int[j])  #appendd the even position
    else:
        odd.append(int[j])  #append the even position
final=list(map(lambda a,b:a+b,odd,even))  #swap the values
print("".join(final)) 
