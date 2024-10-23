import random
 
def generardatos():
   
    facultad = {valor: random.randint(50, 200) for valor in ["Victorias", "Empates", "Derrotas", "Anot_tot", "Anot_rec" ]}
   
    facultad["Anot_tot"] * 30
    facultad["Anot_rec"] * 30 #Para que tengan mas coherencia la cantidad de puntos
   
    return facultad
 
 
def generarhistorico():
    datosuba = generardatos()
    datosuade= generardatos()
    datosuca = generardatos()
    datosutn = generardatos()
    datosusema = generardatos()
    datosuai = generardatos()
    datosup = generardatos()
    datosunlam = generardatos()
   
    estadistica = {
        "UBA": datosuba,
        "UADE": datosuade,
        "UCA": datosuca,
        "UTN": datosutn,
        "USEMA": datosusema,
        "UAI": datosuai,
        "UP": datosup,
        "UNLAM": datosunlam
        }
   
    #for universidad,datos in estadistica.items():
    #    print(f"{universidad}:{datos}")
           
   
    try:
        archivo = open(r"Historico.csv" ,mode = "wt")
        archivo.write("Tabla Historica de Equipos\n")
        archivo.write("Universidad, victorias, Empates, derrotas, Anot_tot, Anot_rec \n")
        for universidad, datos in estadistica.items():
                archivo.write(f"{universidad},{datos['Victorias']},{datos['Empates']},{datos['Derrotas']},{datos['Anot_tot']},{datos['Anot_rec']}\n")
    except IOError as msg:
        print(msg)
        print("No se pudo abrir el archivo historico")        
   
    print("-" * 75)    
    print(f"{'Universidad':<12} {'Victorias':<12} {'Empates':<12} {'Derrotas':<12} {'Anot_tot':<12} {'Anot_rec':<12}")
    print("-" * 75)
 
    # Imprimir datos de cada universidad con formato alineado
    for universidad, datos in estadistica.items():
        print(f"{universidad:<12} {datos['Victorias']:<12} {datos['Empates']:<12} {datos['Derrotas']:<12} {datos['Anot_tot']:<12} {datos['Anot_rec']:<12}")  
