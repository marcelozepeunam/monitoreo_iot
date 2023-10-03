'''Este modulo desarrollado en tkinter muestra en tiempo real con una actualizacion 
de 60 segundos la lectura proporcionada por el sensor y con base a esa lectura
obtiene la categoria (el color de la categoria dependera del rango de categoria en el
que se encuentre), finalmente muestra en la interfaz grafica datos como:
Hora, Fecha, IUV, Categoria.
Se utilizara programación concurrente (por hilos) para ejecutar este modulo y el 
modulo main al mismo tiempo'''


import threading
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime
#from main import lectura_iuv, categoria


#?Ejemplo de uso (modificar con lexturas reales)
lectura_iuv=2
categoria="BAJA"

app = tk.Tk()
app.geometry("1920x1080")
app.title("RELOJ DIGITAL")


# Función que actualiza el reloj
def actualiza_reloj():
    etiqueta_hm.config(text=strftime("%H:%M"))
    etiqueta_s.config(text=strftime("%S"))
    etiqueta_fecha.config(text=strftime("%A, %d / %m / %Y"))
    etiqueta_s.after(1000, actualiza_reloj)

    # Llamamos a la función Color_categoria con el valor de ejemplo "10"
    color_lectura_iuv = Color_categoria(lectura_iuv)
    etiqueta_lectura.config(foreground=color_lectura_iuv, text=f"{lectura_iuv} IUV: {categoria}")

# Función que devuelve el color de acuerdo al valor de lectura_iuv
def Color_categoria(valor):
    # Define las categorías en función del valor
    if valor <= 2:
        return "green"
    elif 3 <= valor <= 5:  # Aquí corregí la estructura para tomar en cuenta el rango de valores
        return "yellow"
    elif 6 <= valor <= 7:
        return "orange"
    elif 8 <= valor <= 10:
        return "red"
    elif valor >= 11:
        return "purple"
    else:
        return "grey"  # Es bueno tener un valor por defecto en caso de que el valor no entre en ninguna de las categorías anteriores


# Etiqueta para la Horas-Minutos
frame_hora = Frame()
frame_hora.pack()
etiqueta_hm = Label(frame_hora, font=("digitalk", 150), text=("H:M"))
etiqueta_hm.grid(row=0, column=0)

# Etiqueta para los Segundos
etiqueta_s = Label(frame_hora, font=("digitalk", 100), text="s")
etiqueta_s.grid(row=0, column=1, sticky="n")

#!Posicionar estas 2 etiquetas más abajo 
# Etiqueta para la fecha
etiqueta_fecha = Label(font=("digitalk", 90), text="dia dd/mm/aaaa")
etiqueta_fecha.pack(anchor="center")


# Etiqueta de lectura de lectura
etiqueta_lectura = Label(app, font=("digitalk", 90), text=f"{lectura_iuv} IUV: {categoria}")
etiqueta_lectura.pack(anchor="s")

#Invocamos la funcion
actualiza_reloj()
app.mainloop()