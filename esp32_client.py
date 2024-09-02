#PROYECTO FINAL

import machine
import time
import network
from umqtt.simple import MQTTClient, MQTTException

# Configuración de red
nombre_red = ""
contrasena_red = ""

# Configuración de parámetros para la comunicación
MQTT_SERVER = ""  # Broker público de Eclipse
#MQTT_USER = "marcelozepe_unam" # Nombre de usuario
#MQTT_PASSWORD = "unam2023"     # Contraseña

MQTT_USER = "" # Nombre de usuario
MQTT_PASSWORD = ""     # Contraseña
MQTT_PORT = 1883
MQTT_TOPIC = b"lectura_iuv"

# Conectando a la red
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(nombre_red, contrasena_red)

# Espera hasta que la conexión sea exitosa
max_attempts = 10
attempts = 0
while not wlan.isconnected() and attempts < max_attempts:
    print("Intentando conectar a la red...")
    time.sleep(2)
    attempts += 1

if wlan.isconnected():
    print("Conexión exitosa")
else:
    print("Error al conectar a la red")
    while True:
        time.sleep(1)  # Mantener el ESP32 en un bucle si no puede conectar

# Conexión al broker MQTT
try:
    client = MQTTClient("esp32_client", MQTT_SERVER, MQTT_PORT, MQTT_USER, MQTT_PASSWORD)
    client.connect()
    print("Conectado al servidor MQTT")
except MQTTException as e:
    print("Error al conectar al servidor MQTT:", e)
    while True:
        time.sleep(1)  # Mantener el ESP32 en un bucle si no puede conectar al MQTT

def convertidor_adc():
    adc = machine.ADC(machine.Pin(36))
    adc.atten(machine.ADC.ATTN_11DB)
    adc.width(machine.ADC.WIDTH_11BIT)

    lectura_digital = adc.read()
    lectura_analogica = (lectura_digital / 2048) * 3.3
    voltaje = custom_map(lectura_analogica, 0.99, 2.7, 0, 15)
    voltaje = round(voltaje, 2)
    voltaje = abs(voltaje)

    print("\n")
    print("Valor digital:", lectura_digital)
    print("Valor analógico:", lectura_analogica)
    print("Voltaje:", voltaje)

    # Publicar el voltaje en el tópico MQTT
    client.publish(MQTT_TOPIC, str(voltaje))

def custom_map(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    convertidor_adc()
    time.sleep(30)  # Esperar 30 segundos antes de la siguiente lectura y publicación
