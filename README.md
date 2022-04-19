## TP-1-WORDLE
# Integrantes:Martín Seijo Rosario, Puelman Lara, Stagno Victoria, Toscano oriana
- **Los requerimientos** (ej. tener conexión a internet, instalar  una base de datos, un módulo…)

- **Cómo usar el programa** --> Ejecutar el .exe
  - Se debe ejecutar el archivo main.exe, y seguir las indicaciones que el mismo indica.
- **Sistema de puntaje**
  - Si se responde al primer intento suma 80 puntos. Al segundo 60 puntos y al tercero, 40 puntos. A partir de ahí por cada intento se le resta 10 hasta llegar al sexto.
  Las palabras de 5 no te dan bonus, la de 6 y 7, 5 y 10 respectivamente. Con tildes se obtiene un bónus de 20 puntos.
  Estos dos se suman y dan la totalidad de puntaje obtenido, si se acertó la palabra en menos de 6 intentos.
  
- **Funciones extra**
  -  El programa obtiene las palabras de varias bases de datos convertidas en archivos python, según la cantidad de letras, y si tiene tilde o no. 
  Además hay un diccionario master para que el programa puede tomar cualquier palabra al momento de jugar, y no solo las que cumplen con la condición.
  - Se puede elegir el nivel de dificultad en la pantalla de inicio ( de 5 a 7 letras o con tildes).
  - Se registra el puntaje más alto y el usuario en un archivo .txt, que luego se utiliza para mostrar un ranking. 
  -Este últipo muestra quién tiene el puntaje más alto, y cuánto es.
