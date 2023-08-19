'''Pendientes
Se debe de borrar el a5rchivo mp3 después de reproducirlo
o en su defecto almacenar los audios en una lista y con un 
iterador ir reproduciendo los audios de acuerdo a las lecturas'''


import requests
import os
import pygame 
from recomendaciones import *  # Asegúrate de importar lo necesario desde recomendaciones
from dotenv import load_dotenv

load_dotenv()

def artificial_voice():


    CHUNK_SIZE = 1024
    url = f"https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM" #Agregar voice id despues de ""speech/#

    # Obtener la clave API de ElevenLabs desde el archivo .env
    XI_API_KEY = os.getenv("ELEVEN_API_KEY")

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": XI_API_KEY
    }

    data = {
        "text": str(respuesta_de_recomendacion),  
        "model_id": "eleven_monolingual_v1",
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

artificial_voice()














import requests
import pygame
import tempfile
import os

from dotenv import load_dotenv
from recomendaciones import *


load_dotenv()

def artificial_voice():
    CHUNK_SIZE = 1024
    url = f"https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

    # Obtener la clave API de ElevenLabs desde el archivo .env
    XI_API_KEY = os.getenv("ELEVEN_API_KEY")

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": XI_API_KEY
    }

    data = {
        "text": str(respuesta_de_recomendacion),
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    
    # Crear un archivo temporal para el audio
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(response.content)
    temp_file.close()

    # Reproducir el archivo de audio con pygame
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file.name)
    pygame.mixer.music.play()

    # Esperar hasta que se complete la reproducción
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Borrar el archivo temporal después de la reproducción
    os.remove(temp_file.name)

artificial_voice()



