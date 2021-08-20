# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:37:08 2020

@author: thiag
"""


from analisa_cor import distingue_cor
categoria = "tenis"
cor = [0, 1 ,2, 3, 4, 5, 6, 7]
#gabarito = [0 ,4, 0, 1, 4, 7, 7, 7, 4, 0, 4] # camisas
#gabarito = [0, 4, 7, 7, 7, 7, 0, 0, 0, 0, 0] # camisetas
gabarito = [0, 0, 7, 0, 0, 7, 7, 7, 0, 0, 7, 7] # tenis
#gabarito = [0, 2, 1, 1, 2, 0, 2, 1, 2, 2, 2] # botas
nome_cor = ["azul","preto","amarelo","vermelho","verde","laranja","marrom","branco"]
x = 1
x = str(x)
acertos = 0
i = 0
print()
print("Teste de distinção de cores")
print()
print("Amostras:", categoria)
print()
while i < 10:
   print("Fig #",i,":")
   roupa = ("C:/Users/thiag/Desktop/tenis/")
   formato = (".png")
   roupa = str(roupa + x + formato)
   dist = distingue_cor(roupa)
   respostas = gabarito[int(x)]
   if  respostas == int(dist):
      acertos += 1
   i += 1
   x = int(x)
   x += 1
   x = str(x)
Precisão = (acertos/ 10 * 100)
print("Precisão: ", Precisão,"%")
