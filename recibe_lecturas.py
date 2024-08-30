#Modulo recibe_lecturas

import os
import paho.mqtt.client as mqtt
import logging
from dotenv import load_dotenv

#Cargando la variable (MQTT_SERVER_IP) desde .env
load_dotenv()  
mqtt_broker = os.getenv("MQTT_SERVER_IP")  

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Nuevo: Agregar logging en el evento de conexión
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Conexión MQTT establecida exitosamente.") #?Logging info
    else:
        logging.error(f"Fallo en la conexión MQTT, código de retorno {rc}.") #?Logging error

def on_message(client, userdata, message, data_queue):
    logging.info(f"Mensaje recibido en topic: {message.topic}") #?Logging info
    try:
        lectura_iuv = float(message.payload.decode("utf-8"))
        logging.info(f"Payload del mensaje: {message.payload}") #?Logging info

        # Definiendo la categoria dependiendo del valor IUV
        if lectura_iuv <= 2:
            categoria = "BAJO"
        elif 3 <= lectura_iuv <= 5:
            categoria = "MODERADO"
        elif 6 <= lectura_iuv <= 7:
            categoria = "ALTO"
        elif 8 <= lectura_iuv <= 10:
            categoria = "MUY ALTO"
        elif lectura_iuv >= 11:
            categoria = "EXTREMO"
        else:
            categoria = "DESCONOCIDA"
        
        # Agrega lectura_iuv y categoria en la cola (data_queue)
        data_queue.put((lectura_iuv, categoria))

    except ValueError:
        logging.warning("No se recibió lectura válida") #?Logging warning
    except Exception as e:
        logging.error(f"Error inesperado: {e}") #?Logging error

def iniciar_servidor_mqtt(data_queue):
    load_dotenv()

    logging.info("Inicializando conexión MQTT...")  #?Logging info
    mqtt_broker = os.getenv("MQTT_SERVER_IP")  # Obtener la IP desde variable desde .env
    if not mqtt_broker:
        logging.error("La dirección IP del servidor MQTT no está configurada. Defina MQTT_SERVER_IP en el archivo .env.") #?Logging error
        raise ValueError("La dirección IP del servidor MQTT no está configurada.")
    mqtt_port = 1883
    mqtt_client = mqtt.Client()

    # Asigna la función on_connect al cliente MQTT
    mqtt_client.on_connect = on_connect

    # Inicia la conexión y suscripción al topic "lectura_iuv"
    logging.info(f"Conectando al broker MQTT en {mqtt_broker}:{mqtt_port}") #?Logging info
    mqtt_client.connect(mqtt_broker, mqtt_port)

    # Suscripción al tópico
    mqtt_client.subscribe("lectura_iuv")
    logging.info(f"Suscrito exitosamente al tópico 'lectura_iuv'") #?Logging info

    # Callback
    mqtt_client.on_message = lambda client, userdata, message: on_message(client, userdata, message, data_queue, )

    # Inicia el bucle de escucha de mensajes
    try:
        mqtt_client.loop_start()  # Cambiado de loop_forever() a loop_start() para no bloquear el hilo
    except KeyboardInterrupt:
        logging.info("Desconectando del broker MQTT...") #?Logging info
        mqtt_client.disconnect()
        logging.info("Desconectado del broker MQTT.") #?Logging info
