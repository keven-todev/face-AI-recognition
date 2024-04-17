import cv2
import os

contents = os.listdir('image')
input = input('Entrer le nom de la vidéo : ')
input = input.lower()

if input in contents:
    path = input
else:
   os.mkdir('image/'+input)
   path = input

# on charge le model
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

c = 50
id=0

# cascadeclassifier permet de prendre un modele de visage spécifique
capture = cv2.VideoCapture("3.mp4")

while True:
    # pour capturer toutes les frames et ouvrir l'onglet: 
    ret, frame = capture.read()

    # changer les couleurs 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect les mouvements, la position et d'autres params
    face = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(c, c))

    #on boucle pour  prendre differentes photos, l'envois dans le dossier image & stock
    for x, y, w, h in face:
        cv2.imwrite("image/"+path+"p-{:d}.png".format(id), frame[y:y+h, x:x+w])
        id+=1
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    # afficher l'image
    cv2.imshow('video', frame)

    # affiche l'image sans s'art 
    key=cv2.waitKey(1)&0xFF 
    if key ==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()