'''Pendientes:
0- Buscar como interactuar desde raspberry sin vscode ya que es muy pesado para el dispositivo
2- Crear funcion de hora para ir agregando a lista en cada iteracion
3- Agregar a listas en cada iteracion hora, categoria, lectura'''

'''Notas 
Para activar el entorno virtual:
1- tesis_env\Scripts\activate

IMPORTANTE AGREGAR EL COMANDO PARA QUE AL ENCENDER RASPBERRY
    SE EJECUTE EL SCRIPT, VER EL SIGUIENTE VIDEO: 
    https://www.youtube.com/watch?v=_aUXG5d2YLY&list=PLxws6VhyQsd0HPBAuLx910MJJ7bC9MMp2&index=11&ab_channel=inobotica
    
    Para acceder al README En la parte superior derecha del archivo "README.md", veremos un icono 
    llamado "Open Preview" (Abrir Vista Previa). Haz clic en él para ver cómo se verá el README 
    formateado.'''

'''OBJETIVO

Este modulo consiste en orquestar tanto la comunicación como los demás modulos.
El programa se ejecutara siempre y cuando el numero de lecturas no sea mayor a 30 lecturas.
Las lecturas se tomaran cada minuto, teniendo un total de 30 lecturas en total o en otras palabras
30 minutos de monitoreo.

En este proceso de monitoreo se mostrara en todo momento el modulo panel_usuario, al mismo tiempo que 
se realizan procesos y calculos internos, además de proporcionar mediante una voz artificial con ayuda 
de IA una recomendación basada en la lectura y/o categoria que se adquiere en ese momento. 
El programa esta diseñado para tener una tolerancia de máximo 3 errores en la lectura adquirida por el
sensor (ML8511), si esto llega a suceder, el programa mostrara un mensaje (mediante interfaz grafica) y 
se suspenderá.

Por el contrario, al finalizar las 30 lecturas, el programa mostrará un resumen de los datos adquiridos
como lo son: 
-Fecha
-Horas registradas
-Lecturas registradas
-Categorias registradas
-Lectura maxima
-Lectura minima
-Lectura promedio
-Lectura moda

Finalmente después de mostrar el resumen mediante gráficas, el programa se finalizara de manera automatica
Proporcionandonos una hoja de calculo en donde se habran registrado cada monitoreo la informacion más 
relevante como lo son:
IUV | Categoría | Hora | Fecha | Errores de lectura '''




# LIBRERIAS
import datetime
import time 
import os
import statistics
#import paho.mqtt.client as mqtt
from time import strftime
import graficas_resumen
import matplotlib.pyplot as plt

# !Libreria de prueba
import random

# VARIABLES Y CONSTANTES   
volver_inicio = True 
lecturas = 0 # Comienza desde 0 lecturas
total_lecturas = 10 # Total de  30 lecturas
errores_de_lectura = 0 # Comienza desde 0 errores
pausa_entre_procesos = 3 # 1 seg
pausa_error = 1 # 30 seg
pausa_resumen = 1 # 30 seg

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

# !INICIO del código principal
volver_inicio = True

# Filtro 1 - Número de lecturas no mayor a 30
while lecturas <= total_lecturas-1:
    lecturas += 1 

    # Generar un nuevo valor para lectura_iuv
    lectura_iuv = random.randint(15, 15)

    # Filtro 2 - Lectura IUV dentro del rango [1-13 IUV]
    if 1 <= lectura_iuv <= 13:
        
        # !Agregamos valores a colecciones en cada lectura
        obtener_fecha_actual()
        define_categoria(lectura_iuv)
        agregando_a_coleccion(lectura_iuv, categoria)  # Solo dos argumentos

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
            volver_inicio=True


if lecturas >= total_lecturas:
    muestra_resumen()  

    #Incova a grafica de barras
    graficas_resumen.grafica_barras(horas_registradas, lecturas_registradas)
    plt.pause(pausa_entre_procesos)  
    plt.close('all')

    #Invoca a grafica de pastel
    graficas_resumen.grafica_pastel(lecturas_prom, lectura_min, lectura_max, lectura_moda)
    plt.pause(pausa_entre_procesos) 
    plt.close('all')


