 import machine
import time
import network
from umqtt.simple import MQTTClient

#Recordar que CLIENTE y SERVIDOR deben de trabajar bajo la misma red
nombre_red = "INFINITUM0643" #!RED DE CASA (PRUEBA)
contrasena_red = "NnPFUtCDuG"

#nombre_red = "" #!RED DE CELULAR (PRODUCCIÓN)
#contrasena_red = ""

# Creando instancia WLAN para la configuración de red
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(nombre_red, contrasena_red)  #Nombre de red y contraseña

# Verificando el estado de la conexión
if wlan.isconnected():
    print("Conexión exitosa")
else:
    print("Error al conectar a la red")

# Configuración de parámetros para la comunicación
MQTT_SERVER = " 192.168.67.90"  # Dirección IP de la Raspberry Pi
MQTT_PORT = 1883               # Puerto MQTT predeterminado de Mosquitto (broker)
MQTT_USER = "marcelozepe_unam" # Nombre de usuario
MQTT_PASSWORD = "unam2023"     # Contraseña
MQTT_TOPIC = b"voltaje"        # Tópico MQTT para publicar el voltaje (utilizar bytes)

# Creando instancia para establecer la conexión
client = MQTTClient("esp32_client", MQTT_SERVER, MQTT_PORT, MQTT_USER, MQTT_PASSWORD)
client.connect()


def convertidor_adc():
    adc = machine.ADC(machine.Pin(36))
    adc.atten(machine.ADC.ATTN_11DB)    # ATENUACIÓN
    adc.width(machine.ADC.WIDTH_11BIT)  # RESOLUCIÓN

    lectura_digital = adc.read()
    lectura_analogica = (lectura_digital / 2048) * 3.3
    voltaje = custom_map(lectura_analogica, 0.99, 2.7, 0, 15)  # Mapeo con los parámetros especificados
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
