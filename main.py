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
    palabraIngresada = str(input("Ingrese una palabra: ")).lower()

    if palabraIngresada == "chau":
        return "Gracias por jugar! Este es el fin de la partida"

    while len(palabraIngresada) != numero:
        palabraIngresada = str(input("La palabra debe ser de 5 letras! Ingrese otra"))
    
    while palabraIngresada not in dicc.values():
        palabraIngresada = str(input("Papa frita, esa palabra no esta en el diccionario!!"))

    if palabraIngresada == palabraAAdivinar:
        # el contador se tendria que poner aca xq es el cierre del programa
        return "Vamooos fiera adivinaste la palabra!!"
        

    resultado = ""

    for i in range(len(palabraIngresada)):
        if palabraIngresada[i] == palabraAAdivinar[i]:
            resultado += f"[{palabraIngresada[i]}] "

        elif palabraIngresada[i] in palabraAAdivinar and palabraAAdivinar[:i].count(palabraAAdivinar[i]) < palabraIngresada.count(palabraAAdivinar[i]):
            resultado += f"|{palabraIngresada[i]}| "
        else:
            resultado += f"{palabraIngresada[i]} "
        
    return f"{palabraIngresada}\n{resultado}"

# falta ver el tema del contador

def finPartida():
    print("Gracias por jugar! Este es el fin de la partida")

# fin partida muestra un dibujo con ascii cada vez que terminas. depende del puntaje

i = 0
while i < 5 or palabraIngresada != palabraAAdivinar:
    print(comparadorDePalabras(cantidadLetras))
    palabraIngresada = comparadorDePalabras
    print(palabraAAdivinar)
    i += 1
        
# hay que solucionar el tema de como hacer que salga del bucle por completo. ADEMAS el problema de las letras repetidas sigue:
# si la letra repetida en pIngresada esta al final de paAdivinar, va a hacer || hasta que llegue al final. o sea, funciona solo si 
# la letra repetida en cuestion esta al principio, que no siempre es el caso. 
# deberiamos encontrar la manera de priorizar []. se podria hacer con listas, y que ingrese las letras en los indexes correspondientes.
# se podria hacer una lista con cada letra sola, y cada letra se va reemplezando por || o []
    


