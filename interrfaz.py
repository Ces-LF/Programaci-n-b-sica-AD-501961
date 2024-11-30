import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

def fetch_image_url(etag):
    url = f"https://search.idigbio.org/v2/search/media{etag}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        accesuri = data.get("items", [])
        if accesuri:
            image_url = accesuri[0].get("accesuri")[0].get("large")
            return image_url
    return None

def display_image(etag):
    image_url = fetch_image_url(etag)
    if image_url:
        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((300, 300)) 
        img_tk = ImageTk.PhotoImage(img)

        image_label.config(image=img_tk)
        image_label.image = img_tk 

root = tk.Tk()
root.title("Visor de Imágenes etag")

etag_label = ttk.Label(root, text="Ingresa el etag:")
etag_label.pack(pady=5)
etag_entry = ttk.Entry(root, width=50)
etag_entry.pack(pady=5)

show_button = ttk.Button(root, text="Mostrar Imagen", command=lambda: display_image(etag_entry.get()))
show_button.pack(pady=5)

image_label = ttk.Label(root)
image_label.pack(pady=10)

root.mainloop()