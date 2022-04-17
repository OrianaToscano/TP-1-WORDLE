import random
import os
from DICCIONARIOS.diccionario_cinco_letras  import *
from DICCIONARIOS.diccionario_seis_letras import *
from DICCIONARIOS.diccionario_siete_letras import *
from DICCIONARIOS.diccionario_master import *
from DICCIONARIOS.diccionario_tildes import *
from inicio import *
from dibujos import *


def dificultadJuego(cantidadLetras):
    dicc_segun_opcion = {
        5: dicc_palabras_cinco_letras,
        6: dicc_palabras_seis_letras,
        7: dicc_palabras_siete_letras,
        range(5,8): dicc_palabras_tildes,
        9: "    Este el ranking actual!"
    }

    if cantidadLetras == 9:
        print(dicc_segun_opcion[9])
        ranking()
        return dificultadJuego(pantallaDeInicioYDificultad())
    else:
        dicc = dicc_segun_opcion[cantidadLetras]
        return dicc, cantidadLetras


def ranking():
    puntajesUsuarios = open("usuariosBaseDeDatos.txt", "r+", 3, "utf-8")
    lineas = puntajesUsuarios.read().splitlines()

    listaPuntajes = []

    for i in lineas[2::5]:
        if i != "0":
            listaPuntajes.append(i)
    puntajesUsuarios.close()    

    listaPuntajes.sort(reverse=True)


    print("USUARIO         PUNTAJE")
    for i in listaPuntajes:
        print(f"| {lineas[lineas.index(i)-1]} | _____________{i}______________")

    input("\nCuando quieras volver al menu, presiona enter!")
    os.system('cls')
    
    

########################################################################################################

#-------------------------------- PARTIDA INDIVIDUAL (1 PALABRA) --------------------------------------#

configuracionActual = dificultadJuego(pantallaDeInicioYDificultad())

