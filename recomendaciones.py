'''Pendientes
Tecnicos:
1- Crear un proceso en el cual se reproduzca la voz artificial en cada lectura del sensor
2- Eliminar ese audio desués de reproducirlo para poder optimizar memoria
3- Implementar MQTT 
4- Hacer un prompt más especifico'''

import os 
import openai
import spacy
import pyautogui

from dotenv import load_dotenv

load_dotenv()

def recomendacion(lectura_iuv, categoria):
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    modelo = "text-davinci-002"

    #Utilizamos few-shots
    prompt = f'''Actua como experto en Protección Solar.
    Dime un dato curioso corto,
    para prevenir y tener cuidado
    ante un índice UV de {lectura_iuv} con 
    categoria {categoria}'''  
    
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
lectura_iuv=2 
categoria = "baja" 
respuesta_de_recomendacion = recomendacion(lectura_iuv, categoria)
print("\nRecomendación: ")
print(respuesta_de_recomendacion)































