print("Esta es la lista de sitos ya reservados")
sitios=[]
numero=10
for n in range(numero):
    sitios.append({"Reserva":"False","Nombre":""})
asiento=sitios[1]
asiento["Reserva"]="True"
asiento["Nombre"]="John Doe"
for n in range(numero):
    print(sitios[n])
reserva_personal=int(input("¿En que sitio estaba?"))
if reserva_personal==(1):
    reserva_personal=int(input("¿A que sitio quiere cambiarse?"))
    asiento=sitios[reserva_personal]
    asiento["Reserva"]="True"
    asiento["Nombre"]="John Doe"
    asiento=sitios[1]
    asiento["Reserva"]="False"
    asiento["Nombre"]=""
    for n in range(numero):
        print(sitios[n])
else:
    print ("Ese sitio no esta ocupado")