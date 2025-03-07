from Hacer_Reserva import *


sitios=[{"Nombre":""},{"Nombre":""},{"Nombre":""},{"Nombre":""}]

print("Hola, bienvenido a la pagina de Renfe")
print("1-Hacer Reserva")
print("2-Cancelar Reserva")
print("3-Cambiar Reserva")
accion=int(input("¿Que quiere hacer"))



if accion==(1):
    sitios = hacer_reserva(sitios)
    print(sitios)

if accion==(2):
    sitios = cambiar_reserva(sitios)