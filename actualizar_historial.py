def actualizar_historial(nombre):
    arch_hist = open("Historico.csv", "wt")
    arch_tabla = open(nombre, "rt")
    for fila in arch_tabla:
        datos = fila.strip().split(";")
        equipo = datos[0].upper()
        victorias = datos[3]
        empates = datos[4]
        derrotas = datos[5]
        anotacionestot = datos[6]
        anotacionesR = datos[7]

        for fil in arch_hist:
            info = fila.strip().split(",")
            equipoH = info[0]
            if equipo == equipoH:
                victoriasH = info[1] + victorias
                empatesH = info[2] + empates
                derrotasH = info[3] + derrotas
                anotacionestotH = info[4] + anotacionestot
                anotacionesRH = info[5] + anotacionesR
                arch_hist.write(f"{equipo},{victoriasH},{empatesH},{derrotasH},{anotacionestotH},{anotacionesRH}\n")