int=list(map(int,input().split())) 
count=0                             
for s in range(int[0],int[1]+1):   
    t=0
    if s!=1:                        
        if s==2:
            count=count+1
        else:
            for j in range(2,s):
                if s%j ==0:              
                    t=1
                    break
            if t==0:
                count=count+1           
print(count)  
