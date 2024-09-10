def CambiarNombre(listEqu):
    cambio = input("Desea cambiar el nombre de alguno de los equipos? Ingrese SI o NO: ")
    cambio = cambio.upper()
    while (cambio.isalpha == False) or (cambio != "SI" and cambio != "NO"):
        print("La respuesta ingresada no es válida")
        cambio = input("Ingrese SI si quiere realizar cambios o NO si no lo desea: ")
        cambio = cambio.upper()
    while cambio == "SI":
        Acambiar = int(input("Ingrese el número del equipo que quiere cambiar: "))
        while Acambiar <= 0 or Acambiar > len(listEqu):
            print("No hay ningún equipo en esa posición")
            Acambiar = int(input("Ingrese un número de equipo que sea válido: "))
        NuevoNombre = input("Ingrese el nuevo nombre que le quiere asignar a ese equipo: ")
        listEqu[Acambiar - 1:Acambiar] = [NuevoNombre]
        cambio = input("Desea cambiar el nombre de alguno de los equipos? Ingrese SI o NO: ")
        cambio = cambio.upper()
        while (cambio.isalpha == False) or (cambio != "SI" and cambio != "NO"):
            print("La respuesta ingresada no es válida")
            cambio = input("Ingrese SI si quiere realizar cambios o NO si no lo desea: ")
            cambio = cambio.upper()
    return(listEqu)