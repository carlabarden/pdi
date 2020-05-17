'''
4. (Opcional): Investigue la ecualización adaptativa de histogramas CLAHE
(Contrast Limited Adaptive Histogram Equalization)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse


'''
    Argumentos
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagem", required=True, help="Caminho da Imagem")


'''
    MAIN
'''
def main():
    # Argumento e Imagem
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"], 0)
    
    # CLAHE
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_cl = clahe.apply(img)
    # Histogramas
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    hist_cl = cv.calcHist([img_cl], [0], None, [256], [0, 256])
    
    # Mostrar
    plt.subplot(2,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Imagem Original")
    plt.imshow(img, cmap="gray")
    
    plt.subplot(2,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Imagem Equalizada")
    plt.imshow(img_cl, cmap="gray")

    plt.subplot(2,2,3)
    plt.title("Histograma Imagem Original")
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist[x], colors="c")
    plt.grid()
    
    
    plt.subplot(2,2,4)
    plt.title("Histograma Imagem CLAHE")
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist_cl[x], colors="c")
    plt.grid()
   
    plt.show()


if __name__ == "__main__":
    main()


