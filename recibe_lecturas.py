'''En este modulo se recibiran los datos de la ESP32 (cliente) por medio 
del protocolo MQTT'''

'''Pendientes
1- Configurar direccion del broker
2- Mandar la variable "lectura_iuv" al modulo main
3-Debemos crear un while para que reciba los datos n veces'''

import paho.mqtt.client as mqtt

def manejar_lectura_iuv(lectura_iuv):
    # Aquí puedes realizar cualquier operación que desees con la variable "lectura_iuv"
    # Por ejemplo, imprimir su valor o almacenarlo en una lista, base de datos, etc.
    print(f"Lectura IUV recibida: {lectura_iuv}")

def on_message(client, userdata, message):
    lectura_iuv = int(message.payload)
    manejar_lectura_iuv(lectura_iuv)

def iniciar_servidor_mqtt():
    # Configura las credenciales para conectarse al broker MQTT
    mqtt_broker = "direccion_del_broker"  # Cambia esto por la dirección de tu broker
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





