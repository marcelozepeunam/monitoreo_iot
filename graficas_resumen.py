#!Pendiente

'''En este modulo se realizaran 2 funciones
   La primera funcion mostrará las graficas de las 
   lecturas con una grafica de barras (x:horas, y:IUV), 
   mientras que la segunda funcion, mostrará un resumen del:
   promedio, iuv_max, iuv_min, hora de iuv max
   hora de iuv min'''




import matplotlib.pyplot as plt
import numpy as np

def grafica_barras():
    # Datos para la gráfica de barras
    horarios = ["08:00", "10:00", "12:00", "14:00", "16:00"] * 12
    iuv = [1,2,2,3,1] * 12

    print("Elementos de horarios: ", len(horarios))
    print("Elementos de iuv: ", len(iuv))

    # Generar índices numéricos para el eje x usando np.arange()
    indices = np.arange(len(horarios))

    # Crear la gráfica de barras
    plt.bar(indices, iuv, color='blue')

    # Agregar etiquetas y título
    plt.xticks(indices, horarios, rotation=45)
    plt.xlabel("Horarios de lectura")
    plt.ylabel("Índices ultravioletas")
    plt.title("Índice Ultravioleta por Horario")

    # Mostrar la gráfica
    plt.show()




def grafica_pastel():
    # Datos de ejemplo para la gráfica de pastel
    iuv_promedio = 7.5
    iuv_minima = 4
    iuv_maxima = 9
    iuv_moda = 9

    # Crear la gráfica de pastel
    etiquetas = ["IUV PROMEDIO", "IUV MINIMA", "IUV MAXIMA", "IUV MODA"]
    valores = [iuv_promedio, iuv_minima, iuv_maxima, iuv_moda]
    colores = ['yellowgreen', 'lightcoral', 'lightskyblue', 'yellow']  # Amarillo para IUV MODA

    plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=140)

    # Agregar título
    plt.title("Índice Ultravioleta\n\n")

    # Ajustar el aspecto del círculo para que se vea como pastel y no elipse
    plt.axis('equal')

    # Mostrar la gráfica
    plt.show()



# Llamar a las funciones para generar las gráficas
grafica_barras()
grafica_pastel()





