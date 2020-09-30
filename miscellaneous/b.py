t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    key=0
    for i in range(0,n):
        if(l[i]==1):
            for j in range(i+1,n):
                if(l[j]==1):
                    if(j-i<6):
                        key=1
                        break
    if(key==1):
        print("NO")
    else:
        print("YES")
                    

                    
        
