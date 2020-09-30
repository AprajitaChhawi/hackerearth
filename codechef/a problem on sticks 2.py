try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        while(0 in l):
            l.remove(0)
        print(len(set(l)))
except Exception:
    pass;
