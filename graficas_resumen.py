#!Pendiente

'''En este modulo se realizaran 2 funciones
   La primera funcion mostrará las graficas de las 
   lecturas con una grafica de barras (x:horas, y:IUV), 
   mientras que la segunda funcion, mostrará un resumen del:
   promedio, iuv_max, iuv_min, hora de iuv max
   hora de iuv min'''

#!Este modulo aún contiene 1 error:
#Al mostrar las graficas de resumen no se cierra la ventana automaticamente 



import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import time


def maximizar_ventana():
    mng = plt.get_current_fig_manager()
    if 'TkAgg' in matplotlib.get_backend():
        mng.window.state('zoomed')  # Para Tkinter
    # Aquí puedes agregar condiciones para otros backends si es necesario

def grafica_barras(horas_registradas, lecturas_registradas):
    # Crear la gráfica de barras utilizando horas_registrados y lecturas_registradas
    plt.figure(figsize=(19.2, 10.8))
    indices = np.arange(len(horas_registradas))
    plt.bar(indices, lecturas_registradas, color='blue')
    plt.xticks(indices, horas_registradas, rotation=45)
    plt.xlabel("Horarios de lectura")
    plt.ylabel("Índices ultravioletas")
    plt.title("Índice Ultravioleta por Horario")
    maximizar_ventana()
    plt.show()
  

def grafica_pastel(iuv_promedio, iuv_minima, iuv_maxima, iuv_moda):
    # Crear la gráfica de pastel utilizando los valores proporcionados
    plt.figure(figsize=(19.2, 10.8))
    etiquetas = ["IUV PROMEDIO", "IUV MINIMA", "IUV MAXIMA", "IUV MODA"]
    valores = [iuv_promedio, iuv_minima, iuv_maxima, iuv_moda]
    colores = ['yellowgreen', 'lightcoral', 'lightskyblue', 'yellow']
    plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=140)
    plt.title("Índice Ultravioleta")
    plt.axis('equal')
    maximizar_ventana()
    plt.show()

#?Ejemplo de uso
# grafica_barras()
# grafica_pastel()
