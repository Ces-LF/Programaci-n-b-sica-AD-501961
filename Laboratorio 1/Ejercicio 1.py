c=input("ingrese el primer número: ")
c=int(c)
b=input("ingrese el segundo número: ")
b=int(b)
def max_num(c,b):
    if c>b:
        return c
    elif b>c:
        return b
    
print(max_num(c,b))
