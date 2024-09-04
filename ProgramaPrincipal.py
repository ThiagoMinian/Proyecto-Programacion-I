from Emparejamientos import CrearMatrizEmparejamiento
import random 

#def imprimirlista(lista):
 #   for i in range(len(lista)):
   #     print(lista[i],end="   ")
   # print()

def CrearListaFechas(ListaFechas,Emparej,ce):
    fila = random.randint(0,ce-1)
    columna = random.randint(0,ce-1)
    k = 0
    while k < (ce*ce) - ce :
        partido = Emparej[fila][columna]
        if ListaFechas.count(partido) == 0 and partido != "X":
            ListaFechas.append(partido)
            k = k + 1
        fila = random.randint(0,ce-1)
        columna = random.randint(0,ce-1)

def dividir_matriz(lista):
    lista1 = []
    lista2 = []
    for numero in lista:
        resultado = numero // 10
        lista1.append(resultado)
        lista2.append(numero % 10)

    return lista1, lista2

def mostrar_resultados(lista1, lista2, listanombres):
    for i in range(len(lista1)):
        eq1 = lista1[i] - 1
        eq2 = lista2[i] - 1
       
        # Generar resultados aleatorios para cada equipo
        resultado_eq1 = random.randint(60, 100)
        resultado_eq2 = random.randint(60, 100)
       
        print(f"FECHA {i+1}: {listanombres[eq1]} - {listanombres[eq2]}")
 
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
#for filas in matriz:
    #print(filas)
CrearListaFechas(listav, matriz,cant)
equipo1, equipo2 = dividir_matriz(listav)
#imprimirlista(listav)
#imprimirlista(equipo1)
#imprimirlista(equipo2)
mostrar_resultados(equipo1, equipo2, equipos)


