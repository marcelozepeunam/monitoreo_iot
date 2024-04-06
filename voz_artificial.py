'''Este modulo genera una recomendacion a traves de la API de openai, esta recomendacion es creada 
con base a los datos de lectura_iuv (lectura del sensor) y categoria.
Se utilizo una tecnica de prompt engineer llamada few-shots la cual le muestra algunos ejemplos de 
como se desea el resultado, de esta forma se evitan alucionaciones de GPT-4'''

#Modulo voz_artificial



import requests
import os
import pygame
import logging
from dotenv import load_dotenv

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def genera_voz_artificial(data_queue):
    load_dotenv()
    XI_API_KEY = os.getenv("ELEVEN_API_KEY")
    url = "https://api.elevenlabs.io/v1/text-to-speech/NgO5mdItOUAtAAnD7lsI"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": XI_API_KEY
    }

    pygame.mixer.init()

    while True:
        try:
            respuesta_de_recomendacion = data_queue.get()
            data = {
                "text": respuesta_de_recomendacion,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }

            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200 and len(response.content) > 1024:
                audio_file = 'output.mp3'
                with open(audio_file, 'wb') as f:
                    f.write(response.content)

                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    pass

                pygame.mixer.music.stop()
                os.remove(audio_file)

                logging.info(f"Voz generada y reproducida con éxito para el texto: {respuesta_de_recomendacion}") #? Logging info
            else:
                logging.warning("La respuesta de la API de voz no fue exitosa o el contenido es demasiado corto.") #? Logging info

        except Exception as e:
            logging.error(f"Error al generar voz artificial: {e}") #? Logging info
            break  # O manejar de otra forma

    pygame.mixer.quit()