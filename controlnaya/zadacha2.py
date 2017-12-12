with open("text.txt", encoding="utf-8") as f:
    lines = f.readlines()
i=1
d=0
while i<len(lines):
    a=lines[i]
    k=1
    c=0
    while k<len(a):
        if a[k]=="|" and a[k-1]=="|":
            c=c+1
        k=k+1
    k=0
    if c==0:
        d=d+1    
    i=i+1
print(d)
