# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:55:20 2020

@author: thiag
"""
import tensorflow as tf
import pickle
import numpy as np

class_names = ["Bota","Camisa", "Camiseta","Tênis"]
nome = "AUG_K_TUNED-CNN2.model"
classes = [0,1,2,3]
X_train = pickle.load(open("trainX3.pickle", "rb"))
model = tf.keras.models.load_model(nome)

print("Testes de predição:")
print(nome)
print()
predição = model.predict(X_train)
#gabarito = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #0 botas
#gabarito = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]  #1- camisetas
#gabarito = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  #2- camisas
gabarito = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3] #3- tenis
acertos = 0
i = 0
while i < len(X_train):
    ctg = np.argmax(predição[i].flatten())
    print("Fig #",i,":")
    print(class_names[ctg])
    if gabarito[i] == classes[ctg]:
        acertos += 1
    i += 1
    
Precisão = (acertos/ len(X_train) * 100)
print("Precisão: ", Precisão,"%")
del gabarito,Precisão, ctg, acertos, i, classes, class_names, model, X_train,predição