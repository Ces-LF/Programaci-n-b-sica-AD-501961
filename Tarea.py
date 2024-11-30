n=float(input("ingresa un número: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(f"factorial: {factorial(n)}")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(f"fibonacci: {fibonacci(i)}")

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]
cadena = "Anita lava la tinA"
print(invertir_cadena(cadena)) 

def potencia(base, exponente):
 
    if exponente == 0:
        return 1
 
    else:
        return base * potencia(base, exponente - 1)
 
base = 2
exponente = 3
print(potencia(base, exponente))

def suma_digitos(numero):
 
    if numero == 0:
        return 0
 
    else:
        return numero % 10 + suma_digitos(numero // 10)


numero = 1234
print(suma_digitos(numero)) 

def merge_sort(arr):
  
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Ordenar la mitad izquierda
    right_half = merge_sort(arr[mid:])  # Ordenar la mitad derecha
     
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
   
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    
    return sorted_array

arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  

def quicksort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
   
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(arr)) 

def busqueda_binaria(arr, x):
    izquierda, derecha = 0, len(arr) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if arr[medio] == x:
            return medio  
        
        elif arr[medio] > x:
            derecha = medio - 1
        
        else:
            izquierda = medio + 1
    
    return -1  

x = 27
print(busqueda_binaria(arr, x))  

def multiplicar_matrices(A, B):
    
    if len(A[0]) != len(B):
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B.")
    
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):  
        for j in range(len(B[0])):  
            for k in range(len(B)):  
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
resultado = multiplicar_matrices(A, B)
print(resultado)  

def elevar_matriz(A, potencia):
  
    if len(A) != len(A[0]):
        raise ValueError("La matriz debe ser cuadrada para elevarla a una potencia.")
    
    n = len(A)
    resultado = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    for _ in range(potencia):
        resultado = multiplicar_matrices(resultado, A)
    
    return resultado



