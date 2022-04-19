## TP-1-WORDLE
# Integrantes:Martín Seijo Rosario, Puelman Lara, Stagno Victoria, Toscano oriana
- **Los requerimientos** 
  - Si se ejecuta desde el archivo .exe:
       - Sistema operativo Windows
       - Se debe descargar el archivo basesDeDatosUsuarios.txt y colocarlos en la misma carpeta donde se aloja el archivo .exe
  - Si se quiere ejecutar desde otro sistema operativo / sin utilizacion del archivo .exe:
       - Tener python descargado e instalado
       - Descargar todos los archivos, guardarlos en la misma carpeta y ejecutar el archivo main desde la consola de comandos u otro programa que soporte python 
          - En la terminal, con el PATH configurado a la ubicacion de los archivos (cd *direccion*), ingresar *from main import \**

- **Cómo usar el programa** 
  - Se debe ejecutar el archivo Wordle.exe, y seguir las indicaciones que el mismo indica.
 
- **Sistema de puntaje**
  - Si se responde al primer intento suma 80 puntos. Al segundo 60 puntos y al tercero, 40 puntos. A partir de ahí por cada intento se le resta 10 hasta llegar al sexto.
  Las palabras de 5 no te dan bonus, las 6 dan 5 puntos y las de 7, 10. Con tildes se obtiene un bonus de 20 puntos.
  Estos dos se suman y dan la totalidad de puntaje obtenido, si se acertó la palabra en menos de 6 intentos.
  
- **Funciones extra**
  -  El programa obtiene las palabras de varias bases de datos convertidas en archivos python, según la cantidad de letras, y si tiene tilde o no. 
  Además hay un diccionario master para que el programa puede tomar cualquier palabra al momento de jugar, y no solo las que cumplen con la condición.
  - Se puede elegir el nivel de dificultad en la pantalla de inicio (de 5 a 7 letras o con tildes).
  - Se registra el puntaje el más alto y el usuario en un archivo .txt, que luego se utiliza para mostrar un rankin.Este últipo muestra quién tiene el puntaje más alto, y cuánto es.
  - Muestra dibujos ascii dependiendo del puntaje obtenido
