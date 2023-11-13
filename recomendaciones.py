'''Pendientes
Tecnicos:
1- Crear un proceso en el cual se reproduzca la voz artificial en cada lectura del sensor
2- Eliminar ese audio desués de reproducirlo para poder optimizar memoria
3- Implementar MQTT 
4- Hacer un prompt más especifico'''

import os 
import openai
import pyautogui

from dotenv import load_dotenv

load_dotenv()

def recomendacion(lectura_iuv, categoria):

    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key
    modelo = "text-davinci-002"

    #Utilizamos few-shots para mejorar la precision de la respuesta
    prompt = f'''Actua como experto en radiación ultravioleta
    Genera una recomendacion en segunda persona para preventiva para el cuidado de la radiacion UV, 
    para el publico que se encuentra en un espacio abierto.
    La recomendación se debe basar en un indice ultravioleta de {lectura_iuv},
    y de categoria {categoria}.'''
    
    pyautogui.press('enter')

    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=0.7,
        max_tokens=300,
    )
    respuesta_de_recomendacion = respuesta.choices[0].text.strip() 
    return respuesta_de_recomendacion


#?Ejemplo de uso
lectura_iuv=6 
categoria = "alta" 
respuesta_de_recomendacion = recomendacion(lectura_iuv, categoria)
print("\nRecomendación: ")
print(respuesta_de_recomendacion)



