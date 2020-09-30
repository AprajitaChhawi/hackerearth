try:
    def nd_largest(l):
        first=second=-2147483548
        for i in l:
            if(i>first):
                second=first
                first=i
            elif(i>second and i!=first):
                second=i
        return second
    def decrement(l,a):
        l1=[]
        for i in l:
            if((i-a)>0):
                l1.append(a)
            else:
                l1.append(i)
        return l1
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        count=0
        if(n==1):
            print(1)
            break
        else:
            while(len(set(l))!=1):
                count=count+1
                a=nd_largest(l)
                l=decrement(l,a)
        print(count+1)
except Exception:
    pass;
