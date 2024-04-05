
#Modulo main 

'''# LIBRERIAS
import datetime
import time 
import os
import statistics
import paho.mqtt.client as mqtt
import queue
import threading #Libreria para utilizar hilos 
from recibe_lecturas import iniciar_servidor_mqtt, define_categoria
from voz_artificial import genera_voz_artificial #Hilo 1
from recomendaciones import recomendacion #Hilo 2
import panel_usuario
from threading import Thread
from time import strftime



#? VARIABLES Y CONSTANTES REALES
#volver_inicio = True 
#lecturas = 0               # Comienza desde 0 lecturas
#total_lecturas = 10        # 10 lecturas
#errores_de_lectura = 0     # Comienza desde 0 errores
#pausa_entre_procesos = 60  # 1 minuto
#pausa_error = 3            # 3 seg
#pausa_resumen = 60         # 60 seg

#VARIABLES Y CONSTANTES DE PRUEBA
volver_inicio = True 
lecturas = 0                # Comienza desde 0 lecturas
total_lecturas = 5          # Total de  30 lecturas
errores_de_lectura = 0      # Comienza desde 0 errores
pausa_entre_procesos = 120   # 1 seg
pausa_error = 10            # 30 seg
pausa_resumen = 10          # 30 seg


#Creando instancia de la cola 
data_queue = queue.Queue()

# Colecciones vacías para almacenar información
lecturas_registradas = []
categorias_registradas = []
horas_registradas = []
fechas_registradas = []


#?FUNCIONES
# Función devolver la fecha actual en formato dd/mm/aaaa.
def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d / %m / %Y")
    return fecha_formateada

# Función para imprimir la hora actual en formato HH:MM:SS
def hora_actual():
    print(strftime("%H:%M:%S"))
    time.sleep(1)


#Función que agrega datos a las colecciones de lecturas, categorías, horas y fechas registradas.
def agregando_a_coleccion(lectura_iuv, categoria):
    fecha = obtener_fecha_actual()  # Llama a la función para obtener la fecha
    hora = strftime("%H:%M:%S")  # Obtiene la hora actual

    lecturas_registradas.append(lectura_iuv)
    categorias_registradas.append(categoria)
    horas_registradas.append(hora)
    fechas_registradas.append(fecha)


lectura_iuv = 0  # Valor inicial o predeterminado


#?FUNCIÓN PRINCIPAL
#Función principal del programa que inicia los hilos y controla el flujo del programa.
def main():
    global lecturas
    global errores_de_lectura

    # Hilo dedicado para panel_usuario 
    hilo_panel_usuario = threading.Thread(target=panel_usuario.iniciar_interfaz_usuario, args=(data_queue,)) #Para que sea tupla, debo de agregar la coma al final
    hilo_panel_usuario.start()

    # Hilo dedicado para voz_artificial 
    hilo_voz_artificial = threading.Thread(target=genera_voz_artificial, args=(data_queue,)) #Para que sea tupla, debo de agregar la coma al final
    hilo_voz_artificial.start()


    volver_inicio = True

    # Filtro 1 - Número de lecturas no mayor a 0
    while lecturas <= total_lecturas-1:
        lecturas += 1 

        # Filtro 2 - Lectura IUV dentro del rango [1-13 IUV]
        if 1 <= lectura_iuv <= 13:
            
            define_categoria(lectura_iuv)
            recomendacion_texto = recomendacion(lectura_iuv, categoria) 
            data_queue.put(recomendacion_texto) 
            
            obtener_fecha_actual()
            agregando_a_coleccion(lectura_iuv, categoria)  # Solo dos argumentos
            data_queue.put((lectura_iuv, categoria))
            print("Datos enviados a la cola:", (lectura_iuv, categoria))

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
            #muestra_resumen()  
            print("Fin del programa")
            time.sleep(3)


    # Esperar a que los hilos terminen
    hilo_panel_usuario.join()
    hilo_voz_artificial.join()

if __name__ == "__main__":
    iniciar_servidor_mqtt(data_queue)
    main()'''











# Modulo main (modificado)

# LIBRERIAS
import datetime
import time
import queue
import threading
from recibe_lecturas import iniciar_servidor_mqtt  # Importa solo lo necesario
from voz_artificial import genera_voz_artificial  # Hilo 1
from recomendaciones import recomendacion  # Hilo 2
import panel_usuario
from time import strftime

# VARIABLES Y CONSTANTES DE PRUEBA
lvolver_inicio = True 
lecturas = 0                # Comienza desde 0 lecturas
total_lecturas = 5          # Total de  30 lecturas
errores_de_lectura = 0      # Comienza desde 0 errores
pausa_entre_procesos = 120   # 1 seg
pausa_error = 10            # 30 seg
pausa_resumen = 10          # 30 seg

# Creando instancia de la cola
data_queue = queue.Queue()

# Colecciones vacías para almacenar información
lecturas_registradas = []
categorias_registradas = []
horas_registradas = []
fechas_registradas = []

# FUNCIONES
def obtener_fecha_actual():
# Función devolver la fecha actual en formato dd/mm/aaaa.
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d / %m / %Y")
    return fecha_formateada

# Función para imprimir la hora actual en formato HH:MM:SS
def hora_actual():
    print(strftime("%H:%M:%S"))
    time.sleep(1)


# Función para imprimir la hora actual en formato HH:MM:SS
def agregando_a_coleccion(lectura_iuv, categoria):
    fecha = obtener_fecha_actual()
    hora = strftime("%H:%M:%S")

    lecturas_registradas.append(lectura_iuv)
    categorias_registradas.append(categoria)
    horas_registradas.append(hora)
    fechas_registradas.append(fecha)

# FUNCIÓN PRINCIPAL
def main():
    #Iniciando los hilos para el servidor MQTT, panel usuario y voz_artificial
    threading.Thread(target=iniciar_servidor_mqtt, args=(data_queue,)).start()
    threading.Thread(target=panel_usuario.iniciar_interfaz_usuario, args=(data_queue,)).start()
    threading.Thread(target=genera_voz_artificial, args=(data_queue,)).start()

    global lecturas, errores_de_lectura

    #?Logica del programa principal
    volver_inicio = True

    while lecturas < total_lecturas:
        try:
            # Espera por una nueva lectura y su categoría de data_queue
            lectura_iuv, categoria = data_queue.get(timeout=pausa_entre_procesos)
            print("Lectura UV y categoría consumidas de data_queue:", lectura_iuv, categoria)
            
            # Aquí deberías generar recomendaciones o realizar otras acciones con los datos
            recomendacion_texto = recomendacion(lectura_iuv, categoria)
            print("Recomendación generada:", recomendacion_texto)
            
            # Agregar datos a las colecciones para un posterior resumen o análisis
            agregando_a_coleccion(lectura_iuv, categoria)

            lecturas += 1  # Incrementa el contador de lecturas procesadas

        except queue.Empty:
            # En caso de timeout (no se reciben datos en el tiempo esperado)
            print("Timeout: No se recibieron datos")
            errores_de_lectura += 1
            if errores_de_lectura >= 3:
                # Manejo de errores repetidos, podría incluir mostrar fallas técnicas o reintentar la conexión
                print("Error: Demasiados intentos fallidos de recibir datos.")
                break

    if lecturas >= total_lecturas:
        # Aquí podrías mostrar un resumen de las lecturas y categorías procesadas
        print("Fin del programa. Lecturas completas:", lecturas)
    
    
    # Espera a que los hilos terminen (opcional, dependiendo de tu lógica específica)
    hilo_panel_usuario.join()
    hilo_voz_artificial.join()

if __name__ == "__main__":
    main()