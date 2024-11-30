import tkinter as tk
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("1200x1200")

set_appearance_mode("dark")
set_default_color_theme("green")

logo = CTkImage(light_image=Image.open('C:\\Users\\Usuario\\Desktop\\Programaci-n-b-sica-AD-501961\\Logo.png'), 
                dark_image=Image.open('C:\\Users\\Usuario\\Desktop\\Programaci-n-b-sica-AD-501961\\Logo.png'),
                size=(260,250))
labelIm = CTkLabel(master = app, text = "", image = logo)
labelIm.place(relx=0.5, rely=0.3, anchor="center")


def buscar():
    print(f"Resultado: {entry.get()}")

label = CTkLabel(master = app, text="Busca mediante uuid, etag, nombre científico o nombre común", font=("Arial", 20), text_color = "#80DAEB")
label.place(relx=0.5, rely=0.1, anchor="center")

entry = CTkEntry(master = app, placeholder_text="Ingresa el dato", width=300, text_color="#80DAEB")
entry.place(relx=0.5, rely=0.6, anchor="center")

button = CTkButton(master = app, text = "Buscar", command = buscar)
button.place(relx=0.5, rely=0.8, anchor="center")

if response = 200:

elif:
ventana_error= CTkToplevel()
ventana_error.title("No existe")
ventana_error.geometry("300x300")
else:


app.mainloop()

