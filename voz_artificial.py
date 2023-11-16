#Modulo voz_artificial

import pygame 
import time
import os
import requests
from dotenv import load_dotenv
from recomendaciones import respuesta_de_recomendacion

load_dotenv()

def voz_artificial():

    CHUNK_SIZE = 1024

    # Url de la voz clonada 
    url = f"https://api.elevenlabs.io/v1/text-to-speech/WMM564fNSAHcr9RrpzG7"
    # url = f"https://api.elevenlabs.io/v1/voices/WMM564fNSAHcr9RrpzG7"

    # Obtener la clave API de ElevenLabs desde el archivo .env
    XI_API_KEY = os.getenv("ELEVEN_API_KEY")

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": XI_API_KEY  # Usa la variable XI_API_KEY en lugar de "<xi-api-key>"
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
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    # Inicializa pygame mixer
    pygame.mixer.init()

    # Carga y reproduce el archivo MP3
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()

    # Espera a que termine la reproducción
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    # Cierra el mixer y elimina el archivo
    pygame.mixer.quit()
    os.remove('output.mp3')


voz_artificial()
