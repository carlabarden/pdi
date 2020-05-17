'''
3. Cargue una imagen y realice la ecualización de su histograma.
img equ = cv2.equalizeHist(img)
Muestre en una misma ventana la imagen original, la versión ecualizada
y sus respectivos histogramas.
Estudie la información suministrada por los histogramas. ¿Qué diferen-
cias nota respecto a las definiciones teóricas?
Repita el análisis para distintas imágenes.
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

    # Histograma
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    # Equalização
    eq = cv.equalizeHist(img)
    # Histograma Imagem Equalizada
    hist_eq = cv.calcHist([eq], [0], None, [256], [0, 256])

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
    plt.imshow(eq, cmap="gray")

    plt.subplot(2,2,3)
    plt.title("Histograma Imagem Original")
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist[x], colors="c")
    plt.grid()
    
    
    plt.subplot(2,2,4)
    plt.title("Histograma Imagem Equalizada")
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hist_eq[x], colors="c")
    plt.grid()
   
    plt.show()


if __name__ == "__main__":
    main()


