'''
2. Los archivos histo1.tif, histo2.tif, histo3.tif, histo4.tif e histo5.tif
contienen histogramas de imágenes con diferentes caracterı́sticas. Se pide:
    >> Analizando solamente los archivos de histograma y realice una descrip-
ción de la imagen a la que corresponden (¿es clara u oscura?, ¿tiene buen
contraste?, ¿el histograma me explica algo respecto de la ubicación de
los grises?, etc.).
    >> Anote la correspondencia histograma-imagen con los archivos imagenA.tif
a imagenE.tif, basándose en su análisis previo.
    >> Cargue las imágenes originales y muestre los histogramas. Comparelos
con sus respuestas del punto anterior.
    >> Obtenga y analice la utilidad de las siguientes propiedades estadı́sticas
de los histogramas: media, varianza, asimetrı́a, energı́a y entropı́a.
'''

import math
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 
from functools import reduce


def ler_hist():
    h1 = cv.imread("../imgs/histo1.tif", -1)
    h2 = cv.imread("../imgs/histo2.tif", -1)
    h3 = cv.imread("../imgs/histo3.tif", -1)
    h4 = cv.imread("../imgs/histo4.tif", -1)
    h5 = cv.imread("../imgs/histo5.tif", -1)
    
    return h1, h2, h3, h4, h5
    
    
def ler_imgs():
    img1 = cv.imread("../imgs/imagenA.tif", 0)
    img2 = cv.imread("../imgs/imagenB.tif", 0)
    img3 = cv.imread("../imgs/imagenC.tif", 0)
    img4 = cv.imread("../imgs/imagenD.tif", 0)
    img5 = cv.imread("../imgs/imagenE.tif", 0)
    
    return img1, img2, img3, img4, img5
    

'''
    Cálculo do histograma.
'''
def calc_hist(img):
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    return hist


'''
    Cálculo da média de luminosidade: med = sum(g * P(g)) = 1/MN*(sum(f(x,y)))
Descreve o brilho médio de uma imagem.
'''
def med_hist(img):
    med = np.mean(img)
    return med

'''
    Cálculo da Variância: var = sum(x - med)^2 * P(x) = 1/MN*(sum(f(x,y) - med)))
Descreve o contraste de uma imagem. 
'''
def variancia(img):
    var = np.var(img)
    return var


'''
    Cálculo da Assimetria: a = sum(x - med)^3 * P(x).
Se > 0, cauda direita --  +valores acima da média
Se < 0, cauda esquerda -- +valores abaixo da média
'''
def assimetria(img):
    hist = calc_hist(img)
    med = med_hist(img)
    assimetria = 0
    for x in range(len(hist)):
        assimetria += ((x - med) ** 3) * hist[x]

    return assimetria


'''
    Cálculo da Energia: E = sum(P(x)^2) 
Valor máximo de 1 para imagem com um único nível de cinza, diminui conforme
aumenta o número de níveis de cinza.
'''
def energia(img):
    hist = calc_hist(img)
    med = med_hist(img)
    energia = 0
    for x in range(len(hist)):
        energia += hist[x] ** 2
    
    return energia


'''
    Cálculo da Entropia: - sum(P(x) * log_base2[P(x)]
Inverso da Energia. Aumenta conforme o número de cinzas da imagem.
'''
def entropia(img):
    hist = calc_hist(img)
    entropia = 0
    for x in range(len(hist)):
        if hist[x] > 0:
            entropia += hist[x] * math.log2(hist[x])
   
    entropia =  entropia * -1
    
    return entropia


'''
    MAIN
'''
def main():
    
    #histogramas dados
    h1, h2, h3, h4, h5 = ler_hist()
    #imagens
    img1, img2, img3, img4, img5 = ler_imgs()
    #histogramas calculados
    hist1 = calc_hist(img1)
    hist2 = calc_hist(img2)
    hist3 = calc_hist(img3)
    hist4 = calc_hist(img4)
    hist5 = calc_hist(img5)
    
    #media, variancia, assimetria, energia e entropia
    
    print("Média")
    print(med_hist(img1), med_hist(img2), med_hist(img3),\
          med_hist(img4), med_hist(img5))

    print("Variância")
    print(variancia(img1), variancia(img2), variancia(img3),\
          variancia(img4), variancia(img5))
     
    print("Assimetria")
    print(assimetria(img1), assimetria(img2), assimetria(img3),\
          assimetria(img4), assimetria(img5))

    print("Energia")
    print(energia(img1), energia(img2), energia(img3),\
          energia(img4), energia(img5))

    print("Entropia")
    print(entropia(img1), entropia(img2), entropia(img3),\
          entropia(img4), entropia(img5))


    #mostrar
    #[:,:,::-1] para converter de bgr para rgb
    plt.subplot(3,5,1)
    plt.imshow(h1[:,:,::-1])
    
    plt.subplot(3,5,2)
    plt.imshow(h2[:,:,::-1])

    plt.subplot(3,5,3)
    plt.imshow(h3[:,:,::-1])

    plt.subplot(3,5,4)
    plt.imshow(h4[:,:,::-1])

    plt.subplot(3,5,5)
    plt.imshow(h5[:,:,::-1])

    plt.subplot(3,5,6)
    plt.imshow(img1, cmap="gray")

    plt.subplot(3,5,7)
    plt.imshow(img2, cmap="gray")

    plt.subplot(3,5,8)
    plt.imshow(img3, cmap="gray")

    plt.subplot(3,5,9)
    plt.imshow(img4, cmap="gray")

    plt.subplot(3,5,10)
    plt.imshow(img5, cmap="gray")
    
    #histogramas calculados
    plt.subplot(3,5,11)
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist1[x], colors="c")
    plt.grid()
    
    plt.subplot(3,5,12)
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist2[x], colors="c")
    plt.grid()
    
    plt.subplot(3,5,13)
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist3[x], colors="c")
    plt.grid()
    
    plt.subplot(3,5,14)
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist4[x], colors="c")
    plt.grid()
    
    plt.subplot(3,5,15)
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist5[x], colors="c")
    plt.grid()
     
    plt.show()      
    


if __name__ == '__main__':
    main() 


