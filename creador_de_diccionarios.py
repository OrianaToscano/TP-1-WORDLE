# La idea de este archivo es re-formatear los archivos "cinco_letras.py", "seis_letras.py", "siete_letras.py" y "tildes.py"
# Cuando se ejecuta, escribe un archivo .py ya creado. Escribe un único diccionario llamado: 
# "dicc_palabras_[numero]_letras" / "dicc_palabras_tildes"
# Además de crear un único diccionario con todos los datos, vuelve a asignar indexes en orden (al filtrar, las palabras tienen 
# indexes no consecutivos)


import DICCIONARIOS.diccionarios_no_formateados.seis_letras #esta linea se cambia por .cinco_letras // .seis_letras // .siete_letras // tildes
from DICCIONARIOS.diccionario_master import *
from DICCIONARIOS.diccionario_seis_letras import *

dicc = dicc_palabras_seis_letras
# archivo = open("DICCIONARIOS\diccionario_master.py", "a", 3, "utf-8") # idem comentario anterior. Se modifica nombre de archivo
# archivo.write("dicc_all_palabras = {") # se modifica nombre de dicc
oracion = ""
i=0
n=0
while len(dicc):
    valor = list(dicc.values())
    dicc_all_palabras.extend
    i+=1
    n+=1

#archivo.write("}")
#archivo.close()
