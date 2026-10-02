def coordenadas_deunLocal():
   #Representa mediante una tupla la latitud y longitud de un negocio.
   #Desempaqueta los valores y muéstralos con etiquetas.
   coordenada = (-34.42, 73.21)
   latitud, longitud = coordenada
   print(f"Latitud: {latitud}")
   print(f"Longitud {longitud}")
   

def dimensiones_caja():
    #Guarda ancho, alto y profundidad en una tupla y calcula el volumen sin modificar la tupla.
    caja = (20, 30, 10)
    ancho, alto, profundidad = caja
    volumen = ancho * alto * profundidad
    print(f"Volumen de la caja: {volumen}")

def registroEstudiante():
    #Representa el nombre, edad y promedio de un estudiante mediante una tupla.
    #Recorre sus elementos y muestra la información.
    estudiante = ("Zack", "24", "100")
    etiquetas = ("Nombre", "Edad", "Promedio")

    for i in range(len(estudiante)):
        print(f"{etiquetas[i]}: {estudiante[i]}")


def puntosRuta():
    #Crea una lista de tuplas para representar varios puntos de una ruta.
    #Recorre la lista mostrando latitud y longitud.
    puntos = [(-34.42, 73.21), (-56.34, 15.1), (65, -24.45)]
    
    for i in range(len(puntos)):
        latitud, longitud = puntos[i]
        print(f"Latitud: {latitud}")
        print(f"Longitud: {longitud}")

def retornoMultiple():
    #Crea una función que reciba una lista de ventas y retorne una tupla con total, promedio y venta máxima.
    ventas = []
    numv = int(input("Ingrese cuantas ventas desea digitar: "))
    for i in range(numv):
        venta = float(input(f"Ingrese cuanto vendio en la venta #{i+1}: "))
        ventas.append(venta)
    
    total = sum(ventas) 
    promedio = total / numv
    ventamax = max(ventas)

    tuplasoli = (total, promedio, ventamax)

    return tuplasoli

