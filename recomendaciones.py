'''Pendientes
Hacer un prompt más especifico'''

import os 
import openai
import spacy
import pyautogui

from dotenv import load_dotenv



load_dotenv()

def recomendacion(categoria):
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    modelo = "text-davinci-002"
    prompt = f'''Actua como experto en Protección Solar.
    Dime algun dato curioso para prevenir y tener cuidado
    ante un índice UV solar de categoria {categoria}
    No menciones numeros ni horarios '''  


    pyautogui.press('enter')
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=0.7,
        max_tokens=300
        ,
    )
    respuesta_de_recomendacion = respuesta.choices[0].text.strip() 
    return respuesta_de_recomendacion


# Invocando a la función
categoria = "muy alta"
respuesta_de_recomendacion = recomendacion(categoria)
print("\nRecomendación: ")
print(respuesta_de_recomendacion)








