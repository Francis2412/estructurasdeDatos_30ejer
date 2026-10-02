def fichaDispositivo():
    #Crea un diccionario para representar modelo, dirección IP, estado y sistema operativo de un producto.
    #Consulta y modifica la existencia.

    producto = {
        "modelo": "Samsung S26",
        "ip": "252.250.162.206 (IPv4)",
        "estado": "Activo",
        "sistema operativo": "Android"
    }

    accion = int(input("¿Que accion desea realizar? Consultar(1), Modificar(2): "))

    if accion == 1:
        info = input("¿Qué información desea saber sobre el producto?: ")

        if info == "modelo":
            print(producto["modelo"])
        elif info == "ip":
            print(producto["ip"])
        elif info == "estado":
            print(producto["estado"])
        elif info == "sistema operativo":
            print(producto["sistema operativo"])
        else:
            print("Información no disponible.")

    elif accion == 2:
        info = input("¿Qué información desea modificar?: ")
        nuevo = input("Ingrese el nuevo valor: ")
        producto[info] = nuevo
        print("Información modificada correctamente.")

    else:
        print("Accion no disponible...")

def directorioUsuarios():

    #Construye un diccionario donde la clave sea el nombre y el valor sea el teléfono.
    #Permite consultar un contacto.

    usuario = {
        "Zack Addy": "1234-5678"
    }

    consultar = input("¿Que usuario desea consultar?: ")

    if consultar in usuario:
        print(usuario[consultar])
    else:
        print("Usuario no encontrado.")

def conteoAccesos():
    # Dada una lista de nombres de accesos registrados, utiliza un diccionario para contar
    # cuántas veces aparece cada dispositivo.

    accesos = ["Laptop", "Celular", "Laptop", "Tablet", "Celular", "Laptop"]

    conteo = {}

    for dispositivo in accesos:
        if dispositivo in conteo:
            conteo[dispositivo] += 1
        else:
            conteo[dispositivo] = 1

    print(conteo)

def IncidentesxTecnico():
    # Almacena en un diccionario el total vendido por cada técnico y determina quién alcanzó la mayor venta.

    ventas = {
        "Carlos": 1500,
        "Maria": 2300,
        "Pedro": 1800,
        "Ana": 2500
    }

    mayor = max(ventas.values())

    for tecnico in ventas:
        if ventas[tecnico] == mayor:
            print(f"El tecnico con mayor venta es {tecnico}: {mayor}")

def actualizacionDispositivos():
    # Representa el inventario como diccionario producto-existencia.
    # Procesa varias entradas y salidas actualizando los valores.

    inventario = {
        "Laptop": 10,
        "Tablet": 15,
        "Celular": 20
    }

    inventario["Laptop"] += 5
    inventario["Tablet"] -= 3
    inventario["Celular"] += 2

    print(inventario)
