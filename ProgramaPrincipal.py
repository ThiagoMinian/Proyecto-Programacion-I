from Emparejamientos import CrearMatrizEmparejamiento
from SimFechas import simfechas
from Fechas import CrearListaFechas
from Mostraresult import mostrar_resultados
from ModificarEquipos import CambiarNombre
def dividir_matriz(lista):
    lista1 = []
    lista2 = []
    for numero in lista:
        resultado = numero // 10
        lista1.append(resultado)
        lista2.append(numero % 10)

    return lista1, lista2

cant = int(input("Ingrese la cantidad de equipos que participaran (mínimo 2): "))
cantidadEquipos = 0
Nombresequipos = []
while cant < 2:
    print("La cantidad ingresada no es valida")
    cant = int(input("Ingrese la cantidad de equipos que participaran (mínimo 2): "))
while cantidadEquipos < cant:
    equi = input("Ingrese las universidades que van a jugar: ")
    if equi.isalpha()==True:
        Nombresequipos.append(equi)
        cantidadEquipos +=1
    else:
        print("Tu contenido tiene un carácter no referenciado a una letra")
CambiarNombre(Nombresequipos)
listafech = []
matriz = []
CrearMatrizEmparejamiento(matriz,cant)
CrearListaFechas(listafech, matriz,cant)
listEquipos1, listEquipos2 = dividir_matriz(listafech)
mostrar_resultados(listEquipos1, listEquipos2, Nombresequipos)
simfechas(listEquipos1, listEquipos2, Nombresequipos)

 


