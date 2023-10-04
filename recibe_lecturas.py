import socket 


if __name__ == "__main__==":
    #1- Creamos el socket
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    servidor = socket.gethostbyname(socket.gethostbyname())

    #2- Enlazamos socket a puerto IP 
    mi_socket.bind((servidor, 1234))

    #3- Escuchamos por una conexion 
    mi_socket.listen(1)

    #Manetemos siempre la escucha activa 
    while True: 
        #4- Aceptamos la conexion
        conexion, direccion = mi_socket.accept()
        print("La conexion con {} ha sido aceptada".format(direccion))

        #5- Aceptamos la conexion 
        datos = conexion.recv(1000)
        print("Esto es lo que contiene la request {}".format(datos.decode("utf-8")))
        print("/n")

        #6- Enviar response
        conexion.send(bytes("Esto se envia desde el servidor", "utf-8"))

    conexion.close()
    mi_socket.close() 


