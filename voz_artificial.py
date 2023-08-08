
import requests
from dotenv import load_dotenv
import os
#from recomendaciones import respuesta_de_recomendacion

load_dotenv()

def artificial_voice():

  CHUNK_SIZE = 1024
  url = "https://api.elevenlabs.io/v1/text-to-speech/ae7Io0wuTbNZGAGL5yfx"

  # Obtener la clave API de ElevenLabs desde el archivo .env
  ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

  headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": ELEVEN_API_KEY  # Usa la variable XI_API_KEY en lugar de "<xi-api-key>"
  }

  data = {
      #"text": {respuesta_de_recomendacion}, #Este text debe de venir de un prompt
      "text": "Categoria ultravioleta muy alta, por favor utilice protector solar", #Este text debe de venir de un prompt
      "model_id": "v0hp8yo0WtalX5MlZKBi",
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