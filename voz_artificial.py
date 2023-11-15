'''Pendientes
Se debe de borrar el archivo mp3 después de reproducirlo
o en su defecto almacenar los audios en una lista y con un 
iterador ir reproduciendo los audios de acuerdo a las lecturas'''



import requests
from dotenv import load_dotenv
import os
from recomendaciones import respuesta_de_recomendacion

load_dotenv()

def voz_artificial():

  CHUNK_SIZE = 1024

  #Url de la voz clonada 
  url = f"https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
  #url = f"https://api.elevenlabs.io/v1/voices/WMM564fNSAHcr9RrpzG7"


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


voz_artificial()

