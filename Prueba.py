# '''Ejemplos de codigo de cliente y servidor para completar la comunicacion correctamente'''

# #Cliente (ESP32)

# #Servidor (Raspberry)

# import socket

# if __name__ == "__main__":
#     # 1- Creamos el socket
#     mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     host = socket.gethostname()  # Obtenemos el nombre del host

#     # 2- Enlazamos el socket a la dirección y puerto
#     mi_socket.bind((host, 1234))

#     # 3- Escuchamos por una conexión
#     mi_socket.listen(1)

#     # Mantenemos siempre la escucha activa
#     while True:
#         # 4- Aceptamos la conexión
#         conexion, direccion = mi_socket.accept()
#         print("La conexión con {} ha sido aceptada".format(direccion))

#         # 5- Recibimos los datos
#         datos = conexion.recv(1000)
#         print("Esto es lo que contiene la request: {}".format(datos.decode("utf-8")))
#         print("\n")

#         # 6- Enviar response
#         respuesta = "Esto se envía desde el servidor"
#         conexion.send(bytes(respuesta, "utf-8"))

#         # Cerramos la conexión
#         conexion.close()

#     # Cerramos el socket (esto no se alcanza en el bucle infinito)
#     mi_socket.close()


import paho.mqtt.client as mqtt

# Configuración del servidor MQTT
mqtt_server = "IP_DEL_SERVIDOR"  # Reemplaza con la dirección IP de tu Raspberry Pi
topic = "mensaje"

# Callback que se ejecuta cuando se recibe un mensaje MQTT
def on_message(client, userdata, message):
    print(f"Mensaje recibido en el tema '{message.topic}': {message.payload.decode()}")

# Configura el cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(mqtt_server, 1883, 60)

# Se suscribe al tema para recibir mensajes
client.subscribe(topic)

# Mantén el cliente en ejecución para recibir mensajes
client.loop_forever()