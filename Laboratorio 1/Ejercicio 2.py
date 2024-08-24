c=input("escribe el primer número: ")
c=float(c)
b=input("escribe el segundo número: ")
b=float(b)
d=input("escribe el tercer número: ")
d=float(d)
def max_de_tres(c,b,d):
    if c>b and c>d:
        return c
    elif b>c and b>d:
        return b
    elif d>c and d>b:
        return d
print("el mayor es: ",max_de_tres(c,b,d))    