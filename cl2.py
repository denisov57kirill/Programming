s='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
a=input()
k=int(input())
for x in a:
    b = s.find (x)
    if b==-1:
        print(x)
    else:
        d = (b+k)%33
        c = s[d]
        print (c)
    
