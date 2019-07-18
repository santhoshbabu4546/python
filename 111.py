import rs
car=rs.compile('[@_!#$%^&*()<>?.;/\|}{~:]')
v=input()
y=0
for j in range (len(v)):
    if(car.search(v[j])!=None):
        y=y+1
print(y)   
