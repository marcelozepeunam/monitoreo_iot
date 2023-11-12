'''El servidor se configuró para que este a la escucha continuamente'''

import paho.mqtt.client as mqtt

def manejar_lectura_iuv(lectura_iuv):
    # Aquí puedes realizar cualquier operación que desees con la variable "lectura_iuv"
    # Por ejemplo, imprimir su valor o almacenarlo en una lista, base de datos, etc.
    print(f"Lectura IUV recibida: {lectura_iuv}")

def on_message(client, userdata, message):
    try:
        lectura_iuv = float(message.payload.decode("utf-8"))  
        manejar_lectura_iuv(lectura_iuv)
    except ValueError:
        print("Error: Lectura IUV no válida")
    except Exception as e:
        print(f"Error inesperado: {e}")

def iniciar_servidor_mqtt():
    # Configura las credenciales para conectarse al broker MQTT
    mqtt_broker = "192.168.1.150"  # Cambia esto por la dirección de tu broker MQTT
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
    iniciar_servidor_mqtt()
