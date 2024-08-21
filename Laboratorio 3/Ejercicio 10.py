lista=[]
c=int(input("ingresa el número de calificaciones, luego ingresa las calificaciones en líneas separadas: "))
for i in range(0,c):
    ele=int(input())
    lista.append(ele)  
sum(lista)  
print("el promedio de las calificaciones es",sum(lista)/c)