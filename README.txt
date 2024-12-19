Proyecto de Reconocimiento Facial

Este proyecto utiliza face_recognition y OpenCV para reconocer rostros y registrar ingresos en un archivo CSV.

La version de python y de los modulos en este proyecto influye ya que solo se puede ejecutar 
con la version de python 3.10. 
version de face_recognition 1.3.0
version de opencv-python 4.10.0.84



Hay dos programas en la carpeta Reconocimiento Facial:
1.proyecto_reconocimiento_facial.py
2.reconocimiento_facial.py

Ejecuta el programa:
Desde un IDE corre el programa a elegir


1.proyecto_reconocimiento_facial.py

Funcionalidad:
Carga y codifica las imágenes en Empleados.
Activa la cámara y busca coincidencias faciales.
Registra el nombre y la hora en registro.csv.

Notas:
El umbral de coincidencia es 0.6, ajustable en el código.
Asegúrate de que las imágenes sean claras para un mejor reconocimiento.
Puedes agregar y quitar imágenes de la carpeta Empleados


2.reconocimiento_facial.py
Funcionalidad:
Carga las imágenes FotoA y FotoB
Detecta y codifica los rostros.
Compara las imágenes y muestra:
Resultado de coincidencia (True/False). Distancia entre los rostros.
El programa dibuja rectángulos en las caras detectadas

Notas:
Las imágenes deben ser claras y contener un solo rostro para mejores resultados.
El resultado y la distancia se muestran en la consola y sobre la imagen de prueba.
Puedes cambiar la FotoA y Foto C tambien para comparar


