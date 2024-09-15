c=input("ingresa una palabra: ")
texto=c
es_palindromo=''.join(reversed(texto))
if texto in es_palindromo:
    print('true')
else:
    print('false')
