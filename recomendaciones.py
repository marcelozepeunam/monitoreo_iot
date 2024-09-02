import logging
import openai
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configurar la API Key de OpenAI desde las variables de entorno
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def recomendacion(lectura_iuv, categoria):
    # Definir el prompt para el modelo
    messages = [
        {"role": "system", "content": "Actúa como Vegeta de Dragon Ball Z. Genera una recomendación para el cuidado de la radiación ultravioleta en un espacio abierto. La recomendación debe basarse en un índice ultravioleta de {lectura_iuv} y en la categoría {categoria}. Debes usar frases propias de Vegeta como: 'Maldito insecto', 'Debes sentirte afortunado...', 'Al menos trata de morir con honor...', y 'Un saiyano que no puede ni moverse es inútil para mí'. La recomendación debe ser corta (máximo 200 tokens) y mencionar siempre los datos de lectura_iuv y categoría."},
        {"role": "user", "content": f"El índice ultravioleta es {lectura_iuv} y la categoría es {categoria}."}
    ]

    try:
        # Llamada a la API para obtener una completación de chat
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Modelo de chat recomendado
            messages=messages,
            max_tokens=200,  # Ajusta según tus necesidades
            temperature=0.7  # Ajusta según el nivel de creatividad deseado
        )

        # Obtener y retornar el contenido de la respuesta
        recomendacion_texto = response.choices[0].message['content'].strip()
        logging.info(f"Recomendación generada con éxito para IUV {lectura_iuv} y categoría {categoria}.")
        return recomendacion_texto
    except Exception as e:
        logging.error(f"Error al generar recomendación: {e}")
        return "Error al generar recomendación."

# Ejemplo de uso
"""
if __name__ == "__main__":
    lectura_iuv = int(input("Lectura_iuv: "))
                      
    if lectura_iuv <= 2:
        categoria = "BAJO"
    elif 3 <= lectura_iuv <= 5:
        categoria = "MODERADO"
    elif 6 <= lectura_iuv <= 7:
        categoria = "ALTO"
    elif 8 <= lectura_iuv <= 10:
        categoria = "MUY ALTO"
    elif lectura_iuv >= 11:
        categoria = "EXTREMO"
    else:
        categoria = "DESCONOCIDA"
    
    print(recomendacion(lectura_iuv, categoria))
"""