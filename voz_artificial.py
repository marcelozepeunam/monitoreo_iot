'''Este modulo genera una recomendacion a traves de la API de openai, esta recomendacion es creada 
con base a los datos de lectura_iuv (lectura del sensor) y categoria.
Se utilizo una tecnica de prompt engineer llamada few-shots la cual le muestra algunos ejemplos de 
como se desea el resultado, de esta forma se evitan alucionaciones de GPT-4'''

#Modulo voz_artificial


import requests
import os
import pygame
import time
from dotenv import load_dotenv


load_dotenv()

pygame.mixer.init()

def genera_voz_artificial(data_queue):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/NgO5mdItOUAtAAnD7lsI"
    XI_API_KEY = os.getenv("ELEVEN_API_KEY")

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": XI_API_KEY
    }

    while True:
        # Esperar a recibir una recomendación desde la cola
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

            # Inicializar pygame para reproducción de audio
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            # Esperar a que termine la reproducción
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            # Detener la reproducción y desinicializar pygame
            pygame.mixer.music.stop()
            pygame.mixer.quit()

            # Eliminar el archivo después de la reproducción
            os.remove(audio_file)



