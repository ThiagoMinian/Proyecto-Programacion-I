def actualizar_historial(nombre):
    with open("Historico.csv", "at") as arch_hist:  # Abrimos el archivo en modo lectura y escritura
        arch_tabla = open(nombre, "rt")  # Abrimos el archivo de la tabla para lectura
 
        for fila in arch_tabla:
            datos = fila.strip().split(";")
            equipo = datos[0].upper()
            victorias = int(datos[3])
            empates = int(datos[4])
            derrotas = int(datos[5])
            anotacionestot = int(datos[6])
            anotacionesR = int(datos[7])
 
            # Leer el archivo histórico línea por línea
            while True:
                posicion_actual = arch_hist.tell()  # Guardamos la posición actual
                linea = arch_hist.readline()  # Leemos la línea actual
 
                if not linea:  # Si no hay más líneas, salimos del bucle
                    break
 
                info = linea.strip().split(",")
                equipoH = info[0]
                print(equipoH)
 
                if equipo == equipoH:  # Si encontramos el equipo
                    victoriasH = str(int(info[1]) + victorias)
                    empatesH = str(int(info[2]) + empates)
                    derrotasH = str(int(info[3]) + derrotas)
                    anotacionestotH = str(int(info[4]) + anotacionestot)
                    anotacionesRH = str(int(info[5]) + anotacionesR)
 
                    # Crear la nueva línea para el equipo
                    nueva_linea = f"{equipo},{victoriasH},{empatesH},{derrotasH},{anotacionestotH},{anotacionesRH}\n"
 
                    # Usamos seek para mover el cursor a la posición actual
                    arch_hist.seek(posicion_actual)
                    # Sobrescribimos la línea con la nueva información
                    arch_hist.write(nueva_linea)
                    break  # Salimos del bucle al actualizar
 
        arch_tabla.close()  # Cerramos el archivo de la tabla