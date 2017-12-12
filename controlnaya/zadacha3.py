with open("text.txt", encoding="utf-8") as f:
    lines = f.readlines()
a="a"
list=[]
k=0
b=len(lines)
while a!="":
    a = input()
    list.append(a)
    k=k+1
for i in range(k-1):
    c=1
    while c < b:
        d=list[i]
        q=lines[c]
        j=0
        for n in range(min(len(d), len(q))):
            if d[n]!=q[n]:
                j=j+1
        if (j==0) and (q[len(d)+1]=="|"):
            print(q)
        c=c+1
            
            
