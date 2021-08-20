# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:32:44 2020

@author: thiag
"""


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
import pickle
import numpy as np
# abrir o dataset criado
X_train = pickle.load(open("trainX.pickle", "rb"))
Y_train = pickle.load(open("trainY.pickle", "rb"))
X_test = pickle.load(open("X_test.pickle", "rb"))
Y_test = pickle.load(open("Y_test.pickle", "rb"))
X_train =  X_train/ 255
X_test =  X_test / 255
model = Sequential()
# pooling
model.add(Conv2D(filters=256, kernel_size=(3, 3), strides=1, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=128, kernel_size=(3, 3), strides=1, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(filters=64, kernel_size=(2, 2), strides=1, activation='relu'))
model.add(MaxPooling2D(pool_size=(1,1)))
model.add(Conv2D(filters=32, kernel_size=(2, 2), strides=1, activation='relu'))
model.add(MaxPooling2D(pool_size=(1,1)))
model.add(Conv2D(filters=32, kernel_size=(2, 2), strides=1, activation='relu'))
model.add(MaxPooling2D(pool_size=(1,1)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(4, activation ='softmax'))



'''
model.add(Conv2D(256, (5,3), input_shape = (40,40,1), activation="relu"))
model.add(Conv2D(128, (5,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32, (3,3), activation="relu"))
model.add(Conv2D(16, (3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten()) # transform a matriz em vetores

model.add(Dense(1024, activation="relu"))
model.add(Dense(1024, activation="relu"))
model.add(Dense(40, activation="relu"))

# output

model.add(Dense(4, activation ='softmax'))
'''
# compilação
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# fit e validação
X_train = np.array(X_train).reshape(-1, 40, 40, 1)
Y_train = np.array(Y_train)

model.fit(X_train, Y_train, batch_size = 2, epochs=5, validation_split=0.2)
# test_loss, test_acc = model.evaluate(X_test, Y_test, verbose = 2)
# print("/n Precisão:",(test_acc * 100),"%")
model.save("AUG_K_TUNED-CNN-3.model")
print(model.summary())
print()
print("[INFO] Sucessfully trained. HECK YEA")