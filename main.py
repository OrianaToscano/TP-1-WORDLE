import random
from pantallaInicio import *

if cantidadLetras == 5:
    from DICCIONARIOS.diccionario_cinco_letras import *
    dicc = dicc_palabras_cinco_letras
elif cantidadLetras == 6:
    from DICCIONARIOS.diccionario_seis_letras import *
    dicc = dicc_palabras_seis_letras
elif cantidadLetras == 7:
    from DICCIONARIOS.diccionario_siete_letras import *
    dicc = dicc_palabras_siete_letras
else:
    from DICCIONARIOS.diccionario_tildes import *
    dicc = dicc_palabras_tildes

palabraAAdivinar = dicc.get(random.randint(0, len(dicc)))

palabraIngresada = ""

def comparadorDePalabras(numero):
    palabraIngresada = str(input("Ingrese una palabra\n>>> ")).lower()

    if numero == range(5,8):                                                                    # SI LA OPCION ES TILDES (= RANGE)
        print(f"La palabra que tenés que averiguar tiene {len(palabraAAdivinar)} letras!")      # 

    if palabraIngresada == "chau":
        return "Gracias por jugar! Este es el fin de la partida"

    while len(palabraIngresada) != numero:
        palabraIngresada = str(input("La palabra debe ser de 5 letras! Ingrese otra\n>>> "))
    
    while palabraIngresada not in dicc.values():
        palabraIngresada = str(input("Papa frita, esa palabra no esta en el diccionario!!\n>>> "))

    if palabraIngresada == palabraAAdivinar:
        # el contador se tendria que poner aca xq es el cierre del programa
        return "Vamooos fiera adivinaste la palabra!!"
        

    resultado = list(palabraIngresada)

    for i in range(len(resultado)):                                #  PRIMERO AVERIGUA
        if resultado[i] == palabraAAdivinar[i]:                    #  CUALES SON []
            resultado.pop(i)                                       #  XQ SON DE MAYOR 
            resultado.insert(i, f"[{palabraIngresada[i]}]")        #  IMPORTANCIA

    for i in range(len(resultado)):                                                                                      # CONDICIONES: 
        if (resultado[i] in palabraAAdivinar and                                                                         # QUE I ESTE EN LA PALABRA
           (resultado.count(f"|{palabraIngresada[i]}|") < palabraAAdivinar.count(palabraIngresada[i]) and                # QUE NO HAYA MAS |I| QUE I EN LA PALABRA
            resultado.count(f"[{palabraIngresada[i]}]") < palabraAAdivinar.count(palabraIngresada[i]))):                 # QUE NO HAYA MAS [I] QUE I EN LA PALABRA
            
            resultado.pop(i)                                                                                             
            resultado.insert(i, f"|{palabraIngresada[i]}|" )                                                             
            
        
    return " ".join(resultado)

# falta ver el tema del contador

def finPartida():
    print("Gracias por jugar! Este es el fin de la partida")

# fin partida muestra un dibujo con ascii cada vez que terminas. depende del puntaje

i = 0
while i <= 5 and palabraIngresada != palabraAAdivinar:
    print(comparadorDePalabras(cantidadLetras))
    print(palabraAAdivinar)
    i += 1
        
# hay que solucionar el tema de como hacer que salga del bucle por completo. 
    


