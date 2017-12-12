with open("text.txt", encoding="utf-8") as f:
    lines = f.readlines()
i=1
while i<len(lines):
    a=lines[i]
    k=""
    b=0
    while k != "|":
        k=a[b]
        b=b+1
    if b>=20:
        print(lines[i])
    i=i+1
