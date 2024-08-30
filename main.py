import datetime
import queue
import logging 
import threading
from time import strftime
from recibe_lecturas import iniciar_servidor_mqtt
from panel_usuario import iniciar_interfaz_usuario
from recomendaciones import recomendacion
from voz_artificial import genera_voz_artificial

volver_inicio = True 
lecturas = 0                # Comienza desde 0 lecturas
total_lecturas = 5          # Total de  30 lecturas
errores_de_lectura = 0      # Comienza desde 0 errores
pausa_entre_procesos = 120   # 1 seg
pausa_error = 10            # 30 seg
pausa_resumen = 10          # 30 seg


#Creando instancia de la cola 
data_queue = queue.Queue()
ui_queue = queue.Queue()
voz_queue = queue.Queue()

lecturas_registradas = []
categorias_registradas = []
horas_registradas = []
fechas_registradas = []

logging.basicConfig(
    filename='main.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d / %m / %Y")
    return fecha_formateada

def agregando_a_coleccion(lectura_iuv, categoria):
    fecha = obtener_fecha_actual()
    hora = strftime("%H:%M:%S")

    lecturas_registradas.append(lectura_iuv)
    categorias_registradas.append(categoria)
    horas_registradas.append(hora)
    fechas_registradas.append(fecha)

def limpiar_cola(data_queue):
    with data_queue.mutex:
        data_queue.queue.clear()

def main():
    print("Inicio de la aplicación")

    hilo_servidor_mqtt = threading.Thread(target=iniciar_servidor_mqtt, args=(data_queue,))
    hilo_panel_usuario = threading.Thread(target=iniciar_interfaz_usuario, args=(ui_queue,))
    hilo_voz_artificial = threading.Thread(target=genera_voz_artificial, args=(voz_queue,))

    hilo_servidor_mqtt.start()
    hilo_panel_usuario.start()
    hilo_voz_artificial.start()

    global lecturas, errores_de_lectura

    while lecturas < total_lecturas:
        lecturas_registradas.clear()
        categorias_registradas.clear()
        horas_registradas.clear()
        fechas_registradas.clear()
        
        try:
            lectura_iuv, categoria = data_queue.get(timeout=pausa_entre_procesos)
            print(f"Lectura UV y categoría consumidas de data_queue: {lectura_iuv}, {categoria}")

            recomendacion_texto = recomendacion(lectura_iuv, categoria)
            print(f"Recomendación generada: {recomendacion_texto}")

            agregando_a_coleccion(lectura_iuv, categoria)

            ui_queue.put((lectura_iuv, categoria))
            voz_queue.put(recomendacion_texto)

            lecturas += 1

        except queue.Empty:
            print("timeout")
            errores_de_lectura += 1
            if errores_de_lectura >= 3:
                print("Error: Demasiados intentos fallidos de recibir datos.")
                break

    if lecturas >= total_lecturas:
        print("Lecturas completas con éxito")
        print("Fin del programa. Lecturas completas:", lecturas)
    
    limpiar_cola(data_queue)

    hilo_servidor_mqtt.join()
    hilo_panel_usuario.join()
    hilo_voz_artificial.join()

    print("Fin del programa. Todas las operaciones han sido completadas.") 

    
if __name__ == "__main__":
    main()
