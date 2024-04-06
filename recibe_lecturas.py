#Modulo recibe_lecturas por medio de MQTT

'''Este modulo es el encargado de recibir las lecturas (topic) por medio del
protocolo MQTT.
El servidor se configuró para que este a la escucha continuamente'''

'''import paho.mqtt.client as mqtt

def manejar_lectura_iuv(lectura_iuv):
    print(f"Lectura IUV recibida: {lectura_iuv}")

def on_message(client, userdata, message):
    try:
        lectura_iuv = float(message.payload.decode("utf-8"))  
        print(f"Tópico: {message.topic} - Lectura IUV recibida: {lectura_iuv}") #!Prueba
        manejar_lectura_iuv(lectura_iuv)
    except ValueError:
        print("Error: Lectura IUV no válida")
    except Exception as e:
        print(f"Error inesperado: {e}")

def iniciar_servidor_mqtt():
    # Configura las credenciales para conectarse al broker MQTT
    #mqtt_broker = "192.168.1.150"  # IP red celular
    mqtt_broker = "192.168.1.103"  # IP extensor de red
    mqtt_port = 1883  # Puerto predeterminado para MQTT

    # Crea una instancia del cliente MQTT
    mqtt_client = mqtt.Client()

    # Asigna la función de manejo de mensajes al cliente MQTT
    mqtt_client.on_message = on_message

    # Conecta al broker MQTT
    mqtt_client.connect(mqtt_broker, mqtt_port)

    # Subscribe al tópico "lectura_iuv" para recibir mensajes
    mqtt_client.subscribe("lectura_iuv")

    # Bucle principal para mantener la conexión MQTT activa
    mqtt_client.loop_forever()


if __name__ == "__main__":
    iniciar_servidor_mqtt()'''






import paho.mqtt.client as mqtt
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def on_message(client, userdata, message, data_queue):
    logging.debug(f"Mensaje recibido en topic: {message.topic}")
    try:
        lectura_iuv = float(message.payload.decode("utf-8"))
        logging.debug(f"Payload del mensaje: {message.payload}")

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
        
        # Poner la lectura y la categoría en data_queue
        data_queue.put((lectura_iuv, categoria))
        logging.info(f"Se recibió lectura {lectura_iuv} con éxito, categoría: {categoria}")

    except ValueError:
        logging.warning("No se recibió lectura válida")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")

def iniciar_servidor_mqtt(data_queue):
    mqtt_broker = "192.168.1.103"  # Cambiar IP dependiendo de donde se conecte
    mqtt_port = 1883
    mqtt_client = mqtt.Client()

    # Inicia la conexión y suscripción
    logging.info(f"Conectando al broker MQTT en {mqtt_broker}:{mqtt_port}")
    mqtt_client.connect(mqtt_broker, mqtt_port)

    # Suscripción al tópico
    mqtt_client.subscribe("lectura_iuv")
    logging.info(f"Suscrito exitosamente al tópico 'lectura_iuv'")

    # Ajuste de la función de callback para mensajes
    mqtt_client.on_message = lambda client, userdata, msg: on_message(client, userdata, msg, data_queue)

    # Inicia el bucle de escucha de mensajes
    try:
        mqtt_client.loop_forever()
    except KeyboardInterrupt:
        logging.info("Desconectando del broker MQTT...")
        mqtt_client.disconnect()
        logging.info("Desconectado del broker MQTT.")


