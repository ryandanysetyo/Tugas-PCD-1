
import numpy as np
import cv2

cap = cv2.VideoCapture(0) #untuk memanggil webcam. angka 0 menunjukkan bahwa yang digunakan adalah webcam pada pc.
print(cap.isOpened())


while(True): #untuk looping imshow, sehingga camera akan menangkap objek video secara realtime.
    ret, frame = cap.read() #untuk menangkap gambar dengan format berwarna
    bright = cv2.addWeighted(frame,1.5, np.zeros(frame.shape, frame.dtype), 0, 100) #untuk meningkatkan nilai kecerahan gambar
    cv2.imshow('Kamera',bright) #umtuk menampilkan gambar setelah diubah brightnessnya.
    if cv2.waitKey(1) & 0xFF == ord('t'): #perintah untuk menghentikan program dengan menekan tombol q pada keyboard
        break


cap.realease()
cv2.destroyAllwindows()