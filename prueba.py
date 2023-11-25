
import requests
from dotenv import load_dotenv
import os
import pygame
import time

load_dotenv()

def genera_y_reproduce_voz_artificial():
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/Cx2aqI2o6jdvuuXrogYa"
    XI_API_KEY = os.getenv("ELEVEN_API_KEY")

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": XI_API_KEY
    }

    data = {
        "text": "Hola este es un audio de prueba",
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
        pygame.mixer.init()
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

genera_y_reproduce_voz_artificial()

