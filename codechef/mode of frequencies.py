from statistics import *
try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        l1=[]
        for i in set(l):
            c=l.count(i)
            l1.append(c)
        ma=l1.count(l1[0])
        mi=l1[0]
        for i in set(l1):
            if(l1.count(i)>ma):
                ma=l1.count(i)
                mi=i
            if(l1.count(i)==ma):
                if(mi>i):
                    ma=l1.count(i)
                    mi=i
        print(mi)
except Exception:
    pass;
