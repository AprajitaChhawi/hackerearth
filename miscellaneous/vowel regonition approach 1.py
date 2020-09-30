import re
def vowel_count(st):
    count=0
    st1=st.lower()
    for i in st1:
        if(re.match("^[aeiou]$",i)):
            count=count+1
    return count
t=int(input())
while t:
    t=t-1
    sum=0
    s=str(input())
    substring=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
    for i in substring:
        sum=sum+vowel_count(i)
    print(sum)
    
