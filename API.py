import requests

url = 'https://search.idigbio.org/v2/search/records/'
archivo_nombre = "plantas1.txt"
arch = ""

params = {
    "rq": {
        "kingdom": "plantae",
    },
    "limit": 1000
}

try:
    response = requests.post(url, json=params)

    # Validar el código de estado
    if response.status_code == 200:
        try:
            data = response.json()
            
            # Verificar si los datos están en 'items' o 'results'
            records = data.get("items") or data.get("results", [])
            if not records:
                print("No se encontraron 'items' ni 'results' en la respuesta.")
                print("Respuesta completa de la API:", data)  # Muestra el JSON completo para inspección
            else:
                for item in records:
                    index_terms = item.get("indexTerms", {})

                    Dom = "Dominio: Eukarya"
                    Kin = f"Reino: {index_terms.get('kingdom', 'Dato no disponible')}"
                    Div = f"Division: {index_terms.get('phylum', 'Dato no disponible')}"
                    Cla = f"Clase: {index_terms.get('class', 'Dato no disponible')}"
                    Or = f"Orden: {index_terms.get('order', 'Dato no disponible')}"
                    Fam = f"Familia: {index_terms.get('family', 'Dato no disponible')}"
                    Gen = f"Genero: {index_terms.get('genus', 'Dato no disponible').capitalize()}"
                    Esp = f"Especie: {index_terms.get('specificepithet', 'Dato no disponible')}"
                    Nom = f"Nombre cientifico: {index_terms.get('genus', 'Dato no disponible').capitalize()} {index_terms.get('specificepithet', 'Dato no disponible')}"
                    Pa = f"Pais: {index_terms.get('country', 'Dato no disponible')}"
                    U = f"uuid: {item.get('uuid', 'Dato no disponible')}"
                    E = f"etag: {item.get('etag', 'Dato no disponible')}"
                    Im = f"Imagen: {index_terms.get('hasImage')}"
                    if Im == True:
                       Im = f"Imagen: {index_terms.get('hasImage')}"
                    else: Im = "No hay imagen"
                    arch += (f"{Dom}\n{Kin}\n{Div}\n{Cla}\n{Or}\n{Fam}\n{Gen}\n{Esp}\n{Nom}\n{Pa}\n{U}\n{E}\n{Im}\n\n")

        except ValueError:
            print("Error al decodificar la respuesta JSON.")
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Error en la solicitud:", e)

# Guardar en archivo
with open(archivo_nombre, "w") as archivo:
    archivo.write(arch)

print("Archivo generado exitosamente.")
