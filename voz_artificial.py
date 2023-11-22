#Modulo voz_artificial 

import requests
from dotenv import load_dotenv
import os
import pygame
from recomendaciones import respuesta_de_recomendacion

load_dotenv()

def voz_artificial():
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/g34gHuiq9eFHOygmLOnZ"
    XI_API_KEY = os.getenv("ELEVEN_API_KEY")

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": XI_API_KEY
    }

    data = {
        "text": str(respuesta_de_recomendacion),
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    with open('voz_artificial.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    # Reproducir el archivo mp3
    reproducir_audio('voz_artificial.mp3')

    # Borrar el archivo mp3
    os.remove('voz_artificial.mp3')

def reproducir_audio(archivo):
    # Inicializar pygame
    pygame.init()

    # Cargar y reproducir el archivo mp3
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()

    # Esperar hasta que la música termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Asegurarse de que la música ha dejado de reproducirse
    pygame.mixer.music.unload()

# Llamada a la función principal
voz_artificial()









