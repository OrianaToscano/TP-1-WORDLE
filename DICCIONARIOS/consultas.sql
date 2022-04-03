# Ejecutar el siguiente programa para CONSULTAR de la base de datos las palabras de 5 letras que NO tengan tildes.
SELECT * FROM palabras 
WHERE
    (palabra LIKE '_____'
    AND sensible NOT LIKE BINARY( '%á%')
    AND sensible NOT LIKE BINARY( '%é%')
    AND sensible NOT LIKE BINARY( '%í%')
    AND sensible NOT LIKE BINARY( '%ó%')
    AND sensible NOT LIKE BINARY( '%ú%'));
    


# Ejecutar el siguiente programa para CONSULTAR de la base de datos las palabras de 6 letras que NO tengan tildes.
SELECT * FROM palabras 
WHERE
    (palabra LIKE '______'
    AND sensible NOT LIKE BINARY( '%á%')
    AND sensible NOT LIKE BINARY( '%é%')
    AND sensible NOT LIKE BINARY( '%í%')
    AND sensible NOT LIKE BINARY( '%ó%')
    AND sensible NOT LIKE BINARY( '%ú%'));
    

# Ejecutar el siguiente programa para CONSULTAR de la base de datos las palabras de 7 letras que NO tengan tildes.
SELECT * FROM palabras 
WHERE
    (palabra LIKE '_______'
    AND sensible NOT LIKE BINARY( '%á%')
    AND sensible NOT LIKE BINARY( '%é%')
    AND sensible NOT LIKE BINARY( '%í%')
    AND sensible NOT LIKE BINARY( '%ó%')
    AND sensible NOT LIKE BINARY( '%ú%'));
    
    
    
    
# Ejecutar el siguiente programa para CONSULTAR de la base de datos las palabras de 5, 6 o 7 letras que SI tengan tildes (SOLO PALABRAS CON TILDE).
SELECT * FROM palabras 
WHERE
    (palabra LIKE '_____'
	OR palabra LIKE '______'
    OR palabra LIKE '_______') AND (
    sensible LIKE BINARY( '%á%')
    OR sensible LIKE BINARY( '%é%')
    OR sensible LIKE BINARY( '%í%')
    OR sensible LIKE BINARY( '%ó%')
    OR sensible LIKE BINARY( '%ú%'));