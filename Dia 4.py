from customtkinter import *
from tkinter import messagebox

# Función para leer el archivo y obtener la información
def buscar_en_archivo(dato_buscar):
    archivo = "plantas1.txt"
    try:
        with open(archivo, "r") as archivo:  # Abrir correctamente el archivo
            contenido = archivo.read()
            # Dividir la información en bloques
            bloques = contenido.strip().split("\n\n")
            for bloque in bloques:
                if dato_buscar.lower() in bloque.lower():  # Buscar sin importar mayúsculas/minúsculas
                    return bloque  # Retornar el bloque si se encuentra el dato
        return None  # Retorna None si no encuentra el dato
    except FileNotFoundError:
        messagebox.showerror("Error", f"El archivo '{archivo}' no fue encontrado.")
        return None

# Función para manejar la búsqueda desde la interfaz
def buscar():
    dato = entry.get().strip()
    if not dato:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dato para buscar.")
        return

    resultado = buscar_en_archivo(dato)  # Llama a la función correcta
    if resultado:
        # Crear una ventana para mostrar los resultados
        ventana_resultados = CTkToplevel()
        ventana_resultados.title("Resultados")
        ventana_resultados.geometry("600x400")
        texto_resultados = CTkTextbox(ventana_resultados, width=500, height=300)
        texto_resultados.pack(pady=10)
        texto_resultados.insert("1.0", resultado)
        texto_resultados.configure(state="disabled")  # Hacer el Textbox de solo lectura
    else:
        # Mostrar una ventana de error
        messagebox.showerror("Error", f"No se encontró información para: {dato}")

# Configuración de la interfaz principal
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
