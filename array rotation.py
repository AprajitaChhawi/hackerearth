from array import *
t=int(input())
while t:
    t=t-1
    n,d=map(int,input().split())
    l=list(map(int,input().split()))
    arr=array('i',l)
    for i in range(d,len(arr)):
        print(arr[i],end=" ")
    for i in range(d):
        print(arr[i],end=" ")
    print("\n",end="")
