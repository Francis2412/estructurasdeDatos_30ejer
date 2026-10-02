def InventarioDispositivos():
    #Crea una lista con al menos 8 productos. Permite agregar un nuevo producto,
    #modificar uno existente y mostrar la lista final.
    productos = ["queso", "frijoles", "arroz", "aguacate", "chiltoma", "salsa", "café", "perejil"]
    
    print(" --- Menú --- ")
    print("1. Agregar un nuevo producto")
    print("2. Modificar uno producto existente")
    
    num = int(input("¿Qué deseas hacer?"))
    if num == 1:
        print("Los productos existentes son los siguientes: ")
        print(productos)
        print("")
        nuevo_producto = input("Ingrese el nuevo producto: ")
        productos.append(nuevo_producto)
        print("")
        print("Producto agregado correctamente...")
        print("")
        print(productos)

    elif num == 2:
        print("Los productos existentes son los siguientes: ")
        print(productos)
        print("")
        posicion = int(input("Ingrese el número del producto que desea modificar (0-7)"))
        nuevo_producto = input("Ingrese el nuevo producto: ")
        productos[posicion] = nuevo_producto
        print("Producto modificado correctamente...")
        print(productos)
        
    else:
        print("Esa opción no existe...")   
        
def VentasSemanales():
    #Registra las ventas de siete días en una lista. Calcula el total, el promedio y muestra el día 
    #con la venta más alta.
    ventas = []

    for i in range(7):
        venta = float(input("Ingrese el día: "))
        ventas.append(venta)

    total = sum(ventas)
    promedio = total / 7
    venta_mayor = max(ventas)
    dia_mayor = ventas.index(venta_mayor)

    print("Ventas:", ventas)
    print("Total de ventas:", total)
    print("Promedio de ventas:", promedio)
    print("El día con mayor venta fue el día", dia_mayor + 1)


def TemperaturasManagua():
    #Almacena temperaturas de varios días y genera una nueva lista con
    #las temperaturas mayores a 30 grados.
    temperaturas = []
    temMayor30 = []

    dias = int(input("¿Por cuántos días deseas almacernar las temperaturas? "))

    for i in range(dias):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temperatura)
        if temperatura > 30:
            temMayor30.append(temperatura)
    
    print(f"Lista de las temperaturas de {dias} días: ")
    print(temperaturas)
    print("")
    print(f"Lista de las temperaturas mayores a 30 grados: ")
    print(temMayor30)

    
    
def dispositivos_sinConexion():
    #Dada una lista de existencias, identifica las posiciones donde la existencia es
    #0 y muestra cuántos productos están agotados.
    existencias = [1, 2, 0, 4, 5, 6, 0, 8, 9, 0]
    posiciones = []
    agotados = 0

    for i in range(len(existencias)):
        if existencias[i] == 0:
            posiciones.append(i + 1)
            agotados += 1
    
    print("Posiciones de productos agotados:")
    print(posiciones)
    print("")
    print(f"Cantidad de productos agotados: {agotados}")
    

def Ordenamientolatencias():
    #Solicita 10 latencias de respuesta, guárdalas en una lista y muestra los precios 
    #de menor a mayor y luego de mayor a menor.
    latencias = []

    for i in range(10):
        respuesta = float(input(f"Ingresa la latencia #{i+1}: "))
        latencias.append(respuesta)
    
    latencias.sort()

    print("Latencias de menor a mayor: ")
    print(latencias)

    latencias.reverse() 
    
    print("Latencias de mayor a menor: ")
    print(latencias)
