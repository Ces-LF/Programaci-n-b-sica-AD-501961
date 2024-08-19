def mas_larga(listapalabras):
    lista=[]
    for n in listapalabras:
        lista.append((len(n),n))
    lista.sort()
    return lista[-1][-1]
listapalabras=["pasarela","peaton","carro","esternocleidomastodeo"]
print(mas_larga(listapalabras))