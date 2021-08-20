# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:24:29 2020

@author: thiag
"""
import imageio
import cv2
import numpy as np
from matplotlib import pyplot as plt   


def distingue_cor(filepath):
    # redimensionamento da img pra distinguir a cor direito
    #img_col=imageio.imread(filepath)
    #resized_col = cv2.resize(img_col, (100,100))
    #centro_col= resized_col[40:60 , 40:60]  # área de interesse plotada  [40:60, 40:60
    
    
    img =cv2.imread(filepath)
    resized = cv2.resize(img, (100,100))
    centro = resized[40:60, 40:60] # construção da área de interesse

    #plt.imshow(centro_col)
    #plt.show()

    
    
    cor = ('b','g','r') # lista dos canais para o histograma
    for i, col in enumerate(cor):
        histr = cv2.calcHist([centro], [i], None, [256], [0,256]) # constrói o histograma p/
        # cada posição da lista cor
        #plt.plot(histr, color = col) # mostra o gráfico
        #plt.xlim([0,256]) #limite d x
        
        # Condições que guardam o valor da frequência e classe de cada histr (y e x)
        if i == 0:
             ymax = max(histr) 
             xmax, _ = np.where(histr == ymax)
             a = xmax[0]
        elif i == 1:
            ymax1 = max(histr)
            xmax1, _ = np.where(histr == ymax1)
            b = xmax1[0]
        else:
            ymax2 = max(histr)
            xmax2, _ = np.where(histr == ymax2)
            c = xmax2[0]
            
    #mostra o pico de cada gráfico, na mesma ordem q na lista cor
    print("Código:", "R:",c, "G:", b, "B:",a)    


    # condições q analisam o intervalo das cores
    if (a > (b + 20)) and (a > (c + 10)) and (a >= 40 and a <= 255) and (b >= 20 and b <= 190) and (c >= 3 and c <= 120):
        nome_cor= "azul"
        return nome_cor
        return str('0')
    elif (a >= 0 and a <= 120) and (b >= 15 and b <= 110) and (c >= 25 and c <= 145):
        nome_cor= "marrom"
        return nome_cor
        return str('1')
    elif (a >= 0 and a <= 108) and (b >= 0 and b <= 111) and (c >= 0 and c <= 35):
        nome_cor= "preto"
        return nome_cor
        return str('2')
    elif (a >= 0 and a <= 148) and (b >= 100 and b <= 230) and (c >= 170 and c <= 254):
        nome_cor= "amarelo"
        return nome_cor
        return str('3')

    elif (c > (a + 20)) and  (c > (b + 20)) and (a >= 15 and a <= 188) and (b >= 0 and b <= 130) and (c >= 80 and c <= 255):
        nome_cor= "vermelho"
        return nome_cor
        return str('4')
   
    elif (b > (a + 20)) and (b > (c + 20)) and (a >= 0 and a <= 170) and (b >= 55 and b <= 255) and (c >= 10 and c <= 90):
        nome_cor= "verde"
        return nome_cor
        return str('5')    
    elif (a >= 0 and a <= 35) and (b >= 55 and b <= 190) and (c >= 200 and c <= 255):
        nome_cor= "laranja"
        return nome_cor
        return str('6')
   
    else:
        nome_cor= "branco"
        return nome_cor
        return str('7')

"""
def codifica_dados(x):
    if x < 9: # bota
        codigos1 = ['0','1','2','3','4','5','6','7']
        print("Código enviado: ", codigos1[x])
        return  codigos1[x] 
    
    elif (x >= 10) and (x < 19): # camisa
        codigos2 = ['q','w','e','r','t','y','u','i']
        b = x % 10    
        print("Código enviado: ", codigos2[b])
        return codigos2[b]
    elif (x >= 20) and (x < 29): # camiseta
        codigos3 = ['a','s','d','f','g','h','j','k']
        c = x % 20    
        print("Código enviado: ", codigos3[c])
        return codigos3[c] 
    elif (x >= 30) and (x < 39): # tenis
        codigos4 = ['z','x','c','v','b','n','m',',']
        d = x % 30    
        print("Código enviado: ", codigos4[d])
        return codigos4[d] 

"""
#codifica_dados(11)
#codifica_dados(23)