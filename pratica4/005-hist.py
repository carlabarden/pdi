'''
Manejo de histograma: la imagen ‘chairs oscura.jpg’ posee poca luminosi-
dad. Usted debe mejorar la imagen a partir de la ecualización de histograma,
comparando los efectos de realizarla en RGB (por planos), en HSV (canal V) y
en HSI (canal I).
• Visualice la imagen original ‘chairs.jpg’, comparela con las imágenes re-
alzadas y discuta los resultados.
• Repita el proceso para otras imágenes de bajo contraste (por ejemplo
‘flowers oscura.tif’) y analice los resultados.
I = (B +G+R)/3
'''
# python 005-hist.py -i ../imgs/chairs_oscura.jpg


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse


'''
    Argumentos
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagem", required=True, help="Imagem")


'''
    Converter RGB para HSV e HSI.
'''
def rgb2hs(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hsi = hsv.copy()
    # HSV2HSI, BGR
    hsi[:,:,2] = np.divide(img[:,:,0] + img[:,:,1] + img[:,:,2], 3)
    return hsv, hsi


'''
    Equalizar histograma RGB.
'''
def eq_hist_rgb(img):
    eq = img.copy()
    eq[:,:,2] = cv.equalizeHist(img[:,:,2])
    eq[:,:,1] = cv.equalizeHist(img[:,:,1])
    eq[:,:,0] = cv.equalizeHist(img[:,:,0])
    return eq


'''
    MAIN
'''
def main():
    
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"])
    
    # Imagem RGB com histograma equalizado
    eq = eq_hist_rgb(img)
    
    # Imagem HSV/I com V/I equalizado
    hsv, hsi = rgb2hs(img)
    hsv[:,:,2] = cv.equalizeHist(hsv[:,:,2])
    hsi[:,:,2] = cv.equalizeHist(hsi[:,:,2])

    # Para mostrar HSV/I 
    hsv = cv.cvtColor(hsv, cv.COLOR_HSV2BGR) 
    #hsi = cv.cvtColor(hsi, cv.COLOR_HSV2BGR)
    
    # Mostrar
    plt.subplot(2,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.imshow(img[:,:,::-1])
    
    plt.subplot(2,2,2)
    plt.title("Histograma RGB Equalizado")
    plt.xticks([])
    plt.yticks([])
    plt.imshow(eq[:,:,::-1])

    plt.subplot(2,2,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Histograma V Equalizado")
    plt.imshow(hsv[:,:,::-1])
    
    plt.subplot(2,2,4)
    plt.xticks([])
    plt.yticks([])
    plt.title("Histograma I Equalizado")
    plt.imshow(hsi, cmap="hsv")
    
    plt.show()


if __name__ == "__main__":
    main()


