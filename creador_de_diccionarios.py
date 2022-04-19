# La idea de este archivo es re-formatear los archivos "cinco_letras.py", "seis_letras.py", "siete_letras.py" y "tildes.py"
# Cuando se ejecuta, escribe un archivo .py ya creado. Escribe un único diccionario llamado: 
# "dicc_palabras_[numero]_letras" / "dicc_palabras_tildes"
# Además de crear un único diccionario con todos los datos, vuelve a asignar indexes en orden (al filtrar, las palabras tienen 
# indexes no consecutivos)


import DICCIONARIOS.diccionarios_no_formateados.siete_letras  #esta linea se cambia por .cinco_letras // .seis_letras // .siete_letras // tildes



dicc = DICCIONARIOS.diccionarios_no_formateados.siete_letras 
archivo = open("TP 1 WORDLE\DICCIONARIOS\diccionario_siete_letras.py", "w", 3, "utf-8") # idem comentario anterior. Se modifica nombre de archivo
archivo.write("dicc_palabras_siete_letras = {") # se modifica nombre de dicc
oracion = ""

for i in range(len(dicc.listaPalabras)): 
    valor = list(dicc.listaPalabras[i].values())
    archivo.write(f"{i}: \"{valor[1]}\", ")

archivo.write("}")
archivo.close()
