def filtrar_mayusculas(cadena):
    filtrar={'mayusculas':0}
    for c in cadena:
        if c.isupper():
            filtrar['mayusculas']+=1
    return filtrar
A=input("ingresa una palabra: ")
print(filtrar_mayusculas(A))
