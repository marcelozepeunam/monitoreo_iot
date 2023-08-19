'''Mejoras: 
1- Crear variables globales para las recomendaciones o mandar llamar esas
   funciones desde el archivo tesis1
1- Aplicar condicionales para:
   En función de las lecturas por medio de los sensores, las etiquetas
   lectura y alerta deben de mostrarse en cierto color
3- Al finalizar el proceso deberá mostrar las graficas a modo de reumen y después
   de unos minutos se apagara'''

'''Notas:
Para las lecturas y alertas se recomiendan los siguientes colores:
IUV Baja: color verde claro o amarillo pálido
IUV Moderada: color amarillo brillante o naranja claro
IUV Alta: color naranja oscuro o rojo claro
IUV Muy alta: color rojo intenso o morado claro
IUV Extremadamente alta: color violeta oscuro o marrón claro'''

import tkinter as tk
import threading
from tkinter import *
from tkinter.ttk import *
from time import strftime

#from main import lectura_iuv, categoria

#!Valores de prueba
valor_digital = 2
categoria = "BAJA"

#!Valores reales dados por el modulo main




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
    color_valor_digital = Color_categoria(valor_digital)
    etiqueta_lectura.config(foreground=color_valor_digital, text=f"{valor_digital} IUV: {categoria}")

# Función que devuelve el color de acuerdo al valor de valor_digital
def Color_categoria(valor):
    if valor <= 2:
        return "green"
    elif valor <= 3 or valor <= 5:
        return "#FFD700"
    elif valor <= 6 or valor <= 7:
        return "orange"
    elif valor <= 8 or valor <= 10:
        return "red"
    elif valor == 11 or 12: #!Verificar margen de error 
        return "purple"

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
etiqueta_lectura = Label(app, font=("digitalk", 90), text=f"{valor_digital} IUV: {categoria}")
etiqueta_lectura.pack(anchor="s")


#Invocamos la funcion
actualiza_reloj()
app.mainloop()