import re
l=list(input())
flag=0
s=''.join(map(str,l))
if(re.match('^[0-9]{2}[A-Z][0-9]{3}-[0-9]{2}$',s)):
    if(re.match('^[^AEIOUY]$',l[2])):
        if(((int(l[0])+int(l[1]))%2==0) and ((int(l[3])+int(l[4]))%2==0) and ((int(l[4])+int(l[5]))%2==0) and ((int(l[7])+int(l[8]))%2==0)):
            flag=1
if(flag==0):
    print("invalid")
else:
    print("valid")
    
