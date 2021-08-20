# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 13:32:46 2021

@author: thiag
"""

def def_obj():
    
    import pyttsx3
    import speech_recognition as sr
    
    engine=pyttsx3.init()
    engine.setProperty('voice','pt')
    
    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as fonte:
        r.adjust_for_ambient_noise(fonte)
        print("Saudações, estou aguardando o seu comando")
        audio= r.listen(fonte)
        print("um momento...")
        try:
            texto= r.recognize_google(audio, language="pt-BR")
            print("Você disse: {}".format(texto)) 
        except:
            print("não entendi .-.")
        
        if len(texto) == 15:
            número = texto[13:15]
            print(número)
            
            #FRASES QUE ELA ENTENDE:
        if texto == "defina objeto um":
            print("deu certo")
        elif texto == "defina objeto" + número:
            print("deu certo tb")
            
        
def_obj()