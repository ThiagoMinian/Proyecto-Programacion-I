from Emparejamientos import CrearMatrizEmparejamiento
from SimFechas import simfechas
from Fechas import CrearListaFechas
from MostrarFechas import mostrar_fechas
from ModificarEquipos import CambiarNombre
from Generar_historico import generarhistorico
from Actualizar_historial import actualizar_historial

def dividir_matriz(lista):
    lista1 = []
    lista2 = []
    for numero in lista:
        resultado = numero // 10
        lista1.append(resultado)
        lista2.append(numero % 10)

    return lista1, lista2

def es_año_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def validar_fecha(año, mes, dia):
    if not (1950 <= año <= 2024):
        raise ValueError("El año debe estar entre 1950 y 2024.")
    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12.")

    dias_por_mes = [31, 29 if es_año_bisiesto(año) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not (1 <= dia <= dias_por_mes[mes - 1]):
        raise ValueError(f"El día {dia} no es válido para el mes {mes}.")

try:
    año = int(input("Ingrese el año en el que se juega el torneo (1950-2024): "))
    validar_fecha(año, 1, 1)

    mes = int(input("Ingrese el mes en el que se juega el torneo (1-12): "))
    validar_fecha(año, mes, 1)

    dia = int(input("Ingrese el día en el que se juega el torneo: "))
    validar_fecha(año, mes, dia)

    fecha = f"{dia},{mes},{año}"
    cant = int(input("Ingrese la cantidad de equipos que participaran (mínimo 2): "))
    cantidadEquipos = 0
    Nombresequipos = []

    while cant < 2:
        print("La cantidad ingresada no es válida.")
        cant = int(input("Ingrese la cantidad de equipos que participaran (mínimo 2): "))

    while cantidadEquipos < cant:
        equi = input("Ingrese las universidades que van a jugar: ")
        if equi.isalpha():
            Nombresequipos.append(equi)
            cantidadEquipos += 1
        else:
            print("Tu contenido tiene un carácter no referenciado a una letra.")

    respuesta = input("Desea generar el historico de los equipos? ")
    if respuesta == "si":
        generarhistorico()
    CambiarNombre(Nombresequipos)
    listafech = []
    matriz = []
    CrearMatrizEmparejamiento(matriz, cant)
    CrearListaFechas(listafech, matriz, cant)
    listEquipos1, listEquipos2 = dividir_matriz(listafech)
    mostrar_fechas(listEquipos1, listEquipos2, Nombresequipos)
    simfechas(listEquipos1, listEquipos2, Nombresequipos, fecha)
    actualizar_historial()

except ValueError as msg:
    print(f"Error: {msg}")
except IOError:
    print("Error: Ocurrió un problema al leer o escribir en el archivo.")
except IndexError:
    print("Error: Acceso a índice fuera de rango. Verifica que las listas y matrices estén bien formadas.")
except TypeError:
    print("Error: Ocurrió un problema con los tipos de datos. Verifica que las funciones devuelvan los datos esperados.")
