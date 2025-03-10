def hacer_reserva (sitios,reserva_personal,nombre):
    sitios=[]
    print ("Esta es la lista de sitios ya reservados")
    for n in range(10):
        sitios.append({"Reserva":"False","Nombre":""})
        asiento=sitios[1]
        asiento["Reserva"]="True"
        asiento["Nombre"]="John Doe"
    for n in range(10):
        print(sitios[n])
        reserva_personal=int(input("¿Que sitio quiere reservar?"))
    if reserva_personal==(1):
        print ("Ese sitio ya esta ocupado")
    else:
        if reserva_personal>9:
            print("Ese sitio no existe")
        else:
            nombre=input("¿A nombre de quien?")
            asiento=sitios[reserva_personal]
            asiento["Reserva"]="True"
            asiento["Nombre"]=nombre
            for n in range(10):
                print(sitios[n])


                