from listas import InventarioDispositivos, VentasSemanales, TemperaturasManagua, dispositivos_sinConexion, Ordenamientolatencias
from tuplas import coordenadas_deunLocal,  dimensiones_caja, registroEstudiante, puntosRuta, retornoMultiple
from conjuntos import usuariosUnicos, aplicacionesCompartidas, aplicacionesExclusivas, catalogoTecnologico_consolidado, UsuariosPlataformas
from diccionarios import fichaDispositivo, directorioUsuarios, conteoAccesos, IncidentesxTecnico, actualizacionDispositivos
from combinadas import listaDispositivos_estructurados, consumoDatos_xdia, sistemasOperativos_unicos, calificaciones_xestudiante, registroSolicitudes_soporte
from zips import estudiantesNotas, dispositivos_direccionesIP, dispositivoIP_estado, comparacionConsumo_datos, construccionRegistros_usuarios

def main ():
    print("********* MENU DE LOS EJERCICIOS *********")
    print("")
    print("********** Ejercicios de listas **********")
    print("1. Inventario de dispositivos")
    print("2. Ventas semanales")
    print("3. Temperaturas de Managua")
    print("4. Dispositivos sin conexión")
    print("5. Ordenamiento de latencias")
    print("")
    print("********** Ejercicios de tuplas **********")
    print("6. Coordenadas de un local")
    print("7. Dimensiones de una caja")
    print("8. Registro de estudiante")
    print("9. Puntos de una ruta")
    print("10. Retorno múltiple")
    print("")
    print("********* Ejercicios de conjuntos *********")
    print("11. Usuarios únicos")
    print("12. Aplicaciones compartidas")
    print("13. Aplicaciones exclusivas")
    print("14. Catálogo tecnológico consolidado")
    print("15. Usuarios de plataformas")
    print("")
    print("******* Ejercicios de diccionarios ********")
    print("16. Ficha de dispositivo")
    print("17. Directorio de usuarios")
    print("18. Conteo de accesos")
    print("19. Incidentes por técnico")
    print("20. Actualización de dispositivos")
    print("")
    print("******** Ejercicios de combinados *********")
    print("21. Lista de dispositivos estructurados")
    print("22. Consumo de datos por día")
    print("23. Sistemas operativos únicos")
    print("24. Calificaciones por estudiante")
    print("25. Registro de solicitudes de soporte")
    print("")
    print("******* Ejercicios de zip() ********")
    print("26. Estudiantes y notas")
    print("27. Dispositivos y direcciones IP")
    print("28. Dispositivo, IP y estado")
    print("29. Comparación de consumo de datos")
    print("30. Construcción de registros de usuarios")
    
    
    opc = int(input("Ingrese el número del ejercicio que desea ejecutar: "))
    match opc:
        case 1:
            InventarioDispositivos()
        case 2: 
            VentasSemanales()
        case 3: 
            TemperaturasManagua()
        case 4:
            dispositivos_sinConexion()
        case 5: 
            Ordenamientolatencias()
        case 6: 
            coordenadas_deunLocal()
        case 7:
            dimensiones_caja()
        case 8:
            registroEstudiante()
        case 9:
            puntosRuta()
        case 10:
            retornoMultiple()
        case 11:
            usuariosUnicos()
        case 12:
            aplicacionesCompartidas()
        case 13:
            aplicacionesExclusivas()
        case 14:
            catalogoTecnologico_consolidado()
        case 15:
            UsuariosPlataformas()
        case 16:
            fichaDispositivo()
        case 17:
            directorioUsuarios()
        case 18:
            conteoAccesos()
        case 19:
            IncidentesxTecnico()
        case 20:
            actualizacionDispositivos()
        case 21:
            listaDispositivos_estructurados()
        case 22: 
            consumoDatos_xdia()
        case 23: 
            sistemasOperativos_unicos()
        case 24:
            calificaciones_xestudiante()
        case 25: 
            registroSolicitudes_soporte()
        case 26: 
            estudiantesNotas()
        case 27:
            dispositivos_direccionesIP()
        case 28:
            dispositivoIP_estado()
        case 29:
            comparacionConsumo_datos()
        case 30:
            construccionRegistros_usuarios()
    
main()
    



