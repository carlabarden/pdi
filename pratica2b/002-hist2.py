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

#import math
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
    

def calc_hist(img):
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    return hist


def med_hist(hist, img):
    [altura, largura] = img.shape
    prob = map(lambda x, y: x * y, hist, range(len(hist)))
    med = reduce (lambda x, y: x + y, prob) 
    med *= 1/(altura*largura)
    
    return med


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
    
    m = med_hist(hist1, img1)
    print(m)
     
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
    #valores discretos, gráfico contínuo
    plt.subplot(3,5,11)
    plt.plot(hist1)
    
    plt.subplot(3,5,12)
    plt.plot(hist2)
    
    plt.subplot(3,5,13)
    plt.plot(hist3)
    
    plt.subplot(3,5,14)
    plt.plot(hist4)
    
    plt.subplot(3,5,15)
    plt.plot(hist5)
     
    plt.show()      
    


if __name__ == '__main__':
    main() 


