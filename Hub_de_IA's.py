# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:53:39 2021

@author: thiag
"""

# VOZ E OUVIDOS DA IA
import speech_recognition as sr
from predições import IA_1
from yolo3_img import IA_2
import pyttsx3

engine=pyttsx3.init()
engine.setProperty('voice','pt')

r = sr.Recognizer()

mic = sr.Microphone()

with mic as fonte:
    r.adjust_for_ambient_noise(fonte)
    engine.say("Saudações, aguardo seu comando")
    engine.runAndWait()
    audio= r.listen(fonte)
    print("um momento...")
    try:
        text= r.recognize_google(audio, language="pt-BR")
        print("Você disse {}".format(text)) 
    except:
        print("não entendi .-.")
        
    #FRASES QUE ELA ENTENDE:
if text =="que roupa é essa":
    IA_1()
elif text == "O que é isso" or text == "que é isso":
    IA_2()
else:
    engine.say("Desculpe, não entendi")
    engine.runAndWait()
engine.stop()