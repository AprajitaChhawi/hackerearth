def sum(x):
    temp=int(x)
    if(temp==0 or temp==6 or temp==9):
        return 6
    if(temp==1):
        return 2
    if(temp==2 or temp==3 or temp==5):
        return 5
    if(temp==4):
        return 4
    if(temp==8):
        return 7
    if(temp==7):
        return 3
t=int(input())
while(t):
    t=t-1
    n=list(input())
    c=len(n)
    d=0
    while(c):
        d=d+sum(n[c-1])
        c=c-1
    if(d%2==1):
        print(7,end="")
        d=d-3
        print('1'*int(d/2))
    else:
        print('1'*int(d/2))
            

            
            
