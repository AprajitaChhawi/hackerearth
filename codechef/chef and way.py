def minimun(l,a,k1):
    for i in range(a,n,k1):
        prod=prod*l[i]
        print(prod)
    return prod
try:
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    prod=1
    if(len(l)%k==0):
        prod=minimum(l,0,k)
    else:
        for i in range(n):
            if((len(l)-i)%k!=0):
                prod=prod*l[i]
            else:
                prod=prod*minimum(l[i:],i,k)
    print(prod)
except Exception:
    pass;
