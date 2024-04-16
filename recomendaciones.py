'''Este modulo genera una recomendacion a traves de la API de openai, esta recomendacion es creada 
con base a los datos de lectura_iuv (lectura del sensor) y categoria.
Se utilizo una tecnica de prompt engineer llamada few-shots la cual le muestra algunos ejemplos de 
como se desea el resultado, de esta forma se evitan alucionaciones de GPT-4'''




#Modulo recomendaciones.py 

import logging
import openai
from dotenv import load_dotenv
import os

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def recomendacion(lectura_iuv, categoria):
    # Carga la clave API desde .env para mayor seguridad
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    prompt = f'''Actua como experto en radiación ultravioleta.
    Genera una recomendacion en segunda persona para preventiva para el cuidado de la radiacion UV, 
    para el publico que se encuentra en un espacio abierto.
    La recomendación se debe basar en un indice ultravioleta de {lectura_iuv},
    y de categoria {categoria}.
    
    Ejemplos de output son proporcionados para guiar la generación de recomendaciones adecuadas.'''

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": prompt}
            ]
        )
        recomendacion_texto = response.choices[0].message['content'].strip()
        logging.info(f"Recomendación generada con éxito para IUV {lectura_iuv} y categoría {categoria}.")
        return recomendacion_texto
    except Exception as e:
        logging.error(f"Error al generar recomendación: {e}")
        return "Error al generar recomendación."

# Ejemplo de cómo se usaría la función
#if __name__ == "__main__":
#    lectura_iuv = 5
#    categoria = "MODERADO"
#    print(recomendacion(lectura_iuv, categoria))