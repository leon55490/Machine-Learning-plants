import cv2
#? para el botón
import tkinter as tk
from tkinter import Label, messagebox
from AdminArchivo import AdminArchivo

cap = cv2.VideoCapture(1)
flor = cv2.CascadeClassifier('cascade.xml')
rosa = cv2.CascadeClassifier('cascade2.xml')

listaPlantas = AdminArchivo.cargar('plantas.json')


def botoncito():  

    countA = 0
    countB = 0

    while True:
        
        ret,frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        florT = flor.detectMultiScale(
            gray,
            scaleFactor = 6,
            minNeighbors = 295, #? 91
            minSize=(35,38) #? (70,78)
        )

        rosaT = rosa.detectMultiScale(
            gray,
            scaleFactor = 6,
            minNeighbors = 295, #? 91
            minSize=(35,38) #? (70,78)
        )

        if len(rosaT) == 1:
            for (x,y,w,h) in rosaT:
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(frame,'Rosa',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
            cv2.imshow('frame',frame)
            if countA == 200:
                messagebox.showinfo('Rosa Detecatada', listaPlantas[0]['Rosa'])
                countA = countA + 1
            else:
                countA = countA + 1
        elif len(florT) == 1:  
            for (x,y,w,h) in florT:
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(frame,'Tulipan',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
            cv2.imshow('frame',frame)
            if countB == 200:
                messagebox.showinfo('Tulipan Detectado', listaPlantas[1]['Tulipan'])
                countB = countB + 1
            else: countB = countB + 1
        cv2.imshow('frame',frame)
     
        if cv2.waitKey(1)== ord('q'):
            break
    cap.release()

ventana = tk.Tk()
ventana.title('Machine Learning')
ventana.geometry('300x220')
l = Label(ventana, text='Presione para ejecutar el detector')
l.pack()
button = tk.Button(ventana, text="Ejecutar", bg="gold", command=lambda:(botoncito(), ventana.destroy()))
button.pack()
ventana.mainloop()