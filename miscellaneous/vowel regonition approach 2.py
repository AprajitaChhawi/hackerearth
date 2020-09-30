import re
t=int(input())
while t:
    t=t-1
    s=str(input())
    s1=0
    t=len(s)
    s2=s.lower()
    for i in range(0,t):
        if(re.match("^[aeiou]$",s2[i])):
            s1=s1+(t-i)*(i+1)
    print(s1)
    
