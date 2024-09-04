import random

def mostrar_resultados(lista1, lista2, listanombres):
    for i in range(len(lista1)):
        eq1 = lista1[i] - 1
        eq2 = lista2[i] - 1
       
        # Generar resultados aleatorios para cada equipo
        resultado_eq1 = random.randint(60, 100)
        resultado_eq2 = random.randint(60, 100)
       
        print(f"FECHA {i+1}: {listanombres[eq1]} - {listanombres[eq2]}")
        print()