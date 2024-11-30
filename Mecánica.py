import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

def fetch_image_url():
    url = "https://search.idigbio.org/v2/search/media"
    params = {
        'rq': '{"kingdom":"plantae"}'
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])
        if items:
            print("Items encontrados:", len(items))
            print("Estructura del primer item:", items[0])
            for item in items:
                media_records = item.get("mediarecords", [])
                if media_records:
                    print(f"Media records para el item {item.get('uuid', 'sin_id')}: {media_records}")
                    for record in media_records:
                        image_url = record.get("thumbnailURL") or record.get("large") or record.get("url") 
                        if image_url:
                            print("Imagen encontrada:", image_url)
                            return image_url
    else:
        print(f"Error al obtener datos: {response.status_code}")
    return None

def display_image():
    image_url = fetch_image_url()
    if image_url:
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                img_data = response.content
                img = Image.open(BytesIO(img_data))
                img = img.resize((300, 300))
                img_tk = ImageTk.PhotoImage(img)
                image_label.config(image=img_tk, text="")
                image_label.image = img_tk
            else:
                image_label.config(text="No se pudo descargar la imagen.")
        except Exception as e:
            print(f"Error al procesar la imagen: {e}")
            image_label.config(text="Error al cargar la imagen.")
    else:
        image_label.config(text="No se encontraron imágenes.")

root = tk.Tk()
root.title("Consulta iDigBio - Plantae")

image_label = ttk.Label(root, text="Haz clic en 'Mostrar Imagen' para comenzar.")
image_label.pack(pady=10)

show_button = ttk.Button(root, text="Mostrar Imagen", command=display_image)
show_button.pack(pady=10)

root.mainloop()