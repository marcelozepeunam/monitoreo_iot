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

'''Errores'''

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

#LIBRERIAS
import datetime
import time 
import os
import statistics
#import paho.mqtt.client as mqtt
from time import strftime

#!Libreria de prueba
import random


#VARIABLES Y CONSTANTES   
num_lecturas = 0 #30 lecturas maximo
errores_de_lectura = 0
volver_inicio = True 
pausa_entre_procesos = 1 #1 seg
pausa_error = 1 #30 seg
pausa_resumen = 1 #30 seg


#FUNCIONES
#!Funcion para simular valores de lectura_iuv 
def lecturas_simulada():
    lectura_iuv = random.randint(1, 13)
    return lectura_iuv

# Ejemplo de uso
lectura_iuv_simulada = lecturas_simulada()
print("Lectura IUV simulada:", lectura_iuv_simulada)
#Funcion para determinar fecha 
def fecha_actual():
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d / %m / %Y")
    return fecha_formateada
fecha_actual = fecha_actual()


#Funcion para determinar el tiempo
def hora_actual():
    print(strftime("%H:%M:%S"))
    time.sleep(1)
    hora_actual()


#Función para invocar la funcion que recibe lectura desde el ESP32 por MQTT 
def recibe_lectura_esp32(lectura_iuv):
    return lectura_iuv


#Función que define la categoria
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


#Funcion que agrega datos a sus respectivas listas
def agregando_a_coleccion():
    lecturas_registradas=[]
    categorias_registradas=[]
    horas_registrados=[]
    errores_registrados=[]


#Función que procesa resumen
def muestra_resumen():
    global lectura_min
    global lectura_max
    global lecturas_prom
    global lectura_moda
    
    lectura_max = max(lecturas_registradas)
    lectura_min = min(lecturas_registradas)
    lecturas_prom = sum(lecturas_registradas) / len(lecturas_registradas)
    lectura_moda = statistics.mode(lecturas_registradas)


# #?Código principal
# lecturas_registradas=[]
# categorias_registradas=[]
# horas_registrados=[]
# errores_registrados=[]



# #!INICIO
# volver_inicio=True

# #Filtro 1- Numero de lecturas no mayor a 30
# while num_lecturas<=30:
#     num_lecturas+=1 

#     #Filtro 2- Lectura IUV dentro del rango [1-13 IUV]
#     if 0>lectura_iuv<13:
        
#         #Capturamos el valor IUV almacenandolo en una lista 
#         lecturas_registradas.append(lectura_iuv)
#         #Realizamos una espera
#         time.sleep (pausa_entre_procesos)

#     else: #En caso de que no 
#         errores_de_lectura+=1

#         if errores_de_lectura==3: #En caso de que si
#             #Invocamos modulo de fallas tecnicas
#             from fallas_tecnicas import fallas_tecnicas
#             time.sleep(pausa_error)
#             break 

#         else: #En caso de que no, regresa al programa principal
#             volver_inicio=True


# #Si se completo las 30 lecturas se mostrara el resumen obtenido 
# from graficas_resumen import grafica_barras
# time.sleep(pausa_resumen)
# from graficas_resumen import grafica_pastel
# time.sleep(pausa_resumen)















#?Código de prueba
lecturas_registradas = []
categorias_registradas = []
horas_registrados = []
errores_registrados = []

#INICIO
volver_inicio = True

# Filtro 1 - Número de lecturas no mayor a 30
while num_lecturas <= 30:
    num_lecturas += 1

    # Genera una nueva lectura IUV simulada
    lectura_iuv = lecturas_simulada()

    # Filtro 2 - Lectura IUV dentro del rango [1-13 IUV]
    if 0 < lectura_iuv < 13:
        # Capturamos el valor IUV almacenándolo en una lista 
        lecturas_registradas.append(lectura_iuv)
        # Realizamos una espera
        time.sleep(pausa_entre_procesos)
    else: 
        # En caso de que no 
        errores_de_lectura += 1

        if errores_de_lectura == 3: 
            # Invocamos módulo de fallas técnicas
            from fallas_tecnicas import fallas_tecnicas
            fallas_tecnicas()  # Asegúrate de llamar a la función aquí
            time.sleep(pausa_error)
            break 
        else: 
            # En caso de que no, regresa al programa principal
            volver_inicio = True

# Si se completaron las 30 lecturas se mostrará el resumen obtenido 
from graficas_resumen import grafica_barras, grafica_pastel
grafica_barras()  # Asegúrate de que estas funciones acepten los datos como argumentos o los manejen internamente
grafica_pastel()
