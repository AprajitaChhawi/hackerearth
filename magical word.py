from math import sqrt
def isPrime(num):
    key=0
    k=int(sqrt(num))+1
    for i in range(2,k):
        if(num%i==0):
            key=1
            break
    if(key>0):
        return False
    else:
        return True
t=int(input())
while(t!=0):
    t=t-1
    n=int(input())
    for i in range(n):
        name=list(input())
        for i in range(0,len(name)):
            num=ord(name[i])
            if(isPrime(num)):
                print(chr(num),end="")
            else:
                n1 = num + 1
                while (True):
                    if (isPrime(n1)):
                        aN = n1  
                        break
                    else: 
                        n1=n1+1
                n2 = num - 1
                while (True):
                    if (isPrime(n2)): 
                        bN = n2  
                        break
                    else: 
                        n2=n2-1
                diff1 = aN -num 
                diff2 = num- bN
                if(aN>176):
                    a=bN
                if(diff1<diff2):
                    a=aN
                else:
                    a=bN
                print(chr(a),end="") 
            
            
