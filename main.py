'''Notas 
Para activar el entorno virtual:
1- tesis_env\Scripts\activate

IMPORTANTE AGREGAR EL COMANDO PARA QUE AL ENCENDER RASPBERRY
    SE EJECUTE EL SCRIPT, VER EL SIGUIENTE VIDEO: 
    https://www.youtube.com/watch?v=_aUXG5d2YLY&list=PLxws6VhyQsd0HPBAuLx910MJJ7bC9MMp2&index=11&ab_channel=inobotica
    
    Para acceder al README En la parte superior derecha del archivo "README.md", veremos un icono 
    llamado "Open Preview" (Abrir Vista Previa). Haz clic en él para ver cómo se verá el README 
    formateado.'''


#Modulo main 

# LIBRERIAS
import datetime
import time 
import os
import statistics
#import paho.mqtt.client as mqtt

import graficas_resumen
import matplotlib.pyplot as plt

import queue
import threading #Libreria para utilizar hilos 
from voz_artificial import genera_voz_artificial
from recomendaciones import recomendacion
import panel_usuario
from threading import Thread
from time import strftime


# !Libreria de prueba
#import random

# VARIABLES Y CONSTANTES   
volver_inicio = True 
lecturas = 0 # Comienza desde 0 lecturas
total_lecturas = 2 # Total de  30 lecturas
errores_de_lectura = 0 # Comienza desde 0 errores
pausa_entre_procesos = 60 # 1 seg
pausa_error = 10 # 30 seg
pausa_resumen = 10 # 30 seg


#Creando instancia de la cola 
data_queue = queue.Queue()

# Colecciones vacías para almacenar información
lecturas_registradas = []
categorias_registradas = []
horas_registradas = []
fechas_registradas = []


# FUNCIONES
# Función para determinar fecha 
def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d / %m / %Y")
    return fecha_formateada

# Función para determinar el tiempo
def hora_actual():
    print(strftime("%H:%M:%S"))
    time.sleep(1)

# Función que define la categoría
def define_categoria(lectura_iuv):
    global categoria
    if lectura_iuv <= 2:
        categoria = "BAJO"
    elif lectura_iuv >= 3 and lectura_iuv <= 5:
        categoria = "MODERADO"
    elif lectura_iuv >= 6 and lectura_iuv <= 7:
        categoria = "ALTO"
    elif lectura_iuv >= 8 and lectura_iuv <= 10:
        categoria = "MUY ALTO"
    elif lectura_iuv >= 11:
        categoria = "EXTREMO"

# Función que agrega datos a sus respectivas listas
def agregando_a_coleccion(lectura_iuv, categoria):
    fecha = obtener_fecha_actual()  # Llama a la función para obtener la fecha
    hora = strftime("%H:%M:%S")  # Obtiene la hora actual

    lecturas_registradas.append(lectura_iuv)
    categorias_registradas.append(categoria)
    horas_registradas.append(hora)
    fechas_registradas.append(fecha)

# Función que procesa resumen
def muestra_resumen():
    global lectura_min
    global lectura_max
    global lecturas_prom
    global lectura_moda
    
    lectura_max = max(lecturas_registradas)
    lectura_min = min(lecturas_registradas)
    lecturas_prom = sum(lecturas_registradas) / len(lecturas_registradas)
    lectura_moda = statistics.mode(lecturas_registradas)

#!Funcion del programa principal con hilos (panel_usuario y voz_artificial)
def main():

    global lecturas

    # Hilo dedicado para panel_usuario 
    hilo_panel_usuario = threading.Thread(target=panel_usuario.iniciar_interfaz_usuario, args=(data_queue,))
    hilo_panel_usuario.start()

    # Hilo dedicado para voz_artificial
    hilo_voz_artificial = threading.Thread(target=genera_voz_artificial, args=(data_queue,))
    hilo_voz_artificial.start()


    volver_inicio = True

    # Filtro 1 - Número de lecturas no mayor a 30
    while lecturas <= total_lecturas-1:
        lecturas += 1 

        #!Codigo de prueba (simula lecturas)
        # Generar un nuevo valor para lectura_iuv
        #lectura_iuv = random.randint(1, 13)


        # Filtro 2 - Lectura IUV dentro del rango [1-13 IUV]
        if 1 <= lectura_iuv <= 13:
            
            define_categoria(lectura_iuv)
            recomendacion_texto = recomendacion(lectura_iuv, categoria) 
            data_queue.put(recomendacion_texto) 
            
            obtener_fecha_actual()
            agregando_a_coleccion(lectura_iuv, categoria)  # Solo dos argumentos
            data_queue.put((lectura_iuv, categoria))

            # Imprimir los valores registrados en este paso
            print([lectura_iuv, categoria, horas_registradas[-1], fechas_registradas[-1]])

            # Realizamos una espera
            time.sleep(pausa_entre_procesos)

        else: 
            # En caso de que no 
            errores_de_lectura += 1

            if errores_de_lectura == 3: 
                # Invocamos módulo de fallas técnicas
                from fallas_tecnicas import fallas_tecnicas
                time.sleep(pausa_error)
                break 

            else: 
                # En caso de que no, regresa al programa principal
                time.sleep(pausa_entre_procesos)
                volver_inicio=True


        if lecturas >= total_lecturas:
            muestra_resumen()  

            #!Error en las graficas, ya que no cierran automaticamente 
            #Incova a grafica de barras
            graficas_resumen.grafica_barras(horas_registradas, lecturas_registradas)
            plt.pause(pausa_entre_procesos)  
            plt.close('all')

            #Invoca a grafica de pastel
            graficas_resumen.grafica_pastel(lecturas_prom, lectura_min, lectura_max, lectura_moda)
            plt.pause(pausa_entre_procesos) 
            plt.close('all')


    # Esperar a que los hilos terminen
    hilo_panel_usuario.join()
    hilo_voz_artificial.join()

if __name__ == "__main__":
    main()











