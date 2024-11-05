Arr=[32+5,5+2,6+190,1*32,0/1000,1000*2,9/100000,103]
def qsort(Arr):
    if len(Arr) <= 1: 
        return Arr
    else: 
        pivote = Arr[-1]
        mpivote = [x for x in Arr[:-1] if x <= pivote]
        Mpivote = [x for x in Arr[:-1] if pivote < x]
        return qsort(mpivote) + [pivote] + qsort(Mpivote)
Sarr = qsort(Arr)
print (f"Ordenamiento rápido: {Sarr}")


def msort(Arr):
    if len(Arr) <= 1:
        return Arr
    else:
        Dividir = len(Arr)//2
        DerArr = msort(Arr[Dividir:])
        IzqArr = msort(Arr[:Dividir])
        return merge(IzqArr,DerArr)
def merge(izq,der):
    final=[]
    i=j=0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            final.append(izq[i])
            i+=1
        else: 
            final.append(der[j])
            j+=1
    final.extend(izq[i:])
    final.extend(der[j:])
    return final
Marr = msort(Arr)
print (f"Ordenamiento de mezcla: {Marr}")




