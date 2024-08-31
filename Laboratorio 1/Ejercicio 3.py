#Definir una funcion que calcule la longitud de una lista o cadena dada
cadenaLista=input("ingresa un elemento: ")
lista=[]
lista.append(cadenaLista)
i=input("si desea incluir mas elementos, introduca si: ") 
while i=="si":
    cadenaLista=input("ingresa un elemento: ")
    lista.append(cadenaLista)
    i=input("si desea incluir mas elementos, introduca si: ") 
tamaño = 0
for value in lista:
    tamaño = tamaño + 1
print(tamaño)
