from datosGuardados import *
import time
import os

#------------------------------------------- INGRESO USUARIO -------------------------------------------------

usuarioActual = None

def ingresoUsuario():
    print(f"""Hola! Bienvenidx a WORDLE!! Acá jugamos con un sistema de usuarios para que se guarden tus puntos! 
    Estos son los usuarios ya creados:
    --> {listaUsuarios} <--
    Si sos nuevx, fijate de ingresar un nombre que no este en la lista! Sino, bienvenidx otra vez!!

    -------------------------------------------------""")

    def obtenerUsuario():
        unUsuario = str(input("Ingresá tu usuario: "))

        if unUsuario not in listaUsuarios:
            print("No hay ningun usuario registrado con ese nombre! Bienvenidx!!\n-------------------------------------------------")
            user = Usuario(unUsuario)
            listaUsuarios.append(user.nombre)
            datos = open("datosGuardados.py","a")
            datos.write(f"{unUsuario} = Usuario(\"{unUsuario}\")\n")

        
        # esto se deberia guardar permanentemente en un archivo. esto es solo en ram. habria que abrir el archivo, buscar x texto y agregar lo que sea necesario, o sea user a lista}
        
        usuarioActual = user
        
        return usuarioActual

    usuarioActual = obtenerUsuario()

    time.sleep(1)
    os.system('cls')

#------------------------------------------- SELECCION DE NIVEL -------------------------------------------------

def pantallaDeInicio():
    print(
    """ .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
    | ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
    | |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
    | |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
    | |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
    | |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
    | |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
    
    >> 1. 5 LETRAS
    >> 2. 6 LETRAS
    >> 3. 7 LETRAS
    >> 4. SOLO TILDES!""")

    opcion = int(input("Ingresá el número de opción que quieras jugar!! --> "))

    while opcion < 1 or opcion > 4: 
        opcion = int(input("Noo las opciones solo son pueden ser 1, 2, 3 o 4!! Volve a intentarlo --> "))

    cantidadLetras = 0

    if opcion == 4:
        cantidadLetras = range(5,8)
    else:
        cantidadLetras = opcion+4

    
    print("Vamos a jugar!!")
    print(cantidadLetras)

    time.sleep(1)
    os.system('cls')
    
    return cantidadLetras


ingresoUsuario()