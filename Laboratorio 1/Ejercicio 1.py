c=float(input("ingrese el primer número: "))
b=float(input("ingrese el segundo número: "))
def max_num(c,b):
    if c>b:
        return c
    elif b>c:
        return b
    elif b==c:
        return "ninguno, son iguales"
    
print("el mayor es: ",max_num(c,b))