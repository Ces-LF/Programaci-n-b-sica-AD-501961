#PROBLEMA 1
lista1=[3,5,7,9]
suma=0
for i in lista1:
    suma=suma+i
print(suma)

#PROBLEMA 2
def fact(n):
    if n==0 or n==1:
        return 1
    else: 
        return n*(fact(n-1))

print(fact(6))

#PROBLEMA 3
def QS(lista2):
    if len(lista2)<=1:
        return lista2
    pivote= lista2[-2]
    izquierda=[x for x in lista2 if x<pivote]
    medio=[x for x in lista2 if x==pivote]
    derecha=[x for x in lista2 if x>pivote]
    return QS(izquierda)+medio+QS(derecha)

lista2=[10,7,8,9,1,5]
Lordenada=QS(lista2)
print(Lordenada)

#PROBLEMA 4
def BB(Lordenada,numero):
    inicio=0
    final=len(Lordenada)-1
    while inicio<=final:
        mitad=(inicio+final)//2
        if Lordenada[mitad]==numero:
            return mitad
        elif Lordenada[mitad]<numero:
            inicio=mitad+1
        else:
            final=mitad-1
    return -1

numero=8
busqueda=BB(Lordenada,numero)
print(busqueda)

#PROBLEMA 5
class FiguraGeometrica:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Atri(self):
        return (self.base * self.altura) / 2

Triangulo = FiguraGeometrica(base=10, altura=5)
Area = Triangulo.Atri()
print(Area)

#PROBLEMA 6
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
respuesta = requests.get(url)
if respuesta.status_code == 200:
    datos = respuesta.json()  
    id = datos["id"]  
    resultado = id * 100  
    print(resultado)
else:
    print(respuesta.status_code)

#PROBLEMA 7
import statistics as st
print(st.median([2, 4, 4, 4, 5, 5, 7]))

#PROBLEMA 8
Frec = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frecuencias = {}
for i in Frec:
    frecuencias[i] = frecuencias.get(i, 0) + 1

SFrec = sum(frecuencias.values())
for i, frec in frecuencias.items():
    print(f"{i}: {frec}")
print(SFrec)

#PROBLEMA 9
import tkinter as tk
def sumar():
    Sus = 45 + 55
    Lla.config(text=f"Suma: {Sus}")
ventana = tk.Tk()
Ssu = tk.Button(ventana, text="Suma de 45 y 55", command=sumar)
Ssu.pack(pady=20)
Lla = tk.Label(ventana, text="La suma es:")
Lla.pack(pady=20)
ventana.mainloop()

# Final: Suma total de los resultados
final_sum = suma + fact(6) + busqueda + Area + suma1 + resultado + st.median([2,4,4,4,5,5,7]) + SFrec + 45 + 55
print(final_sum)
