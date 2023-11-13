'''En este modulo crearemos 3 hilos para que puedan ejecutar diferentes tareas
evitando que exista alguna corrupcion entre ellos
Tendremos un hilo para los modulos
main
panel_usuario
voz_artificial'''

import threading
import queue
import time

# Suponiendo que estas son las funciones definidas en tus módulos
from panel_usuario import actualizar_graficas
from voz_artificial import artificial_voice
from recomendaciones import generar_recomendacion

# Colas seguras para hilos
lecturas_iuv = queue.Queue()
categorias = queue.Queue()

def recibir_datos():
    # Esta función debería ser llamada por el callback de MQTT cuando llega un nuevo mensaje
    # Supongamos que la lectura y categoría se reciben de alguna manera
    nueva_lectura_iuv, nueva_categoria = obtener_nuevos_datos()
    lecturas_iuv.put(nueva_lectura_iuv)
    categorias.put(nueva_categoria)

def proceso_calculos():
    while True:
        # Esperar por una nueva lectura y categoría
        lectura_iuv = lecturas_iuv.get()
        categoria = categorias.get()
        
        # Realizar cálculos y actualizar gráficas
        actualizar_graficas(lectura_iuv)
        # Asegúrate de manejar las excepciones y la sincronización adecuadamente

def proceso_voz_artificial():
    while True:
        # Esperar por una nueva lectura y categoría
        lectura_iuv = lecturas_iuv.get()
        categoria = categorias.get()
        
        # Generar recomendación y reproducir voz
        recomendacion = generar_recomendacion(lectura_iuv, categoria)
        artificial_voice(recomendacion)
        # Manejo adecuado de errores y sincronización

# Crear hilos
hilo_calculos = threading.Thread(target=proceso_calculos)
hilo_voz_artificial = threading.Thread(target=proceso_voz_artificial)

# Iniciar hilos
hilo_calculos.start()
hilo_voz_artificial.start()

# Asegúrate de tener una lógica para terminar los hilos adecuadamente cuando sea necesario.
