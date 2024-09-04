import random 

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