import datetime
import locale

try:
    locale.setlocale(locale.LC_ALL, "es_MX")
except locale.Error:
    print("Advertencia: no se pudo establecer el locale 'es_MX'.")

Nom = input("¡Hola!, ingresa tu nombre: ").strip()
print(f"¡Hola! {Nom}, te doy la bienvenida a este gestor de tareas que te ayudará a mejorar el uso de tu tiempo")
print("A continuación se desplegará un menú para que puedas gestionar tus tareas")

Nuevas_tareas = []

def mostrar_tareas():
    if not Nuevas_tareas:
        print("No hay tareas disponibles.")
    else:
        print(f"Tareas actuales de {Nom}:")
        for i, tarea in enumerate(Nuevas_tareas):
            nombre, vencimiento, descripcion = tarea
            vencimiento_str = vencimiento.strftime("%d/%m/%Y") if vencimiento else "No asignado"
            descripcion_str = descripcion if descripcion else "No asignada"
            print(f"{i}. {nombre} - Vencimiento: {vencimiento_str} - Descripción: {descripcion_str}")

MenuGestor = int(input("Gestor de tareas \n1.- Nueva tarea \n2.- Eliminar tarea \n3.- Modificar tarea \n4.- Salir \n"))

while MenuGestor != 4:
    if MenuGestor == 1:
        NewTask = input(f"{Nom}, asigna un nombre a la nueva tarea: ").strip()
        if NewTask:
            tarea = (NewTask, None, None)
            Nuevas_tareas.append(tarea)
            print(f"Tarea '{NewTask}' agregada.")
        else:
            print(f"{Nom}, el nombre de la tarea no puede estar vacío.")
    
    elif MenuGestor == 2:
        if not Nuevas_tareas:
            print("Error: no hay tareas para eliminar.")
        else:
            mostrar_tareas()
            try:
                i = int(input("Ingresa el número de la tarea que quieres borrar: "))
                if 0 <= i < len(Nuevas_tareas):
                    tarea_eliminada = Nuevas_tareas.pop(i)
                    print(f"Tarea eliminada: {tarea_eliminada[0]}")
                else:
                    print("Número de tarea inválido.")
            except ValueError:
                print("Entrada inválida. Ingresa un número sin decimales.")
    
    elif MenuGestor == 3:
        if not Nuevas_tareas:
            print("Error: no hay tareas para modificar.")
        else:
            mostrar_tareas()
            try:
                i = int(input("Ingresa el número de la tarea que quieres modificar: "))
                if 0 <= i < len(Nuevas_tareas):
                    nombre, vencimiento, descripcion = Nuevas_tareas[i]
                    submenu = int(input("Modificar tareas \n1.- Asignar fecha de vencimiento \n2.- Añadir descripción \n3.- Cambiar nombre \n4.- Salir \n"))
                    
                    if submenu == 1:
                        while True:
                            try:
                                print(f"{Nom}, asigna una fecha de vencimiento (DD/MM/AAAA)")
                                dia = int(input("Ingresa el día de vencimiento: "))
                                mes = int(input("Ingresa el mes de vencimiento: "))
                                anio = int(input("Ingresa el año de vencimiento: "))
                                vencimiento = datetime.date(anio, mes, dia)
                                Nuevas_tareas[i] = (nombre, vencimiento, descripcion)
                                print(f"Fecha límite para '{nombre}': {vencimiento}")
                                break
                            except ValueError as e:
                                print(f"Error: {e}. Por favor, ingresa una fecha válida.")
                    
                    elif submenu == 2:
                        descripcion = input(f"Añade una descripción para '{nombre}': ")
                        Nuevas_tareas[i] = (nombre, vencimiento, descripcion)
                        print(f"Descripción añadida: {descripcion}")
                    
                    elif submenu == 3:
                        nuevo_nombre = input(f"Ingrese un nuevo nombre para la tarea '{nombre}': ").strip()
                        if nuevo_nombre:
                            Nuevas_tareas[i] = (nuevo_nombre, vencimiento, descripcion)
                            print(f"Tarea renombrada a: {nuevo_nombre}")
                        else:
                            print("El nombre de la tarea no puede estar vacío.")
                    else:
                        print("Saliendo al menú principal.")
                else:
                    print("Número de tarea inválido.")
            except ValueError:
                print("Entrada inválida. Ingresa un número sin decimales.")
    
    else:
        print("Opción no válida.")
    
    MenuGestor = int(input("Gestor de tareas \n1.- Nueva tarea \n2.- Eliminar tarea \n3.- Modificar tarea \n4.- Salir \n"))

print(f"¡Hasta luego {Nom}!")
