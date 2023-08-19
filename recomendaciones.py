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

#?from main import categoria, lectura_iuv, lectura_max 

from dotenv import load_dotenv



load_dotenv()

def recomendacion(categoria):
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    modelo = "text-davinci-002"
    # prompt = f'''Actua como experto en Protección Solar.
    # Dime algun dato curioso para prevenir y tener cuidado
    # ante un índice UV solar de categoria {categoria}
    # No menciones numeros ni horarios '''  
    # prompt = f'''Actua como experto en Protección Solar.
    # Dime un "¿sabías qué?" corto para prevenir y tener cuidado
    # ante un índice UV solar de {lectura_iuv} de 
    # categoria {categoria}
    # No menciones numeros ni horarios '''  

    prompt = f'''Actua como experto en Protección Solar.
    Dime un dato curioso corto,
    para prevenir y tener cuidado
    ante un índice UV solar de {lectura_iuv} de 
    categoria {categoria}
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



def recomendacion_final(categoria):
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    modelo = "text-davinci-002"
    prompt = f'''Actua como experto en UV.
    Dame un resumen intermedio basado en la siguientes indices ultravioletas obtenidos durante el día
    IUU minimo: {lectura_min}
    IUV promedio: {lecturas_prom}
    IUV minima: {lectura_min}
    Se debe de entender "IUV" como índice ultravioleta.
    Comienza diciendo "El día de hoy, en que se realizo el monitoreo de UV..."
    Por último finaliza con la frase "el programa se suspenderá en unos segundos
    "'''  

    pyautogui.press('enter')
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=0.7,
        max_tokens=200,
    )
    respuesta_de_recomendacion = respuesta.choices[0].text.strip() 
    return respuesta_de_recomendacion





# #?Recomendacion entre lecturas
# # Invocando a la función
# categoria = "baja" 
# lectura_iuv=1
# #Categoria de prueba 
# respuesta_de_recomendacion = recomendacion(categoria)
# print("\nRecomendación: ")
# print(respuesta_de_recomendacion)



#?Recomendacion final
# Invocando a la función
#categoria = "baja" 
lectura_min=1
lectura_max=3
lecturas_prom=2
#Categoria de prueba 
respuesta_de_recomendacion_final = recomendacion_final(lectura_max)
print("\nRecomendación final: ")
print(respuesta_de_recomendacion_final)


















