# Proyecto de tesis

## Introducción al Proyecto
Este proyecto desarrolla un sistema integrado de monitoreo de radiación ultravioleta utilizando una arquitectura IoT. Se emplea un microcontrolador ESP32 programado en MicroPython para capturar las mediciones de intensidad UV mediante el sensor ML8511. Estos datos son transmitidos en tiempo real a un servidor central basado en una Raspberry Pi 3B+, utilizando el protocolo de comunicación MQTT para el intercambio de mensajes. Para manejar las operaciones concurrentes sin corrupción de datos ni bloqueos, el sistema utiliza programación multihilo en el servidor. Se crean hilos dedicados para cada función principal: uno para el servidor MQTT que maneja la recepción de datos del sensor, otro para la interfaz de usuario que actualiza los datos en tiempo real, y un tercer hilo para la generación de voz artificial, que convierte las recomendaciones textuales en alertas audibles. Este diseño multihilo asegura que las tareas intensivas no interfieran unas con otras y mejora la responsividad del sistema. El servidor procesa los datos recibidos para evaluar niveles de exposición y genera recomendaciones dinámicas utilizando algoritmos de procesamiento de lenguaje natural (NLP) proporcionados por la API de OpenAI (GPT-3.5). Además, se utiliza la API de Elevenlabs para convertir las recomendaciones en alertas audibles, mejorando la interactividad del sistema. Este enfoque permite una supervisión efectiva y una respuesta adaptativa a las condiciones de UV, con el objetivo de mejorar la prevención y gestión de la exposición solar en usuarios finales.

## Tecnologías Utilizadas
- **Python 3.11.2:** Lenguaje de programación utilizado para el desarrollo del servidor y procesamiento de datos.
- **MicroPython:** Implementado en el ESP32 para manejo del sensor y comunicaciones MQTT.
- **API de OpenAI (GPT-3.5):** Utilizada para generar recomendaciones basadas en los datos de UV.
- **API de Elevenlabs:** Empleada para convertir texto en voz, proporcionando alertas audibles basadas en las recomendaciones.
- **MQTT:** Protocolo de mensajería ligero ideal para la comunicación entre el cliente ESP32 y el servidor Raspberry Pi.
- **Pygame:** Biblioteca utilizada para la reproducción de audio y manejo de la interfaz gráfica.

## Procesos
El sistema inicia con la activación del servidor MQTT en el Raspberry Pi, que luego suscribe al tópico 'lectura_iuv'. Mientras tanto, el ESP32 captura lecturas de UV y las envía al servidor. En el servidor, los datos son procesados para determinar categorías de riesgo UV y generar recomendaciones, que luego son comunicadas al usuario a través de la interfaz gráfica y por audio utilizando síntesis de voz. Los datos también son almacenados para análisis y visualización de tendencias.

## Diagrama de flujo
[Diagrama de flujo del sistema](https://lucid.app/lucidchart/323ef5f6-a94a-461a-a8f1-e6a4174953e3/edit?viewport_loc=66%2C-531%2C1798%2C768%2C0_0&invitationId=inv_d69216f1-87ba-48e5-b3b2-cfc10a90f023)

## Precios de las APIs
- [OpenAI API Overview](https://platform.openai.com/overview)
- [ElevenLabs Pricing](https://elevenlabs.io/)
