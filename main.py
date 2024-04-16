
# Modulo main (main thread)

# LIBRERIAS
import datetime
import time
import queue
import logging #Debug (10), Info (20), Warning (30), Error(40), Critical(50)
import threading
from recibe_lecturas import iniciar_servidor_mqtt # Importa solo lo necesario
from voz_artificial import genera_voz_artificial  # Hilo 1
from recomendaciones import recomendacion         # Hilo 2
import panel_usuario
from time import strftime

# VARIABLES Y CONSTANTES DE PRUEBA
volver_inicio = True 
lecturas = 0                # Comienza desde 0 lecturas
total_lecturas = 5          # Total de  30 lecturas
errores_de_lectura = 0      # Comienza desde 0 errores
pausa_entre_procesos = 120  # 1 seg
pausa_error = 10            # 30 seg
pausa_resumen = 10          # 30 seg

# Creando instancia de la cola
data_queue = queue.Queue()

# Colecciones vacías para almacenar información
lecturas_registradas = []
categorias_registradas = []
horas_registradas = []
fechas_registradas = []

# Configuración del formato de logging 
logging.basicConfig(filename='main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


# FUNCIONES

# Función devolver la fecha actual en formato dd/mm/aaaa.
def obtener_fecha_actual():
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
    logging.info("Inicio de la aplicación") #?Logging info 


    #Creando los hilos
    # Creando los hilos
    hilo_servidor_mqtt = threading.Thread(target=iniciar_servidor_mqtt, args=(data_queue,))
    hilo_servidor_mqtt = threading.Thread(target=iniciar_servidor_mqtt, args=(data_queue,))
    hilo_panel_usuario = threading.Thread(target=panel_usuario.iniciar_interfaz_usuario, args=(data_queue,))
    hilo_voz_artificial = threading.Thread(target=genera_voz_artificial, args=(data_queue,))
    

    #Iniciando los hilos
    hilo_servidor_mqtt.start()
    logging.info("El hilo para el servidor MQTT ha sido iniciado.") #?Logging info 
    hilo_panel_usuario.start()
    logging.info("El hilo para el panel de usuario ha sido iniciado.") #?Logging info 
    hilo_voz_artificial.start()
    logging.info("El hilo para la voz artificial ha sido iniciado.") #?Logging info 

    global lecturas, errores_de_lectura

    #?Logica del programa principal
    volver_inicio = True

    while lecturas < total_lecturas:
        try:
            # Espera por una nueva lectura y su categoría de data_queue
            lectura_iuv, categoria = data_queue.get(timeout=pausa_entre_procesos)
            logging.info(f"Lectura UV y categoría consumidas de data_queue: {lectura_iuv}, {categoria}")  #?Logging info
            
            # Aquí deberías generar recomendaciones o realizar otras acciones con los datos
            recomendacion_texto = recomendacion(lectura_iuv, categoria)
            logging.info(f"Recomendación generada: {recomendacion_texto}")
            
            # Agregar datos a las colecciones para un posterior resumen o análisis
            agregando_a_coleccion(lectura_iuv, categoria)

            lecturas += 1  # Incrementa el contador de lecturas procesadas

        except queue.Empty:
            # En caso de timeout (no se reciben datos en el tiempo esperado)
            logging.warning(f"Timeout: No se recibieron datos después de {pausa_entre_procesos} segundos. Intentos fallidos: {errores_de_lectura}. Total de lecturas procesadas: {lecturas}.") #?Logging info
            
            errores_de_lectura += 1
            if errores_de_lectura >= 3:
                # Manejo de errores repetidos, podría incluir mostrar fallas técnicas o reintentar la conexión
                logging.warning("Error: Demasiados intentos fallidos de recibir datos.")
                break

    if lecturas >= total_lecturas:
        # Aquí podrías mostrar un resumen de las lecturas y categorías procesadas
        logging.info("Lecturas completas con éxito") #?Logging info
        print("Fin del programa. Lecturas completas:", lecturas)
        

    # Espera a que los hilos terminen 
    hilo_servidor_mqtt.join()
    hilo_panel_usuario.join()
    hilo_voz_artificial.join()

    #Logging para el fin del programa main
    logging.info("Fin del programa. Todas las operaciones han sido completadas.") #?Logging info

if __name__ == "__main__":
    main()