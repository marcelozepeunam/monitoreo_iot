'''Este modulo genera una recomendacion a traves de la API de openai, esta recomendacion es creada 
con base a los datos de lectura_iuv (lectura del sensor) y categoria.
Se utilizo una tecnica de prompt engineer llamada few-shots la cual le muestra algunos ejemplos de 
como se desea el resultado, de esta forma se evitan alucionaciones de GPT-4'''

#Modulo recomendaciones.py 


# import requests
# import os
# from dotenv import load_dotenv
# from recomendaciones import recomendacion

# load_dotenv()

# def voz_artificial(data_queue):
#     while True:
#         if not data_queue.empty():
#             lectura_iuv, categoria = data_queue.get()
#             recomendacion_texto = recomendacion(lectura_iuv, categoria)

#             CHUNK_SIZE = 1024
#             url = "https://api.elevenlabs.io/v1/text-to-speech/Cx2aqI2o6jdvuuXrogYa"
#             XI_API_KEY = os.getenv("ELEVEN_API_KEY")

#             headers = {
#                 "Accept": "audio/mpeg",
#                 "Content-Type": "application/json",
#                 "xi-api-key": XI_API_KEY
#             }

#             data = {
#                 "text": recomendacion_texto,
#                 "model_id": "eleven_monolingual_v2",
#                 "voice_settings": {
#                     "stability": 0.5,
#                     "similarity_boost": 0.5
#                 }
#             }

#             response = requests.post(url, json=data, headers=headers)
#             with open('voz_artificial.mp3', 'wb') as f:
#                 for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
#                     if chunk:
#                         f.write(chunk)



#Codigo modificado para la reproduccion y eliminacion automatica del mp3
# import requests
# import os
# from dotenv import load_dotenv
# from recomendaciones import recomendacion
# from playsound import playsound  # Importa playsound

# load_dotenv()

# def generar_voz_artificial(data_queue):
#     while True:
#         if not data_queue.empty():
#             lectura_iuv, categoria = data_queue.get()
#             recomendacion_texto = recomendacion(lectura_iuv, categoria)

#             CHUNK_SIZE = 1024
#             url = "https://api.elevenlabs.io/v1/text-to-speech/Cx2aqI2o6jdvuuXrogYa"
#             XI_API_KEY = os.getenv("ELEVEN_API_KEY")

#             headers = {
#                 "Accept": "audio/mpeg",
#                 "Content-Type": "application/json",
#                 "xi-api-key": XI_API_KEY
#             }

#             data = {
#                 "text": recomendacion_texto,
#                 "model_id": "eleven_monolingual_v2",
#                 "voice_settings": {
#                     "stability": 0.5,
#                     "similarity_boost": 0.5
#                 }
#             }

#             response = requests.post(url, json=data, headers=headers)
#             file_path = 'C:/Users/usuario/Desktop/Tesis/Programacion/Programacion_raspberry/voz_artificial.mp3'
#             with open(file_path, 'wb') as f:
#                 for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
#                     if chunk:
#                         f.write(chunk)

#             # Reproduce el archivo de audio
#             playsound(file_path)

#             # Elimina el archivo de audio después de su reproducción
#             os.remove(file_path)






# #Con pygame
# import requests
# import os
# from dotenv import load_dotenv
# from recomendaciones import recomendacion
# import pygame  # Importa el módulo pygame

# load_dotenv()

# def generar_voz_artificial(data_queue):
#     while True:
#         if not data_queue.empty():
#             lectura_iuv, categoria = data_queue.get()
#             recomendacion_texto = recomendacion(lectura_iuv, categoria)

#             CHUNK_SIZE = 1024
#             url = "https://api.elevenlabs.io/v1/text-to-speech/Cx2aqI2o6jdvuuXrogYa"
#             XI_API_KEY = os.getenv("ELEVEN_API_KEY")

#             headers = {
#                 "Accept": "audio/mpeg",
#                 "Content-Type": "application/json",
#                 "xi-api-key": XI_API_KEY
#             }

#             data = {
#                 "text": recomendacion_texto,
#                 "model_id": "eleven_monolingual_v2",
#                 "voice_settings": {
#                     "stability": 0.5,
#                     "similarity_boost": 0.5
#                 }
#             }

#             response = requests.post(url, json=data, headers=headers)
#             file_path = 'C:/Users/usuario/Desktop/Tesis/Programacion/Programacion_raspberry/voz_artificial.mp3'
#             with open(file_path, 'wb') as f:
#                 for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
#                     if chunk:
#                         f.write(chunk)
#                     else:
#                         print("Error en la petición: ", response.status_code)

#             # Reproduce el archivo de audio
#             pygame.mixer.init()
#             pygame.mixer.music.load(file_path)
#             pygame.mixer.music.play()

#             # Espera a que termine la reproducción del audio
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(10)

#             # Elimina el archivo de audio después de su reproducción
#             os.remove(file_path)






#Con pydub
import requests
import os
from dotenv import load_dotenv
from recomendaciones import recomendacion
from pydub import AudioSegment
from pydub.playback import play

load_dotenv()

def generar_voz_artificial(data_queue):
    while True:
        if not data_queue.empty():
            lectura_iuv, categoria = data_queue.get()
            recomendacion_texto = recomendacion(lectura_iuv, categoria)

            CHUNK_SIZE = 1024
            url = "https://api.elevenlabs.io/v1/text-to-speech/Cx2aqI2o6jdvuuXrogYa"
            XI_API_KEY = os.getenv("ELEVEN_API_KEY")

            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": XI_API_KEY
            }

            data = {
                "text": recomendacion_texto,
                "model_id": "eleven_monolingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }

            response = requests.post(url, json=data, headers=headers)
            file_path = 'voz_artificial.mp3'
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
                    else:
                        print("Error en la petición: ", response.status_code)

            # Reproduce el archivo de audio
            audio = AudioSegment.from_mp3('C:/Users/usuario/Desktop/Tesis/Programacion/Programacion_raspberry/voz_artificial.mp3')
            play(audio)

            # Elimina el archivo de audio después de su reproducción
            os.remove('C:/Users/usuario/Desktop/Tesis/Programacion/Programacion_raspberry/voz_artificial.mp3')

