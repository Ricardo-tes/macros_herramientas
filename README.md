Este repositorio contiene macros escritas en python con la libreria pyautogui y herramientas para ayudar a la escritura de macros. La librería pyautogui tiene funciones de busqueda de imagenes. La busqueda es relativamente lenta y para agilizarla se puede limitar a partes de la pantalla.


## herramientas.py
- La función guardar punto permite tomar las coordenadas de un punto en la pantalla, lo muestra en forma de tupla y da la opción de guardarlo en un archivo .csv. Tambien muyestra la resolucion de la pantalla
- La función guardar zona es similiar a guardar punto pero sirve para delimitar una zona rectangular en  la pantalla. Por lo demas tiene la misma funcionalidad de la funcion anterior.
- La función guardar recorte permite tomar una captura de parte de la pantalla y guardarla en formato png.

## macro_computrabajo.py
Accede a la pagina de computrabajo hace una busqueda y envía curriculums a los avisos que contengan palabras claves especificadas. Los puntos se tomaron con una resolucion de pantalla de 1920*1080. 
Para hacer funcionar la macro:
- cambiar las coordenadas de los puntos y zonas.
- Reemplazar la imagen usuario.png dentro de la carpeta "marcadores" con una imagen de su nombre de usuario y mismonombre.
- Dentro de la carpeta "palabras_clave" poner imagenes png de las palabras clave que quiera buscar. Las imagenes deben ser capturas tomadas de anuncios de la página. La funcion de busqueda solo compara imagenes, no reconoce el significado de las palabras. Cambiar en el programa los nombres de las imagenes.
