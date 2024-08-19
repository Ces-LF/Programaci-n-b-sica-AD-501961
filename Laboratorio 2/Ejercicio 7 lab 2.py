edades=(10,50,6,32,12)
filtro_mayores_a_20=lambda x: x > 20
mayores=filter(filtro_mayores_a_20,edades)
print(tuple(mayores))