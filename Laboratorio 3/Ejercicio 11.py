c=input("ingresa tu peso en kilogramos: ")
b=input("ingresa tu estatura en metros: ")
c=float(c)
b=float(b)
IMC=c/b**2
def I_M_C(IMC):
    if IMC<18.5:
        return "categoría: peso bajo"
    elif 18.5<IMC<24.9:
        return "categoría: ideal"
    elif 24.9<IMC<29.9:
        return "categoría: sobrepeso"
    elif 29.9<IMC<34.9:
        return "categoría: obesidad"
    elif 34.9<IMC:
        return "categoría: obesidad mórbida"

print("tu IMC es",IMC,", ",I_M_C(IMC))