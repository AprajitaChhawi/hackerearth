t=int(input())
while t>0:
    t=t-1
    flag=0
    l1=int(input())
    l=list(map(int,input().split(" ")))
    for i in range(0,len(l)-1):
        if(l[i+1]-l[i]==min(l[i+1],l[i])):
           
           print("YES")
        else:
            print("NO")
           
    
    
           
         
            
        
                   
