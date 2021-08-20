# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 00:01:34 2020

@author: thiag
"""
from keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
import numpy as np
import keras 
import pickle
trainX = pickle.load(open("trainX5.pickle", "rb"))



datagen = ImageDataGenerator(horizontal_flip= True,
                             vertical_flip= True,
                             rotation_range = 45,
                             brightness_range=(0.01,1.8),
                             zoom_range = 0.45,
                             channel_shift_range = 0.4,
                             fill_mode='nearest')

count = 0

for batch in  enumerate(datagen.flow(trainX,batch_size = 1,save_to_dir="C:/Users/thiag/Desktop/Projetos 2020 - Coisas da IA/augmented imgs", save_prefix="botas", save_format= ".jpg")):
    count += 1
    if count == 2000:
        break


print("Pronto, 2000 imgs baixadas")





'''def faz_modelo():
    model = Sequential()
    # pooling
    model.add(Conv2D(32, (3,3),padding = 'same', input_shape = trainX.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Conv2D(32, (3,3),padding = 'same', input_shape = trainX.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))    
    
    model.add(Flatten()) # transforma a matriz em vetores
    
    model.add(Dense(100))
    model.add(Activation("relu"))
    model.add(Dropout(0.25))
        
    # output
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
    
    # compilação
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model'''