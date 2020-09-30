from math import sqrt
def isPrime(N):
    k=int(sqrt(N))+1
    for i in range(2,k):
        if(N%i==0):
            return False
            break
        else:
            return True
t=int(input())
while(t!=0):
    t=t-1
    n=int(input())
    for i in range(0,n):
        name=input()
        l=list(name)
        aN=-1
        bN=-1
        for i in range(0,n):
            num=ord(l[i])
            if(isPrime(num)==False):
                incr = -1
                multiplier = -1
                count = 1
                while True:
                    if isPrime(num):
                        break
                    else:
                        num = num + incr
                        multiplier = multiplier * -1
                        count = count + 1
                        incr = multiplier * count
                print(chr(num))
            else:
                print(chr(num))
            
             
                
                

                    
                
