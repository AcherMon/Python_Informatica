def cancelar_reserva (sitios,reserva_personal):
    print("Esta es la lista de sitos ya reservados")
    sitios=[]
    for n in range(10):
        sitios.append({"Reserva":"False","Nombre":""})
    asiento=sitios[1]
    asiento["Reserva"]="True"
    asiento["Nombre"]="John Doe"
    for n in range(10):
        print(sitios[n])
    reserva_personal=int(input("¿Que reserva quiere cancelar?"))
    if reserva_personal==(1):
        print("Reserva cancelada,señor John Doe")
    else:
        print ("Ese sitio no esta reservado")

        