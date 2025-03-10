sitios=[{"Nombre":""},{"Nombre":""},{"Nombre":""},{"Nombre":""}]
print("Hola, bienvenido a la pagina de Renfe")
print("1-Hacer Reserva")
print("2-Cancelar Reserva")
print("3-Cambiar Reserva")
accion=int(input("¿Que quiere hacer"))

from Hacer_Reserva import *
from Cancelar_Reserva import *
from Cambiar_Reserva import *


nombre=input("¿A nombre de quien?")

if accion==(1):
    reserva_personal=int(input("¿Que sitio quiere reservar?"))
    hacer_reserva(sitios,reserva_personal,nombre)
    
else:
    if accion==(2):
            reserva_personal=int(input("¿Que reserva quiere cancelar?"))
            cancelar_reserva(sitios,reserva_personal,nombre)
            
    else:
        if accion==(3):
            reserva_personal=int(input("¿A que sitio quiere cambiarse?"))
            cambiar_Reserva(sitios,reserva_personal,nombre)
            