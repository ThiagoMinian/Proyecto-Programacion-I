def actualizar_historico(nombre):
    # leemos el archivo histórico
    with open("Historico.csv", "rt") as arch_hist:
        registros = arch_hist.readlines()

    # se ee el archivo de torneo
    with open(nombre, "rt") as arch_torn:
        datos_torneos = arch_torn.readlines()

    # se reescribe el archivo historico
    with open("Historico.csv", "wt") as arch_hist:
        for fila in datos_torneos:
            datos = fila.strip().split(";")
            equipo = datos[0].upper()
            victorias = int(datos[3])
            empates = int(datos[4])
            derrotas = int(datos[5])
            anot_tot = int(datos[6])
            anot_rec = int(datos[7])
            
            for i, linea in enumerate(registros):
                informacion = linea.strip().split(",")
                equipoH = informacion[0]
                
                if equipo == equipoH:
                    informacion[1] = str(int(informacion[1]) + victorias)
                    informacion[2] = str(int(informacion[2]) + empates)
                    informacion[3] = str(int(informacion[3]) + derrotas)
                    informacion[4] = str(int(informacion[4]) + anot_tot)
                    informacion[5] = str(int(informacion[5]) + anot_rec)
                    
                    nuevos_datos = informacion[0] + "," + informacion[1] + "," + informacion[2] + "," + informacion[3] + "," + informacion[4] + "," + informacion[5] + "\n"
                    registros[i] = nuevos_datos
                    print("Actualizando registro con los siguientes datos:", registros[i])

        arch_hist.writelines(registros)