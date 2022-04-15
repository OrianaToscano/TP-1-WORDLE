from datosGuardados import *
import time
import os
#Todavía falta diseño. gg1, 2, 3 dependen de tu puntaje.
perdiste = "Te quedaste sin intentos!! Mejor suerte la próxima!"
chau = "Decidiste salir de la partida!! Chauchis"
gg1 = "Adivinaste la palabra!!!"
gg2 = "lol"
gg3 = "Ganaste pero costó"
graciasPorJugar = "gracias pa"

#Esta funcion se llama desde el def cortar juego
def pantallaFinal(num):
    if num == 0:
        print(perdiste)
    elif num == 1:
        print(chau)
    else:
        print("oo")
        """
        if puntaje > n:
            print(gg1)
        elif puntaje > z:
            print(gg2)
        else:
            print(gg3)
        

    print(ranking())"""
    return print(graciasPorJugar)




#time.sleep(30)
#os.system('cls')