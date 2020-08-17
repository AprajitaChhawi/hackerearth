t=int(input())
l=list(map(int,input().split()))
q=list(tuple(l))
q.sort()
k=-1
s=sum(q)
for i in q:
    ans=s-i
    if(ans%7==0):
        k=i
        break
if(k==-1):
    print(k)
else:
    print(l.index(k))
