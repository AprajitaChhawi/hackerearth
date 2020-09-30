def inverse(l):
    l.insert(0,0)
    l1={}
    for i in range(0,len(l)):
        l1[i]=l[i]
    print(l1)
    return l1
n=int(input())
l2=[]
l=list(map(int,input().split()))
if(n==0):
    sys.exit()
elif(n==1):
    print("ambiguous")
else:
    l1=inverse(l)
    l2=[]
    for i in l1.values():
        l2.append(i)
    del l2[0]
    del l[0]
    if(l2==l):
        print("ambiguous")
    else:
        print("not ambiguous")
            
