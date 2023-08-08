'''Pendiente
El error se encuentra en el model_id'''


import requests
import os
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

















