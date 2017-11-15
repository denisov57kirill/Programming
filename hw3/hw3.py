a=input()
letters=list(a)
b = len (a);
while b > 0:
    for i in range(b):
        c = letters[i]
        print(c, end='')
    b = b-1
    print()
