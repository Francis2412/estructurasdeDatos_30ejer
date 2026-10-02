def usuariosUnicos():
    #Dada una lista con nombres repetidos de clientes, crea un conjunto y
    #muestra cuántos clientes diferentes existen.
    nombres = ["Brennan", "Zack", "Jack", "Angela", "Booth", "Zack", "Angela", "Zack"]
    nombres = set(nombres)
    print(nombres)
    print(f"Clientes diferentes: {len(nombres)}")

def aplicacionesCompartidas():
    #Dos proveedores ofrecen diferentes dispositivos. Identifica cuáles aparecen en ambos catálogos.
    proveedor1 = {"Laptop", "Tablet", "Celular", "Consola"}
    proveedor2 = {"Celular", "Tablet", "Audifonos", "Monitor"}

    compartidos = proveedor1 & proveedor2

    print("Dispositivos en ambos catálogos:")
    print(compartidos)

def aplicacionesExclusivas():
    #Determina qué dispositivos ofrece el proveedor A que no ofrece el proveedor B.
    proveedorA = {"Laptop", "Tablet", "Celular", "Consola"}
    proveedorB = {"Celular", "Tablet", "Audifonos", "Monitor"}
    
    dif = proveedorA - proveedorB
    
    print("Dispositivos exclusivos del proveedor A::")
    print(dif)

def catalogoTecnologico_consolidado(): 
    #Une los dispositivos de dos proveedores sin conservar duplicados y muestra el catálogo final.
    proveedor1 = {"Laptop", "Tablet", "Celular", "Consola"}
    proveedor2 = {"Celular", "Tablet", "Audifonos", "Monitor"}

    sindupli = proveedor1 | proveedor2

    print("Catálogo final sin duplicados")
    print(sindupli)

def UsuariosPlataformas():
    #Dos listas representan personas que asistieron a dos eventos.
    #Determina quiénes asistieron a ambos y quiénes asistieron solo al primero.
    evento1 = ["Zack", "Anne", "Jack", "Daisy", "Sweets", "Angela"]
    evento2 = ["Zack", "Anne", "Angela", "Booth", "Brennan", "Daisy"]
    
    evento1 = set(evento1)
    evento2 = set(evento2)

    ambos = evento1 & evento2
    solo1erevento = evento1 - evento2

    print("Asistieron a ambos eventos: ")
    print(ambos)
    print("Asistieron solo al primer: ")
    print(solo1erevento)
