import math
def pF(n): 
    count=0
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        count+=1 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            count+=1
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        count+=1
    return count
t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    count=0
    if(k==1 and n>=2):
        print(1)
    else:
        if(k>=30):
            print(0)
        else:
            p=int(2**k)
            if(p<=n and pF(n)>=k):
                print(1)
            else:
                print(0)
