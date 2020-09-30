t=int(input())
while t:
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[]
    for i in l:
        if(k%i==0):
            l1.append(i)
    if l1:
        print(max(l1))
    else:
        print(-1)
        
    
    
