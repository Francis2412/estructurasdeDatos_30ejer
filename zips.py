def estudiantesNotas():
    # Relaciona dos listas, una de estudiantes y otra de notas, utilizando zip().
    # Muestra cada estudiante junto con su nota.

    estudiantes = ["Zack", "Anne", "Brennan"]
    notas = [100, 95, 98]

    for estudiante, nota in zip(estudiantes, notas):
        print(f"{estudiante}: {nota}")

def dispositivos_direccionesIP():
    # Construye un diccionario dispositivo-IP a partir de dos listas relacionadas utilizando zip().

    dispositivos = ["Laptop", "Celular", "Tablet"]
    ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

    resultado = dict(zip(dispositivos, ips))

    print(resultado)

def dispositivoIP_estado():
    # Relaciona tres listas mediante zip() para mostrar en cada recorrido el nombre, modelo,
    # dirección IP y estado de un dispositivo.

    nombres = ["Laptop", "Celular", "Tablet"]
    modelos = ["Dell", "Samsung", "Lenovo"]
    ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]
    estados = ["Activo", "Inactivo", "Activo"]

    for nombre, modelo, ip, estado in zip(nombres, modelos, ips, estados):
        print(f"Nombre: {nombre} | Modelo: {modelo} | IP: {ip} | Estado: {estado}")

def comparacionConsumo_datos():
    # Relaciona el consumo de datos de dos semanas y muestra la diferencia entre ambas para cada día.

    semana1 = [10, 15, 12, 20, 18]
    semana2 = [12, 13, 15, 18, 20]

    for i, (consumo1, consumo2) in enumerate(zip(semana1, semana2)):
        diferencia = consumo2 - consumo1
        print(f"Dia {i + 1}: diferencia = {diferencia}")

def construccionRegistros_usuarios():
    # Usa listas de nombres, edades y ciudades para construir una lista de diccionarios mediante zip().

    nombres = ["Zack", "Anne", "Brennan"]
    edades = [24, 20, 35]
    ciudades = ["Washington", "Managua", "Washington"]

    usuarios = []

    for nombre, edad, ciudad in zip(nombres, edades, ciudades):
        usuario = {
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad
        }

        usuarios.append(usuario)

    print(usuarios)