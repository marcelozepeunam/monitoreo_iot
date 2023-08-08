'''Pendientes:
0- Falta agregar correctamente la funcion que registre las lecturas 
   en excel o el excel de ubuntu
1- Falta crear una función que realice la conexión entre el resumen 
   y BD
2- Configurar gestor de BD 
3- Programar el envío de datos a BD
4- Implementar Docker en nuestro código
5- Implementar docker '''

'''Notas 
Para activar el entorno virtual:
1- tesis_env\Scripts\activate

IMPORTANTE AGREGAR EL COMANDO PARA QUE AL ENCENDER RASPBERRY
    SE EJECUTE EL SCRIPT, VER EL SIGUIENTE VIDEO: 
    https://www.youtube.com/watch?v=_aUXG5d2YLY&list=PLxws6VhyQsd0HPBAuLx910MJJ7bC9MMp2&index=11&ab_channel=inobotica'''

'''Errores
1- Me falta agregar un contador a num_lecturas
2- Hay que solucionar el error en el modulo de graficas de matplotlib
3- Hay que agregar los valores a las graficas '''

'''Readme 
Este programa consiste en recibir las lecturas por medio del MQTT cada 30 segundos 
dentro del programa en cada ciclo debe de guardar hora y la lectura correspondiente
finalmente debe de almacenar en una lista las lecturas y horas recolectadas '''

#LIBRERIAS
import time 
import os
import statistics
import paho.mqtt.client as mqtt

import random


#VARIABLES Y CONSTANTES   
num_lecturas = 60 #60 seg
errores_de_lectura = 0
volver_inicio = True 
pausa_entre_procesos = 1 #1 seg
pausa_error = 1 #1 seg
pausa_resumen = 1 #1 seg


#FUNCIONES
#!Esta funcion debe de ser sustituida por el modulo recibe_datos.py
#Esta funcion debe de recibir la lectura iuv del sensor 
def recibe_lectura_esp32(lectura_iuv):
    #!Esta parte es de prueba
    for i in range (1,60):
        lectura_iuv = random.randint(1, 5)
        print(lectura_iuv)
        time.sleep(pausa_entre_procesos)
    return lectura_iuv
    


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


#Esta funcion debe de adquirir los datos al finalizar todas las lecturas
def muestra_resumen():
    global lectura_min
    global lectura_max
    global lecturas_prom
    global lectura_moda
    
    lectura_max = max(lecturas)
    lectura_min = min(lecturas)
    lecturas_prom = sum(lecturas) / len(lecturas)
    lectura_moda = statistics.mode(lecturas)


#Código principal
lecturas=[]

#!Creo que aqui hay error en el ciclo while 
volver_inicio=True

while num_lecturas<=60:
    
    #Filtro 1- 0>lectura_iuv<=13
    if 0>lectura_iuv<=13: #En caso de que si 
        
        #Filtro 2- num_lecturas<=60
        if num_lecturas<=60:
            #Agregamos lectura lista
            lecturas.append(lectura_iuv)
            #Agregamos un contador al numero de lecturas
            num_lecturas+=1
            #Realizamos una espera
            time.sleep (pausa_entre_procesos)

        else:
            from graficas_resumen import grafica_barras
            time.sleep(pausa_resumen)
            from graficas_resumen import grafica_pastel
            time.sleep(pausa_resumen)
            break


    
    else: #En caso de que no 
        errores_de_lectura+=1

        if errores_de_lectura==3: #En caso de que si
            #Invocamos modulo de fallas tecnicas
            from fallas_tecnicas import fallas_tecnicas
            time.sleep(pausa_error)
            break 

        else: #En caso de que no, regresa al programa principal
            volver_inicio=True


