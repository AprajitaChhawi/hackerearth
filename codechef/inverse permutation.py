try:
    n=int(input())
    while n:
        l=list(map(int,input().split()))
        d={}
        l1=[]
        for i in range(n):
            d[i+1]=l[i]
        for(key,value) in sorted(d.items(),key=lambda x:x[1]):
            l1.append(key)
        if(l==l1):
            print("ambiguous")
        else:
            print("not ambiguous")
        n=int(input())
except Exception:
    pass;
            
            
