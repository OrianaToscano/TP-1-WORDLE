import time
import os

#------------------------------------------- INGRESO USUARIO -------------------------------------------------

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

usuarioActual = None

def usuariosCreados():
        usuariosBase = open("usuariosBaseDeDatos.txt", "r+", 3, "utf-8")
        lineas = usuariosBase.read().splitlines()

        listaUsuarios = []

        for i in lineas[1::5]:
            listaUsuarios.append(i)    
        usuariosBase.close()

        return listaUsuarios

def ingresoUsuario():
    
    listaUsuarios = usuariosCreados()

    print(f"""Hola! Bienvenidx a WORDLE!! 
Acá jugamos con un sistema de usuarios para que se guarden tus puntos! 
Estos son los usuarios ya creados:
--> {listaUsuarios} <--
Si sos nuevx, fijate de ingresar un nombre que no este en la lista! Sino, bienvenidx otra vez!!
    -------------------------------------------------""") 

    unUsuario = str(input("Ingresá tu usuario: "))

    if unUsuario not in listaUsuarios:
        print("No hay ningun usuario registrado con ese nombre! Bienvenidx!!\n-------------------------------------------------")
        datosUsuario = open(f"usuariosBaseDeDatos.txt", "a+", 3, "utf-8")
        datosUsuario.write("#La primera linea será el nombre, la segunda su puntaje acumulado y la tercera su racha\n")
        datosUsuario.write(f"{unUsuario}\n0\n0\n \n")
        datosUsuario.close()
    else:
        print(f"\nYa hay un usuario con ese nombre, bienvenidx de vuelta {unUsuario}!!")
    
    usuarioActual = unUsuario

     
    time.sleep(1)
    cls()

    return usuarioActual

usuarioActual = ingresoUsuario()

#------------------------------------------- SELECCION DE NIVEL -------------------------------------------------

def pantallaDeInicioYDificultad():
    print(
    f"""                                        ¡Bienvenidx {usuarioActual}!
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
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

ELEGÍ LA CANTIDAD DE LETRAS CON LAS QUE QUIERAS JUGAR!! (A mayor cantidad, mayor bonus!)
    >> 1. 5 LETRAS
    >> 2. 6 LETRAS
    >> 3. 7 LETRAS
    >> 4. SOLO TILDES

    >> 5. RANKING
    """)

    opcion = str(input("Ingresá el número de opción que quieras jugar!! --> "))

    while opcion not in "123456": 
        opcion = str(input("Noo las opciones solo son pueden ser 1, 2, 3 o 4!! Volve a intentarlo --> "))

    cantidadLetras = 0

    if opcion == "4":
        cantidadLetras = range(5,8)
    else:
        cantidadLetras = int(opcion) + 4

    
    print("Vamos a jugar!!")

    time.sleep(1)
    cls()
    
    return cantidadLetras

#------------------------------------------- INSTRUCCIONES -------------------------------------------------

def instrucciones():
    print("""
Las instrucciones del juego son las siguientes!
Vas a tener 6 intentos para intentar averiguar una palabra con una cierta cantidad de letras (vos podes elegir cuantas!). 
Cuando ingreses una palabra, esta volverá a mostrarse en pantalla con ciertos símbolos, estos son:
    [ a ] ---> Significa que la letra está en la palabra y en la posición correcta!
    | a | ---> Significa que la letra está en la palabra, pero no en la posición correcta!
      a   ---> Significa que la letra NO está en la palabra!
""")



    
