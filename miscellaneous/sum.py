try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split(())))
        s=sum(l)
        print(s)
except Exception:
    pass;
