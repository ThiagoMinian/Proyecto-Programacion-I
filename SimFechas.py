
import random

def simfechas(lista1, lista2, listanombres):
    # Inicializar las listas de puntos, victorias, derrotas, empates, anotaciones y anotaciones recibidas
    puntos = [0] * len(listanombres)
    victorias = [0] * len(listanombres)
    derrotas = [0] * len(listanombres)
    empates = [0] * len(listanombres)
    anotaciones_totales = [0] * len(listanombres)
    anotaciones_recibidas = [0] * len(listanombres)
    partidos_jugados = [0] * len(listanombres)
    for i in range(len(lista1)):
        eq1 = lista1[i] - 1
        eq2 = lista2[i] - 1
        # Generar resultados aleatorios para cada equipo
        resultado_eq1 = random.randint(60, 100)
        resultado_eq2 = random.randint(60, 100)
        # Actualizar puntos, victorias, derrotas, empates, anotaciones y anotaciones recibidas según el resultado
        if resultado_eq1 > resultado_eq2:
            puntos[eq1] += 3
            victorias[eq1] += 1
            derrotas[eq2] += 1
        elif resultado_eq1 < resultado_eq2:
            puntos[eq2] += 3
            victorias[eq2] += 1
            derrotas[eq1] += 1
        else:
            puntos[eq1] += 1
            puntos[eq2] += 1
            empates[eq1] += 1
            empates[eq2] += 1
        # Actualizar anotaciones totales y recibidas
        anotaciones_totales[eq1] += resultado_eq1
        anotaciones_totales[eq2] += resultado_eq2
        anotaciones_recibidas[eq1] += resultado_eq2
        anotaciones_recibidas[eq2] += resultado_eq1
        # Actualizar partidos jugados
        partidos_jugados[eq1] += 1
        partidos_jugados[eq2] += 1
        # Imprimir el resultado del partido
        print(f"FECHA {i+1}: {listanombres[eq1]} {resultado_eq1} - {resultado_eq2} {listanombres[eq2]}")
        # Crear una lista de tuplas (equipo, puntos, partidos jugados, victorias, empates, derrotas)
        tabla_puntos = list(zip(listanombres, puntos, partidos_jugados, victorias, empates, derrotas))
        # Ordenar la tabla de puntos por puntos en orden descendente
        tabla_puntos_ordenada = sorted(tabla_puntos, key=lambda x: x[1], reverse=True)
        # Imprimir la tabla de puntos actualizada con encabezados
        print("Tabla de puntos:")
        print(f"{'Equipo':<10} {'Puntos':<6} {'PJ':<3} {'V':<3} {'E':<3} {'D':<3}")
        for equipo, punto, pj, victoria, empate, derrota in tabla_puntos_ordenada:
            print(f"{equipo:<10} {punto:<6} {pj:<3} {victoria:<3} {empate:<3} {derrota:<3}")
        print()
    # Imprimir la tabla final con Campeón y Subcampeón
    print("Tabla final:")
    print(f"{'Equipo':<10} {'Puntos':<6} {'PJ':<3} {'V':<3} {'E':<3} {'D':<3} {'Anot Tot':<10} {'Anot Rec':<10} {'Dif Anot':<10}")
    for i, (equipo, punto, pj, victoria, empate, derrota) in enumerate(tabla_puntos_ordenada):
        anotaciones_tot = anotaciones_totales[listanombres.index(equipo)]
        anotaciones_rec = anotaciones_recibidas[listanombres.index(equipo)]
        diferencia_anot = anotaciones_tot - anotaciones_rec
        if i == 0:
            titulo = "Campeón"
        elif i == 1:
            titulo = "Subcampeón"
        else:
            titulo = ""
        print(f"{equipo:<10} {punto:<6} {pj:<3} {victoria:<3} {empate:<3} {derrota:<3} {anotaciones_tot:<10} {anotaciones_rec:<10} {diferencia_anot:<10} {titulo}")
    print()
 