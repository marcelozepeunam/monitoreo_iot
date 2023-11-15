#Modulo recomendaciones.py 

'''Este modulo genera una recomendacion a traves de la API de openai, esta recomendacion es creada 
con base a los datos de lectura_iuv (lectura del sensor) y categoria.
Se utilizo una tecnica de prompt engineer llamada few-shots la cual le muestra algunos ejemplos de 
como se desea el resultado, de esta forma se evitan alucionaciones de GPT-4'''


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

    Ejemplo 1 de output: Actualmente, la lectura del Índice Ultravioleta (IUV) es de 1, lo cual indica una 
    categoría 'Baja'. Esto significa que el riesgo de daño por la exposición al sol es mínimo. Sin embargo, 
    aún es recomendable usar protección si planeas estar al aire libre durante un tiempo prolongado. 
    Para una protección óptima, considera usar gafas de sol y aplicar un protector solar con un FPS de al menos 15. 
    ¡Disfruta del día de manera segura!

    Ejemplo 2 de output: "¡Atención! La lectura actual del Índice Ultravioleta (IUV) es de 6, lo cual se clasifica en la 
    categoría 'Alta'. 
    Esto implica un riesgo elevado de daño por exposición al sol. 
    Es altamente recomendable tomar medidas de protección, como usar un protector solar con un factor de protección solar (FPS) 
    de al menos 30, llevar ropa que cubra la piel, usar sombrero y gafas de sol que bloqueen los rayos UV. 
    Evita la exposición solar entre las 10 a.m. y las 4 p.m. si es posible. ¡Protege tu piel y disfruta del día de forma segura!"


    Ejemplo 3 de output: Alerta Crítica: El Índice Ultravioleta (IUV) actual es de 11, lo cual se encuentra en la categoría 'Extremadamente 
    Alta'. Este nivel representa un riesgo muy serio de daño por la exposición al sol. Es esencial tomar medidas de protección exhaustivas. 
    Usa un protector solar con un factor de protección solar (FPS) de 50 o más, viste ropa de manga larga, pantalones y sombrero de ala ancha.
    Las gafas de sol deben ofrecer protección completa contra los rayos UVA y UVB. Limita al máximo la exposición directa al sol, 
    especialmente entre las 10 a.m. y las 4 p.m. 
    Busca sombra siempre que sea posible y mantente hidratado. 
    La exposición en estas condiciones puede causar graves quemaduras solares y daños en la piel a corto plazo. 
    ¡Prioriza tu salud y seguridad!''' 

    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": prompt}
        ]
    )
    respuesta_de_recomendacion = respuesta.choices[0].message['content'].strip()
    return respuesta_de_recomendacion

# Ejemplo de uso
lectura_iuv = 1
categoria = "baja" 
respuesta_de_recomendacion = recomendacion(lectura_iuv, categoria)
print("\nRecomendación: ")
print(respuesta_de_recomendacion)


