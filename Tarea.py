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
