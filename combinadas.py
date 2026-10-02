def listaDispositivos_estructurados():
    # Crea una lista de diccionarios donde cada diccionario represente un producto.
    # Muestra solo los dispositivos cuyo precio sea mayor que un valor dado.

    dispositivos = [
        {"nombre": "Laptop", "precio": 800},
        {"nombre": "Tablet", "precio": 400},
        {"nombre": "Celular", "precio": 600},
        {"nombre": "Monitor", "precio": 300}
    ]

    valor = float(input("Ingrese el precio minimo: "))

    for dispositivo in dispositivos:
        if dispositivo["precio"] > valor:
            print(dispositivo)

def consumoDatos_xdia():
    # Usa un diccionario cuyos valores sean listas de ventas. Calcula el total vendido por cada día.

    ventas = {
        "Lunes": [100, 150, 200],
        "Martes": [120, 180, 90],
        "Miercoles": [200, 250, 100]
    }

    for dia in ventas:
        total = sum(ventas[dia])
        print(f"{dia}: {total}")

def sistemasOperativos_unicos():
    # A partir de una lista de diccionarios de dispositivos, construye un conjunto con las
    # categorías diferentes.

    dispositivos = [
        {"nombre": "Laptop", "sistema": "Windows"},
        {"nombre": "Celular", "sistema": "Android"},
        {"nombre": "Tablet", "sistema": "Android"},
        {"nombre": "MacBook", "sistema": "macOS"}
    ]

    sistemas = set()

    for dispositivo in dispositivos:
        sistemas.add(dispositivo["sistema"])

    print(sistemas)

def calificaciones_xestudiante():
    # Crea un diccionario donde cada estudiante tenga como valor una lista de notas.
    # Calcula el promedio de cada estudiante.

    estudiantes = {
        "Zack": [100, 95, 98],
        "Anne": [90, 92, 95],
        "Brennan": [100, 100, 98]
    }

    for estudiante in estudiantes:
        promedio = sum(estudiantes[estudiante]) / len(estudiantes[estudiante])
        print(f"{estudiante}: {promedio}")

def registroSolicitudes_soporte():
    # Representa cada pedido como un diccionario que incluya cliente y una lista de dispositivos.
    # Muestra cuántos dispositivos contiene cada pedido.

    pedidos = [
        {"cliente": "Zack", "dispositivos": ["Laptop", "Celular"]},
        {"cliente": "Anne", "dispositivos": ["Tablet", "Laptop", "Monitor"]}
    ]

    for pedido in pedidos:
        cantidad = len(pedido["dispositivos"])
        print(f"{pedido['cliente']}: {cantidad} dispositivos")