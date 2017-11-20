

with open("text.txt", encoding="utf-8") as f:
    for line in f:    
        if line.endswith("\n"):
            words = line.split()
            b=b+len(words)
            c=c+1
        print(b,c)
