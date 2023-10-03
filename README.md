#Proyecto de tesis

El proyecto de tesis presentado tiene como objetivo 
el monitoreo de UV por medio del protocolo de comunicacion 
MQTT.
El proyecto consta de un cliente (ESP32)y un servidor (Raspberry)
utilizando herramientas apoyadas en IA.

##Logica del proyecto
Por medio de un sensor ML8511 conectado a una ESP32 (cliente) 
se utiliza la informacion adquirida para convertirla a 
lecturas digitales, luego determinamos el índice ultravioleta (IUV) mediante una formula matematica, todo esto programado en micropython.
Luego este valor guardado en la variable "lectura_iuv" será enviado como topic por MQTT al servidor (Raspberry pi 3 B+) cada 60 segundos durante 30 minutos.
Al llegar al servidor y utilizando el lenguaje de programación Python, se desarrollo diferentes tipos de modulos como lo son:

1-fallas_tecnicas
2-graficas_resumen
3-main
4-panel_usuario
5-recibe_lecturas
6-recomendaciones
7-registros 
8-voz_artificial

Estos modulos se utilizaran en el modulo principal "main" en donde por medio de un algoritmo y ciertos tiempos establecidos ejecutaremos funciones del modulo correspondiente.
En cada lectura se podra visualizar los datos adquiridos por el recibidos, y en funcion a esos datos
se generará con ayuda del modelo de procesamiento de lenguaje natural, y posteriormente se leerá esta
recomendación con ayuda de elevenlabs.
Al finalizar las 30 lecturas, el programa mostrara un resumen por medio de graficas y se guardara un archivo de excel en donde tendremos informacion relevante durante la ejecucion del proyecto.

##Notas
Es importante saber que para utilizar este proyecto correctamente se debe de crear unas API keys en:
https://platform.openai.com/overview
https://elevenlabs.io/

Estas keys por seguridad se guardaran en el archivo .env
Su uso tiene un costo dependiendo del uso, se puede consultar en los mismos links.