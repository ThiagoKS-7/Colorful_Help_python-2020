# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:58:59 2021

@author: thiag
"""

import tensorflow as tf

model = tf.keras.models.load_model("AUG_K_TUNED-CNN2.model")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tfmodel = converter.convert()
print("[INFO] modelo convertido.")
with open("model.tflite","wb") as f:
    f.write(tfmodel)
print(["[INFO] modelo aberto."])