#Propagación de incertidumbres
a=float(input("Ingresa la medición A: "))
b=float(input("Ingresa la medición B: "))
Deltaa=float(input("ingresa la incertidumbre de A: "))
Deltab=float(input("ingresa la incertidumbre de B: "))
Menu=int(input("1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- Division \n 5.- Salir \n"))
while Menu != 5:
    if Menu == 1:
        print(f"{a+b}±{Deltaa+Deltab}")
    if Menu == 2:
        print(f"{a-b}±{Deltaa+Deltab}")
    if Menu == 3:
        print(f"{a*b}±{a*b*((Deltaa/a)+(Deltab/b))}")
    if Menu == 4:
        print(f"{a/b}±{(a/b)*((Deltaa/a)+(Deltab/b))}")
    Menu=int(input("1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- Division \n 5.- Salir \n"))


