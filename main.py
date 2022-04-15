import random
from pantallaInicio import *
from pantallaExit import *



cantidadLetras = pantallaDeInicio()
listaUsuarios = usuariosCreados()
puntaje=0

# -----------Asignador de diccionarios--------------

if cantidadLetras == 5:
    from DICCIONARIOS.diccionario_cinco_letras import *
    dicc = dicc_palabras_cinco_letras
    puntaje += 5
elif cantidadLetras == 6:
    from DICCIONARIOS.diccionario_seis_letras import *
    dicc = dicc_palabras_seis_letras
    puntaje += 10
elif cantidadLetras == 7:
    from DICCIONARIOS.diccionario_siete_letras import *
    dicc = dicc_palabras_siete_letras
    puntaje += 15
elif cantidadLetras == range(5,8):
    from DICCIONARIOS.diccionario_tildes import *
    from DICCIONARIOS.diccionario_master import *
    dicc = dicc_palabras_tildes
    puntaje += 20


#---------------------------------------------------

def escribirDatosFinales(racha,puntaje):
    datosUsuario = open(f"usuariosBaseDeDatos.txt", "r+", 3, "utf-8")
    linea = datosUsuario.readlines()
    datosUsuario.seek(0)
    index = linea.index(f"{usuarioActual}\n")

    if int(linea[index+1]) < puntaje:
        linea[index+1] = f"{puntaje}\n"
        datosUsuario.writelines( linea )

    if int(linea[index+2]) < racha:
        linea[index+2] = f"{racha}\n"
        datosUsuario.writelines( linea )
        
    datosUsuario.close()

instrucciones()

def ejecucionUnaPartida():
    #------------Declaracion de variables---------------

    palabraAAdivinar = dicc.get(random.randint(0, len(dicc)))
    contadorIntentos = 1
    racha = 0
    
    
    #---------------------------------------------------
    def asignarPuntaje(elPuntaje, losIntentos):
        if losIntentos == 1:
            elPuntaje += 80
        elif losIntentos == 2:
            elPuntaje += 60
        elif losIntentos == 3:
            elPuntaje += 40
        elif losIntentos == 4:
            elPuntaje += 30
        elif losIntentos == 5:
            elPuntaje += 20
        elif losIntentos ==6:
            elPuntaje += 10
            
        return(elPuntaje)

    #---------------------------------------------------

    print(f"La palabra que tenés que averiguar tiene {len(palabraAAdivinar)} letras!")


    def corteJuego(intentos, unaRacha, unPuntaje):
        print(f"\n >>>> Intento N° {intentos} <<<<")
        palabraIngresada = str(input("Ingrese una palabra\n>>> ")).lower()

        if intentos > 6:
            unPuntaje=0
            return print(f"\nTe quedaste sin intentos!!\n La palabra a adivinar era {palabraAAdivinar.upper()} \nMejor suerte la próxima! {dibujoPorPuntaje(unPuntaje)}")

        elif palabraIngresada == "chau":
            return print("Decidiste salir de la partida!! Chauchis")

        elif palabraIngresada == palabraAAdivinar:
            unaRacha += 1
            escribirDatosFinales(unaRacha, unPuntaje)
            unPuntaje=asignarPuntaje(unPuntaje, intentos)
            return print(f"{dibujoPorPuntaje(unPuntaje)} Adivinaste la palabra!!! Sumaste {unPuntaje} puntos")

        else:
            print(comparadorDePalabras(len(palabraAAdivinar),palabraIngresada))
            intentos += 1
            corteJuego(intentos,unaRacha, unPuntaje)
            

    def comparadorDePalabras(numero, palabra):

        print(palabraAAdivinar)

        if palabra == "help":
            instrucciones()

        while len(palabra) != numero:
            palabra = str(input(f"La palabra debe ser de {numero} letras! Ingrese otra\n>>> "))
        
        while cantidadLetras == range(5,8) and palabra not in dicc_totalidad_palabras.values():
            palabra = str(input("Papa frita, esa palabra no esta en el diccionario!!\n>>> "))
        
        while cantidadLetras != range(5,8) and palabra not in dicc.values():
            palabra = str(input("Papa frita, esa palabra no esta en el diccionario!!\n>>> "))
            

        resultado = list(palabra)

        for i in range(len(resultado)):                                #  PRIMERO AVERIGUA
            if resultado[i] == palabraAAdivinar[i]:                    #  CUALES SON []
                resultado.pop(i)                                       #  XQ SON DE MAYOR 
                resultado.insert(i, f"[{palabra[i]}]")                 #  IMPORTANCIA

        for i in range(len(resultado)):                                                                    # CONDICIONES: 
            if (resultado[i] in palabraAAdivinar and                                                       # QUE I ESTE EN LA PALABRA
            (resultado.count(f"|{palabra[i]}|") < palabraAAdivinar.count(palabra[i]) and                # QUE NO HAYA MAS |I| QUE I EN LA PALABRA
                resultado.count(f"[{palabra[i]}]") < palabraAAdivinar.count(palabra[i]))):                 # QUE NO HAYA MAS [I] QUE I EN LA PALABRA
                
                resultado.pop(i)                                                                                             
                resultado.insert(i, f"|{palabra[i]}|" )                                                             
                
        
        return " ".join(resultado)

    corteJuego(contadorIntentos, racha, puntaje)

    # fin partida muestra un dibujo con ascii cada vez que terminas. depende del puntaje

ejecucionUnaPartida()


        

    


