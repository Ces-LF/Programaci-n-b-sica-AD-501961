import requests
from openpyxl import Workbook
from customtkinter import *
from tkinter import messagebox

url = 'https://search.idigbio.org/v2/search/records/'

archivo_nombre = "plantas1.txt"
arch = ""

params = {
    "rq": {
        "kingdom": "Plantae", 
        "phylum": ["magnoliophyta", "pynophyta", "spermatophyta"],
        "class": ["liliopsida", "magnoliopsida", "monocotyledonae", "dicotyledonae", "pinopsida"]
    },
    "limit": 5000
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
                    data = item.get("data", {})
                    lat = index_terms.get('geopoint', {}).get('lat', None)
                    lon = index_terms.get('geopoint', {}).get('lon', None)

                    Dom = "Dominio: Eukarya"
                    Kin = f"Reino: {index_terms.get('kingdom', 'Dato no disponible')}"
                    Div = f"Division: {index_terms.get('phylum', 'Dato no disponible')}"
                    Cla = f"Clase: {index_terms.get('class', 'Dato no disponible')}"
                    Or = f"Orden: {index_terms.get('order', 'Dato no disponible')}"
                    Fam = f"Familia: {index_terms.get('family', 'Dato no disponible')}"
                    Gen = f"Genero: {index_terms.get('genus', 'Dato no disponible')}"
                    Esp = f"Especie: {index_terms.get('specificepithet', 'Dato no disponible')}"
                    Nom = f"Nombre cientifico: {index_terms.get('scientificname', 'Dato no disponible').capitalize()}"
                    NomCom= f"Nombre comun: {index_terms.get('commonname', 'Dato no disponible') or data.get('dwc:vernacularName', 'Dato no disponible')}"
                    Est = f"Estado: {index_terms.get('stateprovince', 'Dato no disponible') or data.get('dwc:stateProvince', 'Dato no disponible')}"
                    Pa = f"Pais: {index_terms.get('country', 'Dato no disponible')}"
                    U = f"uuid: {item.get('uuid', 'Dato no disponible')}"
                    E = f"etag: {item.get('etag', 'Dato no disponible')}"
                    Gp = f"Geopunto: {index_terms.get('geopoint', 'Dato no disponible')}"
                    if lat is not None and lon is not None:
                        if 23.166861 <= lat <= 27.758262 and -101.162811 <= lon <= -98.431148:
                            Gp = "Nuevo Leon"
                        elif 25.079642 <= lat <= 29.70575 and -102.175286 <= lon <= -101.559122:
                            Gp = "Cohahuila"
                        else:
                            Gp = "fuera del rango"
                    else:
                            Gp = "Coordenadas no disponibles"
                    arch += (f"{Dom}\n{Kin}\n{Div}\n{Cla}\n{Or}\n{Fam}\n{Gen}\n{Esp}\n{Nom}\n{NomCom}\n{Est}\n{Pa}\n{U}\n{E}\n{Gp}\n\n")

        except ValueError:
            print("Error al decodificar la respuesta JSON.")
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Error en la solicitud:", e)

# Guardar en archivo
with open(archivo_nombre, "w") as archivo:
    archivo.write(arch)

print("Generado: 'plantas1.txt'.")

wb = Workbook()
hoja = wb.active
hoja.title = "Hoja 1"


encabezados = [
    "Dominio", "Reino", "División", "Clase", "Orden", 
    "Familia", "Género", "Especie", "Nombre científico", "Nombre comun", "Estado",
    "País", "uuid", "etag", "latitud", "longitud"
]
hoja.append(encabezados)


for item in records:
    index_terms = item.get("indexTerms", {})

    fila = [
        "Eukarya",  # Dominio
        index_terms.get('kingdom', 'Dato no disponible'),
        index_terms.get('phylum', 'Dato no disponible'),
        index_terms.get('class', 'Dato no disponible'),
        index_terms.get('order', 'Dato no disponible'),
        index_terms.get('family', 'Dato no disponible'),
        index_terms.get('genus', 'Dato no disponible'),
        index_terms.get('specificepithet', 'Dato no disponible'),
        index_terms.get('scientificname', 'Dato no disponible').capitalize(),
        index_terms.get('commonname', 'Dato no disponible') or data.get('dwc:vernacularName', 'Dato no disponible'),
        index_terms.get('stateprovince', 'Dato no disponible') or data.get('dwc:stateProvince', 'Dato no disponible'),
        index_terms.get('country', 'Dato no disponible'),
        item.get('uuid', 'Dato no disponible'),
        item.get('etag', 'Dato no disponible'),
        index_terms.get('geopoint', {}).get("lat", None),
        index_terms.get('geopoint', {}).get("lon", None)
    ]

    hoja.append(fila)

wb.save("plantas1.xlsx")
print("Generado: 'plantas1.xlsx'.")

def buscar_en_archivo(dato_buscar):
    archivo = "plantas1.txt"
    try:
        with open(archivo, "r") as archivo:  
            contenido = archivo.read()
            # Dividir la información en bloques
            bloques = contenido.strip().split("\n\n")
            for bloque in bloques:
                if dato_buscar.lower() in bloque.lower():  
                    return bloque  
        return None  
    except FileNotFoundError:
        messagebox.showerror("Error", f"El archivo '{archivo}' no fue encontrado.")
        return None

def buscar():
    dato = entry.get().strip()
    if not dato:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dato para buscar.")
        return

    resultado = buscar_en_archivo(dato)  
    if resultado:
        ventana_resultados = CTkToplevel()
        ventana_resultados.title("Resultados")
        ventana_resultados.geometry("600x400")
        texto_resultados = CTkTextbox(ventana_resultados, width=500, height=300)
        texto_resultados.pack(pady=10)
        texto_resultados.insert("1.0", resultado)
        texto_resultados.configure(state="disabled")  
    else:
        messagebox.showerror("Error", f"No se encontró información para: {dato}")

app = CTk()
app.geometry("800x600")

set_appearance_mode("dark")
set_default_color_theme("green")

frame = CTkFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
frame.pack(expand=True)

label = CTkLabel(master=frame, text="ingresa nombre científico, uuid o etag", font=("Arial", 20), text_color="#80DAEB")
entry = CTkEntry(master=frame, placeholder_text="ingresa...", width=300, text_color="#80DAEB")
btn = CTkButton(master=frame, text="Buscar", command=buscar)

label.pack(anchor="s", expand=True, pady=10, padx=30)
entry.pack(anchor="s", expand=True, pady=10, padx=30)
btn.pack(anchor="n", expand=True, padx=30, pady=20)

app.mainloop()
