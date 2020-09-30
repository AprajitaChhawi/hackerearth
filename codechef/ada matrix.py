try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        count=0
        l=[]
        for i in range(n):
            l.append([int(x) for x in imput().split()])
        print(l)
        for i in range(n-1,0,-1):
            a=l[i][i-1]+1
            print(a)
            if (a!=l[i][i]):
                count=count+1
                d=a+1
                for i in range(d):
                    for j in range(1,d):
                        trav=b[i][j]
                        b[i][j]=b[j][i]
                        b[j][i]=trav
            print(count)
except Exception:
    pass;
                
