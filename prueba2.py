import numpy as np
import cv2
 
#cargamos la plantilla e inicializamos la webcam:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
caras =[] 
resized = []
indice = 0
sujeto = 0
flag_sujeto = 0

while(True):
    #leemos un frame y lo guardamos
    ret, img = cap.read()
 
    #convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    #buscamos las coordenadas de los rostros (si los hay) y
    #guardamos su posicion
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    #Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x,y,w,h) in faces:
		#con la tecla 'q' salimos del programa
	    if (cv2.waitKey(1) & 0xFF == ord('q')) and not flag_sujeto:
			flag_sujeto = 1
			sujeto += 1
			print sujeto
	    if flag_sujeto:
	                resized = img[y:y+h,x:x+w]
   		        #cv2.imshow('img',resized)
		        cv2.imwrite("sujeto%s-foto%s.png" % (sujeto,indice) ,resized)
		        indice += 1
	    if (cv2.waitKey(1) & 0xFF == ord('e')) and flag_sujeto:
			flag_sujeto = 0
    	
            cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
 
    #Mostramos la imagen
    cv2.imshow('img',img)
     
    #con la tecla 'q' salimos del programa
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

cap.release()
cv2-destroyAllWindows()
