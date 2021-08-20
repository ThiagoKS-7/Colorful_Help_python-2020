# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 23:53:32 2020

@author: thiag
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np



class_names = ["Nada","Camisa", "Camiseta","Tênis"]

path = "C:/Users/thiag/Desktop/camisetas/Camiseta (4).jpg" 
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Image", image)

blurred = cv2.GaussianBlur(image, (5, 5), 0)

thresh = cv2.adaptiveThreshold(blurred, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 15, 3)


mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 88), (cX + 75 , cY + 88), 255,-1)
masked = cv2.bitwise_and(image, image, mask = mask) 
#cv2.imshow("Mask Applied to Image", masked)

mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 88), (cX + 75 , cY + 88), 255,-1)
masked = cv2.bitwise_and(image, image, mask = mask) 
#cv2.imshow("Mask Applied to Adap. thresh", masked)
plt.imshow(masked,cmap = 'gray')
plt.show()
cv2.imwrite("teste.jpg", masked)
resize = cv2.resize(cv2.imread("teste.jpg"), (40,40))
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Done.")
resize = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
resized2 = resize.reshape(1,40,40,-1)
model = tf.keras.models.load_model("AUG_K_TUNED-CNN.model")
print("Testes de predição:")
predicao = model.predict([resized2])
print("Fig #1:")
    # colocar enderço da imagem dentro do "prepare()"
ctg = np.argmax(predicao.flatten())   
print(class_names[ctg])
print("Posição da predição encontrada:", ctg)

del cX,cY, mask,thresh,blurred,image,path,masked