import requests

url = 'https://search.idigbio.org/v2/search/records/'
params = {
    "rq": {
        "kingdom": "plantae",
        "country": "MX"
    },
    "limit": 100
}

response = requests.post(url, json=params) 
arch=""
if response.status_code == 200:
    data = response.json()
    
    records = data.get('items') or data.get('results', [])
    
    for item in records:
        index_terms = item.get("indexTerms", {})

        Dom = "Dominio: Eukarya"
        Kin = f"Reino: {index_terms.get('kingdom')}"
        Div = f"Division: {index_terms.get('phylum')}"
        Cla = f"Clase: {index_terms.get('class')}"
        Or = f"Orden: {index_terms.get('order')}"
        Fam = f"Familia: {index_terms.get('family')}"
        Gen = f"Genero: {index_terms.get('genus').capitalize()}"
        Esp = f"Especie: {index_terms.get('specificepithet')}"
        Nom = f"Nombre cientifico: {index_terms.get('genus').capitalize()} {index_terms.get('specificepithet')}"
        Pa = f"Pais: {index_terms.get('country')}"
        U = f"uuid: {item.get('uuid')}"
        Im = f"Imagen: {index_terms.get('hasImage')}"
        if Im == True:
            Im = f"Imagen: {index_terms.get('hasImage')}"
        else: Im = "No hay imagen"
        arch += (f"{Dom}\n{Kin}\n{Div}\n{Cla}\n{Or}\n{Fam}\n{Gen}\n{Esp}\n{Nom}\n{Pa}\n{U}\n{Im}\n\n")
else:
    print("Error en la solicitud:", response.status_code)

Archivo = "plantas.txt"

with open(Archivo, "w") as archivo:
    archivo.write(arch)

print("Archivo generado exitosamente.")
 