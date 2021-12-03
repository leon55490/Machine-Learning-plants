import numpy as np
import cv2
import imutils
import os

Datos = 'p'

if not os.path.exists(Datos):
   print('Carpeta creada: ', Datos) #
   os.makedirs(Datos) # Creamos directorio, si no existe

cap = cv2.VideoCapture(1)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0

while True:
   ret, frame = cap.read()
   if ret == False: break
   imAux = frame.copy()
   cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

   objeto = imAux[y1:y2,x1:x2]
   objeto = imutils.resize(objeto, width=30)

   k = cv2.waitKey(1)

   if k == ord('s'):
      cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto) # Almacenando imagen
      print('Imagen almacenada: ', 'Roja_{}.jpg'.format(count)) # Impresión
      count = count + 1

   cv2.imshow('frame',frame)
   cv2.imshow('objeto',objeto)

   if k == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()