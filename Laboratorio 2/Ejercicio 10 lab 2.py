Años=(1980, 2000, 2020, 2021, 1984)
es_bisiesto=lambda x: x % 4 == 0
bisiestos=filter(es_bisiesto,Años)
print(tuple(bisiestos))