def CrearMatrizEmparejamiento (matriz,ce):
    for f in range (ce):
        matriz.append([])
        for c in range (ce):
            if f != c:
                matriz[f].append(((f+1)* 10) + (c+1))
            else:
                matriz[f].append("X")
