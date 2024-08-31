c=float(input("escribe el primer número: "))
b=float(input("escribe el segundo número: "))
d=float(input("escribe el tercer número: "))
def max_de_tres(c,b,d):
    if c>b and c>d:
        return c
    elif b>c and b>d:
        return b
    elif d>c and d>b:
        return d
    elif c==d and d==b:
        return "ninguno, son iguales"
print("el mayor es: ",max_de_tres(c,b,d))    