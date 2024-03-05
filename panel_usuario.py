'''Este modulo desarrollado en tkinter muestra en tiempo real con una actualizacion 
de 60 segundos la lectura proporcionada por el sensor y con base a esa lectura
obtiene la categoria (el color de la categoria dependera del rango de categoria en el
que se encuentre), finalmente muestra en la interfaz grafica datos como:
Hora, Fecha, IUV, Categoria.
Se utilizara programación concurrente (por hilos) para ejecutar este modulo y el 
modulo main al mismo tiempo'''


#Modulo panel_usuario 


import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime


# Inicializa las variables globales con valores predeterminados
lectura_iuv = 0
categoria = "DESCONOCIDA"



def iniciar_interfaz_usuario(data_queue):

    # Funcion que actualiza las variables lectura_iuv y categoria
    def actualizar_datos_sensor(nueva_lectura, nueva_categoria):
        global lectura_iuv, categoria
        
        lectura_iuv = nueva_lectura
        categoria = nueva_categoria
        
        print("Nueva lectura IUV:", lectura_iuv) #!Borrar esta linea
        print("Nueva categoria:", categoria) #!Borrar esta linea
        actualizar_interfaz()

    # Función que actualiza la interfaz de usuario
    def actualizar_interfaz():
        color_lectura_iuv = Color_categoria(lectura_iuv)
        etiqueta_lectura.config(foreground=color_lectura_iuv, text=f"\n{lectura_iuv} IUV: {categoria}")

    # Función que devuelve el color de acuerdo al valor de lectura_iuv
    def Color_categoria(valor):
        if valor <= 2:
            return "green"
        elif 3 <= valor <= 5:
            return "yellow"
        elif 6 <= valor <= 7:
            return "orange"
        elif 8 <= valor <= 10:
            return "red"
        elif valor >= 11:
            return "purple"
        else:
            return "grey"

    # Función que se llama periódicamente para actualizar los datos desde la cola
    def verifica_y_actualiza():
        global lectura_iuv, categoria
        if not data_queue.empty():
            nueva_lectura, nueva_categoria = data_queue.get()
            actualizar_datos_sensor(nueva_lectura, nueva_categoria)
        app.after(1000, verifica_y_actualiza)  # Actualiza cada segundo

    app = tk.Tk()
    app.geometry("1920x1080")
    app.title("Monitoreo en tiempo real")

    # Función que actualiza el reloj
    def actualiza_reloj():
        etiqueta_hm.config(text=strftime("%H:%M"))
        etiqueta_s.config(text=strftime("%S"))
        etiqueta_fecha.config(text=strftime("%A, %d / %m / %Y"))
        etiqueta_s.after(120000, actualiza_reloj) #Actualiza pantalla cada 2 minutos

    # Etiquetas y Widgets
    frame_hora = Frame()
    frame_hora.pack()
    #etiqueta_hm = Label(frame_hora, font=("digitalk", 150), text=("H:M")) #Tamaño de letra para pantalla
    etiqueta_hm = Label(frame_hora, font=("digitalk", 80), text=("H:M"))   #Tamaño de letra para Raspberry
    etiqueta_hm.grid(row=0, column=0)

    #etiqueta_s = Label(frame_hora, font=("digitalk", 100), text="s")      #Tamaño de letra para pantalla
    etiqueta_s = Label(frame_hora, font=("digitalk", 60), text="s")        #Tamaño de letra para Raspberry
    etiqueta_s.grid(row=0, column=1, sticky="n")

    #etiqueta_fecha = Label(font=("digitalk", 80), text="dia dd/mm/aaaa")   #Tamaño de letra para pantalla
    etiqueta_fecha = Label(font=("digitalk", 40), text="dia dd/mm/aaaa")   #Tamaño de letra para Raspberry
    etiqueta_fecha.pack(anchor="center")

    etiqueta_lectura = Label(app, font=("digitalk", 60), text=f"\n{lectura_iuv} IUV: {categoria}")
    etiqueta_lectura.pack(anchor="s")

    # Inicia el reloj y la simulación de datos
    actualiza_reloj()

    #Verifica que existan datos desde la cola
    verifica_y_actualiza()

    # Inicia el bucle principal de Tkinter
    app.mainloop()








# #?Este codigo es para poder simular y comprobar el funcionamiento del programa sin lecturas reales
# import tkinter as tk
# from tkinter import *
# from tkinter.ttk import *
# from time import strftime
# import random  # Importado para simular datos aleatorios

# # Inicializa las variables globales con valores predeterminados
# lectura_iuv = 0
# categoria = "DESCONOCIDA"

# # Funcion que actualiza las variables lectura_iuv y categoria
# def actualizar_datos_sensor(nueva_lectura, nueva_categoria):
#     global lectura_iuv, categoria
#     lectura_iuv = nueva_lectura
#     categoria = nueva_categoria
#     actualizar_interfaz()

# # Función que actualiza la interfaz de usuario
# def actualizar_interfaz():
#     color_lectura_iuv = Color_categoria(lectura_iuv)
#     etiqueta_lectura.config(foreground=color_lectura_iuv, text=f"{lectura_iuv} IUV: {categoria}")

# # Función que devuelve el color de acuerdo al valor de lectura_iuv
# def Color_categoria(valor):
#     if valor <= 2:
#         return "green"
#     elif 3 <= valor <= 5:
#         return "yellow"
#     elif 6 <= valor <= 7:
#         return "orange"
#     elif 8 <= valor <= 10:
#         return "red"
#     elif valor >= 11:
#         return "purple"
#     else:
#         return "grey"

# # Configuración de la ventana principal
# app = tk.Tk()
# app.geometry("1920x1080")
# app.title("RELOJ DIGITAL")

# # Función que actualiza el reloj
# def actualiza_reloj():
#     etiqueta_hm.config(text=strftime("%H:%M"))
#     etiqueta_s.config(text=strftime("%S"))
#     etiqueta_fecha.config(text=strftime("%A, %d / %m / %Y"))
#     etiqueta_s.after(1000, actualiza_reloj)

# # Etiquetas y Widgets
# frame_hora = Frame()
# frame_hora.pack()
# etiqueta_hm = Label(frame_hora, font=("digitalk", 150), text=("H:M"))
# etiqueta_hm.grid(row=0, column=0)

# etiqueta_s = Label(frame_hora, font=("digitalk", 100), text="s")
# etiqueta_s.grid(row=0, column=1, sticky="n")

# etiqueta_fecha = Label(font=("digitalk", 90), text="dia dd/mm/aaaa")
# etiqueta_fecha.pack(anchor="center")

# etiqueta_lectura = Label(app, font=("digitalk", 90), text=f"{lectura_iuv} IUV: {categoria}")
# etiqueta_lectura.pack(anchor="s")

# # Función para simular la recepción de nuevos datos
# def simular_datos():
#     nueva_lectura = random.uniform(0, 15)  # Genera un número aleatorio como ejemplo
#     nueva_categoria = "Simulada"  # Esto es solo un ejemplo
#     actualizar_datos_sensor(int(nueva_lectura), nueva_categoria)
#     app.after(2000, simular_datos)  # Programa para ejecutar de nuevo después de 60 segundos

# # Inicia el reloj y la simulación de datos
# actualiza_reloj()
# simular_datos()

# # Inicia el bucle principal de Tkinter
# app.mainloop()