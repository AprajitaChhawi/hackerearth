t=int(input())
while t:
    t=t-1
    n,k=map(int,input().split(" "))
    l=list(map(int,input().split()))
    s=l[:]
    s.sort()
    if(k-s[0]>0):
        print(k-s[0])
    else:
        print(0)
