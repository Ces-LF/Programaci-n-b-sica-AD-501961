import random
n=0
n=random.randrange(1,100)
c=input("ingresa el número que crees que es: ")
c=int(c)
def adv_num(n,c):
    if c in n+10 or c in n-10:
        return "estás relativamente cerca"
    elif c in n+5 or c in n-5:
        return "estás muy cerca"
    elif c in n+1 or c in n-1:
        return "solo un paso más, ¿o menos?"
    elif c in n: 
        return "¡felicidades, lo lograste!"
print(adv_num(n,c))

    