with open("folder/text.txt", encoding="utf-8") as f:
    text = f.read()
lines = text.splitlines()
i=0
b=0
while i < len(lines):
    words=lines[i].split()
    b=b+len(words)
    i=i+1
print(b/len(lines))
