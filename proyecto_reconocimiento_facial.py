import face_recognition as fr
import cv2
import os
import numpy
from datetime import datetime

#variables
ruta = 'Empleados'
nombres_empleados = []
lista_empleados = os.listdir(ruta)
mis_imagenes = []

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)
#codificar imagenes
def codificar(imagenes):
    #crear una lista nueva
    lista_codificada = []

    #pasar todas las imagenes a rgb
    for imagen in imagenes:
        #pasamos la imagen a rgb
        imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

        #codificamos la imagen actual
        codificado = fr.face_encodings(imagen)[0]

        #agregar a la lista
        lista_codificada.append(codificado)

    #devolver la lista codificada con las imagenes ya codificadas
    return lista_codificada


#registrar los ingresos
def ingreso (persona):
    f = open('registro.csv','r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


#lista con todos las imagenes de empleados codificada
lista_empleados_codificada = codificar(mis_imagenes)


#tomar una captura de camara web
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#leer imagen de la captura
exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    #reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    #codificamos la imagen de la captura
    cara_captura_codificadda = fr.face_encodings(imagen,cara_captura)

    #buscar coincidencias
    for caracodif,caraubic in zip(cara_captura_codificadda,cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada,caracodif)
        distancias = fr.face_distance(lista_empleados_codificada,caracodif)

        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)
        if distancias[indice_coincidencia]> 0.6:
            print('No coincide con ninguno de nuestros empleados')
        else:
            #buscar el nombre del usuario encontrado
            nombre = nombres_empleados[indice_coincidencia]

            y1,x2,y2,x1 = caraubic
            cv2.rectangle(imagen,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(imagen,(x1,y2-35),(x2,y2),(0,255,2),cv2.FILLED)
            cv2.putText(imagen,nombre,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,
                        (255,255,255))

            ingreso(nombre)

            cv2.imshow('Foto webcam',imagen)
            cv2.waitKey(0)