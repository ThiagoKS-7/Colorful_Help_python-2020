# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:03:39 2020

@author: thiag
"""


import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf

# endereço do dataset e categorias'
Dir = "C:/Users/thiag/Downloads/roupas"
Categorias = ["bota","camisa", "camiseta","tenis" ]

for categoria in Categorias:
    path = os.path.join(Dir, categoria)
    for img in os.listdir(path):
        array_img = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(array_img, cmap = "gray")
        plt.show()
        break
    break

# dai agr checa o tamanho dela
print("\033[39mTamanho da imagem: ", array_img.shape)

# Redimensionameto
tamanho = 60
array_novo = cv2.resize(array_img, (tamanho, tamanho))
plt.imshow(array_novo, cmap = "gray")
plt.show()
print("\033[39mTamanho da imagem: ", array_novo.shape)
    
# ta agr vai criar a train data
training_data = []
def create_training_data():
    for categoria in Categorias:
        path = os.path.join(Dir, categoria)
        class_num = Categorias.index(categoria)
        for img in os.listdir(path):
            try: 
                array_img = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                tamanho = 60
                array_novo = cv2.resize(array_img, (tamanho, tamanho))
                training_data.append([array_novo, class_num])
            except Exception as e:
                pass
     
create_training_data()
print("Comprimento do array: ", len(training_data))   

import random

# embaralha as imagens 
random.shuffle(training_data)

# imprime as amostras
'''
print("Amostra: [(")
for sample in training_data:
    print(sample[1], end =" ")
print(")]")
'''
X = []
y = []



for features, label in training_data:
    X.append(features)
    y.append(label)
    
X = np.array(X).reshape(-1, tamanho, tamanho, 1)

import pickle

# salvar alterações e construção do modelo

pickle_out = open("X.pickle4","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle4","wb")
pickle.dump(y, pickle_out)
pickle_out.close()
    
    
# abrir o que foi salvo:

pickle_in = open("X.pickle4", "rb")
X = pickle.load(pickle_in)


X[1]
print("y:", y[1])
print()
print("Done. YATAAAAAAAAAAAAAAA")
    
