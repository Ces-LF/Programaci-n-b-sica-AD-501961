lista=[]
c=int(input("ingresa el número de elementos de la lista, luego ingresa una lista de números en líneas separadas: "))
for i in range(0,c):
    ele=int(input())
    lista.append(ele)  
sum(lista)  
print("la suma de los elementos de la lista es",sum(lista))