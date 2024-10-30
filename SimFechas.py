import random
from actualizar_historial import actualizar_historico

def simfechas(lista1, lista2, listanombres, fech, pos=0):

    try:
        puntos = [0] * len(listanombres)
        victorias = [0] * len(listanombres)
        derrotas = [0] * len(listanombres)
        empates = [0] * len(listanombres)
        anotaciones_totales = [0] * len(listanombres)
        anotaciones_recibidas = [0] * len(listanombres)
        partidos_jugados = [0] * len(listanombres)
        rachas_actuales = [0] * len(listanombres)
        rachas_maximas = [0] * len(listanombres)

        # Lista para almacenar los resultados de cada fecha
        resultados = []

        # Simular los partidos
        for i in range(len(lista1)):
            eq1 = lista1[i] - 1
            eq2 = lista2[i] - 1
            resultado_eq1 = random.randint(60, 100)
            resultado_eq2 = random.randint(60, 100)

            if resultado_eq1 > resultado_eq2:
                puntos[eq1] += 3
                victorias[eq1] += 1
                derrotas[eq2] += 1
                rachas_actuales[eq1] += 1
                rachas_actuales[eq2] = 0
            elif resultado_eq1 < resultado_eq2:
                puntos[eq2] += 3
                victorias[eq2] += 1
                derrotas[eq1] += 1
                rachas_actuales[eq2] += 1
                rachas_actuales[eq1] = 0
            else:
                puntos[eq1] += 1
                puntos[eq2] += 1
                empates[eq1] += 1
                empates[eq2] += 1
                rachas_actuales[eq1] = 0
                rachas_actuales[eq2] = 0

            anotaciones_totales[eq1] += resultado_eq1
            anotaciones_totales[eq2] += resultado_eq2
            anotaciones_recibidas[eq1] += resultado_eq2
            anotaciones_recibidas[eq2] += resultado_eq1
            partidos_jugados[eq1] += 1
            partidos_jugados[eq2] += 1

            if rachas_actuales[eq1] > rachas_maximas[eq1]:
                rachas_maximas[eq1] = rachas_actuales[eq1]
            if rachas_actuales[eq2] > rachas_maximas[eq2]:
                rachas_maximas[eq2] = rachas_actuales[eq2]

            # Guardar el resultado de la fecha
            resultados.append(f"FECHA {i+1}: {listanombres[eq1]} {resultado_eq1} - {resultado_eq2} {listanombres[eq2]}")

        # Imprimir resultados solo si es la última posición
        if pos == len(listanombres) - 1:
            for resultado in resultados:
                print(resultado)

            tabla_puntos = list(zip(listanombres, puntos, partidos_jugados, victorias, empates, derrotas, anotaciones_totales, anotaciones_recibidas))
            tabla_puntos_ordenada = sorted(tabla_puntos, key=lambda x: (x[1], x[6] - x[7]), reverse=True)

           # print("Tabla de puntos:")
           # print(f"{'Equipo':<10} {'Puntos':<6} {'PJ':<3} {'V':<3} {'E':<3} {'D':<3} {'Anot Tot':<10} {'Anot Rec':<10}")
           # for equipo, punto, pj, victoria, empate, derrota, anotaciones_totales, anotaciones_recibidas in tabla_puntos_ordenada:
            #    print(f"{equipo:<10} {punto:<6} {pj:<3} {victoria:<3} {empate:<3} {derrota:<3} {anotaciones_totales:<10} {anotaciones_recibidas:<10}")
            #print() 

            mayor_racha = max(rachas_maximas)
            equipo_mayor_racha = listanombres[rachas_maximas.index(mayor_racha)]
            print(f"El equipo con la mayor racha de victorias es {equipo_mayor_racha} con {mayor_racha} victorias consecutivas.")

            # Guardar los resultados en archivos
            nombre_archivo = "Torneo" + fech + ".csv"
            with open("Campeones.csv", mode="a") as arch_campeones:
                with open(nombre_archivo, "wt") as arch_tablas:
                    print("Tabla final:")
                    print(f"{'Equipo':<10} {'Puntos':<6} {'PJ':<3} {'V':<3} {'E':<3} {'D':<3} {'Anot Tot':<10} {'Anot Rec':<10} {'Dif Anot':<10}")
                    for i in range(len(tabla_puntos_ordenada)):
                        equipo, punto, pj, victoria, empate, derrota, anotaciones_totales, anotaciones_recibidas = tabla_puntos_ordenada[i]
                        diferencia_anot = anotaciones_totales - anotaciones_recibidas
                        if i == 0:
                            titulo = "Campeón"
                            arch_campeones.write(equipo + ";Fue campeón en el torneo de la fecha " + str(fech) + "\n")
                        elif i == 1:
                            titulo = "Subcampeón"
                        else:
                            titulo = ""
                        print(f"{equipo:<10} {punto:<6} {pj:<3} {victoria:<3} {empate:<3} {derrota:<3} {anotaciones_totales:<10} {anotaciones_recibidas:<10} {diferencia_anot:<10} {titulo}")
                        información_equipo = f"{equipo};{punto};{pj};{victoria};{empate};{derrota};{anotaciones_totales};{anotaciones_recibidas};{diferencia_anot}\n"
                        arch_tablas.write(información_equipo)
            # Después de imprimir la tabla de puntos y antes de la llamada a actualizar_historico, buscar al equipo descendido y guardarlo en un archivo
            if pos == len(listanombres) - 1:

                equipo_descendido = tabla_puntos_ordenada[-1][0]  #el último equipo es el descendido
                print("el equipo descendido es: ", equipo_descendido)
                with open("descendido.csv", mode="a") as arch_descendido:
                    arch_descendido.write(f"{equipo_descendido};{fech}\n")


            actualizar_historico(nombre_archivo)
            print("Archivo con los datos del torneo generado correctamente")
            print("Archivo con los equipos campeones actualizado")
            print("Archivo Historico actualizado correctamente")
            print("Archivo con los equipos descendidos actualizado correctamente")

        else:
            # Continuar la recursión con la siguiente posición
            #print(f"{listanombres[pos]}: {rachas_maximas[pos]} victorias consecutivas")
            simfechas(lista1, lista2, listanombres, fech, pos + 1)

    except IOError:
        print("Hubo un error al generar el archivo.")
    except FileNotFoundError:
        print("No se encontró el archivo para crear o editar.")