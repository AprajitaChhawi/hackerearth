try:
    t=int(input())
    while t:
        t=t-1
        p,h=map(int,input().split())
        while(p and h):
            p=p-h
            h=int(h/2)
        if(p>0):
            print(0)
        else:
            print(1)
except Exception:
    pass;
