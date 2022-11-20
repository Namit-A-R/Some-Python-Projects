import string
s=list(input())
ss=sorted(list(set(s)))
c=0
comp=[]
for i in range(len(s)):
    for j in string.ascii_lowercase:
        sc=list(s)
        sc[i]=j
        if sc==sc[::-1] and sc[::-1] not in comp and sc!=s:
            c+=1
            comp.append(sc[::-1])
print(c)
