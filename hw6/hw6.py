a="a"
list=[]
k=0
while a!="":
    a = input()
    list.append(a)
    k=k+1
for i in range(k):
    b=len(list[i])
    d=list[i]
    c=""
    for u in range (b):
        if (u+1)%3!=0:
            c=c+d[u]
    l=""
    for u in range (len(c)):
        p=len(c)-u-1
        l=l+c[p]
    list[i]=l+"\n"
with open("referats.txt", "w", encoding="utf-8") as f:    
    for i in range (len(list)):
        f.write(list[i])


