s='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
a=input()
k=int(input())
for x in a:
    b = s.find (x)
    d = (b+k)%33
    c = s[d]
    print (c)
    
