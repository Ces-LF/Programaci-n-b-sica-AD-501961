c=input("ingrese el primer número: ")
c=float(c)
b=input("ingrese el segundo número: ")
b=float(b)
def max_num(c,b):
    if c>b:
        return c
    elif b>c:
        return b
    
print("el mayor es: ",max_num(c,b))