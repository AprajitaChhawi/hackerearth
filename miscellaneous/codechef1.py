n,d=map(int,input().split(" "))
count=0
for i in range(0,n):
    a=int(input())
    if(a%d==0):
        count=count+1
print(count)        
