import cv2
import face_recognition as fr

# cargar imagenes
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

#cambiar el color a rgb de las imagenes
foto_control = cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

#localizar cara de foto control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codifica_A =fr.face_encodings(foto_control)[0]

#localizar cara de foto prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codifica_B =fr.face_encodings(foto_prueba)[0]

#mostrar rectangulos
#foto control
cv2.rectangle(foto_control,(lugar_cara_A[3],lugar_cara_A[0]),
              (lugar_cara_A[1],lugar_cara_A[2]),
              (0,255,0),2)
#foto prueba
cv2.rectangle(foto_prueba,(lugar_cara_B[3],lugar_cara_B[0]),
              (lugar_cara_B[1],lugar_cara_B[2]),
              (0,255,0),2)

#comparar imagenes
resultado =fr.compare_faces([cara_codifica_A],cara_codifica_B)
print(resultado)

#realizar medida de la distancia
distancia = fr.face_distance([cara_codifica_A],cara_codifica_B,)
print(distancia)

#mostrar resultado
cv2.putText(foto_prueba,f'{resultado} {distancia}',
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,255,0),
            2)


#mostrar imagenes
cv2.imshow('foto control', foto_control)
cv2.imshow('foto_prueba',foto_prueba)


#mantener programa abierto
cv2.waitKey(0)