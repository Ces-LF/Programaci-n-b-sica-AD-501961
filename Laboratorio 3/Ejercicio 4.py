import time
def dias_transcurridos(fechanac,fechaact):
    formato_fecha="%d/%m/%Y"
    a=time.mktime(time.strptime(fechanac,formato_fecha))
    b=time.mktime(time.strptime(fechaact,formato_fecha))
    delta=a-b
    return int (delta/86400)
c=input("ingrese su fecha de nacimiento en formato DD/MM/AAAA: ")
fechanac=c
fechaact="21/8/2024" 
print("han pasado",dias_transcurridos(fechaact,fechanac),"dias")
