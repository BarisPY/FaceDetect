import cv2

#Haar Cascade sınıflandırıcısını yükle
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Resim dosyasını açın
image_path ="a.jpg"
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Yüzleri tespit et
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()