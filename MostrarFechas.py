import random

def mostrar_fechas(lista1, lista2, listanombres):
    for i in range(len(lista1)):
        eq1 = lista1[i] - 1
        eq2 = lista2[i] - 1
       
        print(f"FECHA {i+1}: {listanombres[eq1]} - {listanombres[eq2]}")
        print()
        
  
        