if configuracionActual:

    listaUsuarios = usuariosCreados()
    puntajeTotal = 0
    rachaTotal = 0
    puntajeMaxAMin = [80,60,40,30,20,10]        #Si 1er intento: 80, 2do: 60, 3ro: 40, etc etc
    bonusMinAMax = [0,5,10,20]                  #Si 5 letras: 0, 6 letras: 5, 7 letras: 10, tildes: 20


    def finalizacionPartida(puntos):
        for i in dibujosSegunPuntaje:
            if puntos in i:
                print(f"{dibujosSegunPuntaje[i]}")
                if puntos != 0:
                    print(f"  Tu puntaje total es de {puntajeTotal}!! Acabás de sumar {puntos} puntos!")
                return puntos


    def ejecucionUnaPartida():
        #------------Declaracion de variables---------------
        dicc = configuracionActual[0]
        cantidadLetras = configuracionActual[1]
        palabraAAdivinar = dicc.get(random.randint(0, len(dicc)))
        contadorIntentos = 1
        
        
        #------------ Asignador Puntajes: DEVUELVE EL PUNTAJE POR ADIVINAR UNA PALABRA -------------------
        
        def asignarPuntaje(losIntentos):
            elPuntaje = puntajeMaxAMin[losIntentos-1]           #ej: intentos = 3 --> 3-1= 2, index 2 = 40 puntos
            if isinstance(cantidadLetras,int):
                bonus = bonusMinAMax[cantidadLetras-5]          #ej: cantidadLetras = 6 --> 6-5= 1, index 1 = 5 puntos de bonus
            else:
                bonus = bonusMinAMax[3]                         #si es tilde, la cantidad es un range. Para que no se rompa:

            return elPuntaje+bonus
        
        #-------------------------------------------------------------------------------------------------

        print(f"La palabra que tenés que averiguar tiene {len(palabraAAdivinar)} letras!")

        def corteJuego(intentos, unaRacha):
            print(f"\n >>>> Intento N° {intentos} <<<<")
            palabraIngresada = str(input("Ingrese una palabra\n>>> ")).lower()
            global puntajeTotal, rachaTotal

            # ------------------ EN CASO DE INGRESAR PALABRAS NO VALIDAS -------------------
            while len(palabraIngresada) != len(palabraAAdivinar):
                palabraIngresada = str(input(f"La palabra debe ser de {len(palabraAAdivinar)} letras! Ingrese otra\n>>> "))
            
            while cantidadLetras == range(5,8) and palabraIngresada not in dicc_totalidad_palabras.values():     # si es con tildes, chequea que este en diccionario master
                palabraIngresada = str(input("Papa frita, esa palabra no esta en el diccionario!!\n>>> "))
            
            while cantidadLetras != range(5,8) and palabraIngresada not in dicc.values():                        # si NO es con tildes, chequea en el dicc que le corresponde
                palabraIngresada = str(input("Papa frita, esa palabra no esta en el diccionario!!\n>>> "))
            # -------------------------------------------------------------------------------

            if palabraIngresada == palabraAAdivinar:
                print(comparadorDePalabras(palabraIngresada))
                print("         >>> Adivinaste la palabra!!! <<<")
                rachaTotal += 1
                puntosObtenidos = asignarPuntaje(intentos)
                puntajeTotal += puntosObtenidos
                finalizacionPartida(puntosObtenidos)
                finalizarSesionDeJuego()

            elif palabraIngresada == "chau":
                print("Decidiste salir de la partida!! Chauchis")
                finalizarSesionDeJuego()

            elif intentos > 5:
                print(comparadorDePalabras(palabraIngresada))
                escribirDatosFinales(rachaTotal,puntajeTotal)
                rachaTotal = 0
                puntosObtenidos = 0
                finalizacionPartida(puntosObtenidos)
                print(f"           Te quedaste sin intentos!!\n         La palabra a adivinar era {palabraAAdivinar.upper()}")
                finalizarSesionDeJuego()

            else:
                print(comparadorDePalabras(palabraIngresada))
                intentos += 1
                corteJuego(intentos,unaRacha)
                
        def comparadorDePalabras(palabra):
            resultado = list(palabra)

            for i in range(len(resultado)):                                #  PRIMERO AVERIGUA
                if resultado[i] == palabraAAdivinar[i]:                    #  CUALES SON []
                    resultado.pop(i)                                       #  XQ SON DE MAYOR 
                    resultado.insert(i, f"[{palabra[i]}]")                 #  IMPORTANCIA

            for i in range(len(resultado)):                                                                                             # CONDICIONES: 
                if (resultado[i] in palabraAAdivinar and                                                                                # QUE I ESTE EN LA PALABRA
                    resultado.count(f"[{palabra[i]}]") + resultado.count(f"|{palabra[i]}|") < palabraAAdivinar.count(palabra[i])):        # QUE NO HAYA MAS |I|+[I] QUE I EN LA PALABRA

                    resultado.pop(i)                                                                                             
                    resultado.insert(i, f"|{palabra[i]}|" )                                                             
                    
            
            return " ".join(resultado)

        corteJuego(contadorIntentos, rachaTotal)
        

    #------------------------------------------------------------------------------------------------------#

    ########################################################################################################


    ########################################################################################################

    #------------------ SESION DE JUEGOS (PARTIDAS INDIVIDUALES HASTA QUE EL USUARIO DECIDA PARAR) -------------------------#

    def finalizarSesionDeJuego():
        confirmacion = str(input("""
Que querés hacer?
    >> 1.Jugar otra partida! (Misma cantidad de letras)
    >> 2.Cambiar de nivel! (Jugar con otra cantidad de letras, volves al menú!)
    >> 3.Salir! (Cierra el programa)
Opcion ---> """))

        while confirmacion not in "123":
            confirmacion = str(input("Solo podes ingresar 1, 2 o 3!!"))

        os.system('cls')

        if confirmacion == "1":
            ejecucionUnaPartida()

        elif confirmacion == "2":
            global configuracionActual
            configuracionActual = dificultadJuego(pantallaDeInicioYDificultad())
            ejecucionUnaPartida()

        elif confirmacion == "3":
            escribirDatosFinales(rachaTotal,puntajeTotal)
            print("Bueno eso es todo! Esperamos que te haya gustado! <3\nCuando quieras salir, presiona enter!")
            input()        
            exit()
            
    def escribirDatosFinales(racha,puntaje):
        datosUsuario = open(f"usuariosBaseDeDatos.txt", "r", 3, "utf-8")
        linea = datosUsuario.readlines()
        index = linea.index(f"{usuarioActual}\n")
        datosUsuario.close()

        datosUsuario = open(f"usuariosBaseDeDatos.txt", "w", 3, "utf-8")
        if int(linea[index+1]) < puntaje:
            linea[index+1] = f"{puntaje}\n"
        if int(linea[index+2]) < racha:
            linea[index+2] = f"{racha}\n"
            
        datosUsuario.writelines( linea )
        datosUsuario.close()

    instrucciones()
    ejecucionUnaPartida()

    #-----------------------------------------------------------------------------------------------------------------------#

    ########################################################################################################




