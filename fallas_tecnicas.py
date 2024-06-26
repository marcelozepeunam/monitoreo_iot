'''Este modulo tiene como objetivo mostrar un mensaje por medio de una interfaz grafica
cuando se presento un error en la logica principal'''


#Modulo fallas tecnicas


import tkinter  as tk
from tkinter import Label
import logging 

# Configuración inicial de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #?Logging info

#Funcion fallas_tecnicas
def fallas_tecnicas():
    logging.info("Activación del módulo de fallas técnicas.") #? Logging info 

    #Creando ventana
    ventana = tk.Tk()
    ventana.title("Mantenimiento")
    ventana.geometry("1920x1080")
    # Crear una instancia de la ventana
    #ventana = tk.Tk()
    #ventana.attributes("-fullscreen", True)

    #Crear etiquetas
    etiqueta1 = tk.Label(ventana, text="EN MANTENIMIENTO", font=("Arial", 80))
    etiqueta2 = tk.Label(ventana, text='''\nDisculpe las molestias ocasionadas, 
    estamos trabajando para solucionar 
    la falla técnica lo antes posible.''', font=("Arial", 40))
    etiqueta3 = tk.Label(ventana, text="Contacto: marcelozepeda47@aragon.unam.mx", font=("Arial", 30))
    #etiqueta3 = tk.Label(ventana, text="\n\nContacto: marcelozepeda47@aragon.unam.mx", font=("Arial", 40))


    #Posicionar etiquetas
    etiqueta1.place(relx=0.5, rely=0.2, anchor="center")
    etiqueta2.place(relx=0.5, rely=0.5, anchor="center")
    etiqueta3.place(relx=0.5, rely=0.8, anchor="center")

    logging.info("Ventana de mantenimiento mostrada correctamente.") #?Logging info

    ventana.mainloop()
    
    

print(fallas_tecnicas())


