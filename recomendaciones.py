'''Este modulo genera una recomendacion a traves de la API de openai, esta recomendacion es creada 
con base a los datos de lectura_iuv (lectura del sensor) y categoria.
Se utilizo una tecnica de prompt engineer llamada few-shots la cual le muestra algunos ejemplos de 
como se desea el resultado, de esta forma se evitan alucionaciones de GPT-4'''




#Modulo recomendaciones.py 

import os 
import openai
from dotenv import load_dotenv

load_dotenv()

def recomendacion(lectura_iuv, categoria):
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    prompt = f'''Actua como experto en radiación ultravioleta.
    Genera una recomendacion en segunda persona para preventiva para el cuidado de la radiacion UV, 
    para el publico que se encuentra en un espacio abierto.
    La recomendación se debe basar en un indice ultravioleta de {lectura_iuv},
    y de categoria {categoria}.
    
    Te mostrare algunos ejemplos y con base a los ejemplos quiero que el output sea parecido:

    Ejemplo 1 de output: "IUV 1 (Bajo): Riesgo mínimo de daño solar. Aun así, usa protector solar 
    FPS 15+ y gafas de sol si estarás al aire libre por largo tiempo. ¡Disfruta con seguridad!"

    Ejemplo 2 de output: IUV 6 (Alto): Riesgo elevado de daño solar. Usa protector solar FPS 30+, 
    ropa protectora, sombrero y gafas UV. Evita el sol de 10 a.m. a 4 p.m. ¡Protege tu piel!


    Ejemplo 3 de output: "IUV 11 (Extremo): Riesgo serio de daño solar. Aplica protector solar FPS 
    50+, viste manga larga, pantalones, sombrero y gafas UV completas. Limita exposición solar, 
    especialmente de 10 a.m. a 4 p.m., y mantente hidratado. ¡Prioriza tu salud!"''' 

    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": prompt}
        ]
    )
    respuesta_de_recomendacion = respuesta.choices[0].message['content'].strip()
    return respuesta_de_recomendacion

#Ejemplo de uso
#lectura_iuv = 1
#categoria = "baja" 
#respuesta_de_recomendacion = recomendacion(lectura_iuv, categoria)
#print("\nRecomendación: ")
#print(respuesta_de_recomendacion)

