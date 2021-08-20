# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:33:36 2020

@author: thiag
"""
import tensorflow as tf
import pickle

X_test = pickle.load(open("testX.pickle", "rb"))
Y_test = pickle.load(open("testY.pickle", "rb"))

X_test =  X_test/ 255

class_names = ["Nada","Camisa", "Camiseta","Tênis"]
model = tf.keras.models.load_model("64x3-CNN20.model")
print("Testes de avaliação:")
print()
test_loss, test_acc = model.evaluate(X_test, Y_test, verbose = 2)
print(model.summary())
print("Precisão:",(test_acc * 100),"%","  Perda:",  test_loss)
print()
print("Done.")

del X_test, Y_test, class_names, test_acc,test_loss