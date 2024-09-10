from Emparejamientos import CrearMatrizEmparejamiento
from SimFechas import simfechas
from Fechas import CrearListaFechas
from Mostraresult import mostrar_resultados

def dividir_matriz(lista):
    lista1 = []
    lista2 = []
    for numero in lista:
        resultado = numero // 10
        lista1.append(resultado)
        lista2.append(numero % 10)

    return lista1, lista2

cant = int(input("Ingrese la cantidad de equipos que participaran (mínimo 2): "))
cantidad = 0
equipos = []
while cant < 2:
    print("Cantida ingresada no es valida")
    cant = int(input("Ingrese la cantidad de equipos que participaran (mínimo 2): "))
while cantidad < cant:
    equi = input("Ingrese las universidades que van a jugar: ")
    if equi.isalpha()==True:
        equipos.append(equi)
        cantidad +=1
    else:
        print("Tu contenido tiene un carácter no referenciado a una letra")
listav = []
matriz = []
CrearMatrizEmparejamiento(matriz,cant)
CrearListaFechas(listav, matriz,cant)
equipo1, equipo2 = dividir_matriz(listav)
mostrar_resultados(equipo1, equipo2, equipos)
simfechas(equipo1, equipo2, equipos)

 


