import time
import os
from dibujos import *
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

#--------------------------------------

def dibujoPorPuntaje(puntos):
    if puntos==100:
        return print(f"""Tu puntaje literalmente no puede ser mejor, deberiamos hacerte otro captcha!!! 
        {dibujo1}""")
    elif puntos<100 and puntos>=60:
        return print(f"""Felicitaciones sos bastante buenx!! 
        {dibujo2}""")
    elif puntos<60 and puntos>30:
        return print(f"""Buen puntaje, aunque falta practica no? 
        {dibujo3}""")
    elif puntos<=30 and puntos>0:
        return print(f"""Peor es nada 
        {dibujo4}""")
    elif puntos== 0:
        return print(dibujoCero)


    




#time.sleep(30)
#os.system('cls')

