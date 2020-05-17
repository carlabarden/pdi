'''
Ejercicio 3: Filtros de acentuado
1. Obtenga versiones mejoradas de diferentes imágenes mediante el filtrado por
máscara difusa. Implemente el cálculo como
g(x, y) = f (x, y) − PB(f (x, y))
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


def main():
    # Argumento e Imagem
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"], 0)
    
    # Definir máscara
    k = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # Imagem filtrada
    img_f = cv.filter2D(img, -1, k)
    # Diferença
    img_md = cv.subtract(img, img_f)
    
    # Mostrar
    plt.subplot(1,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Imagem Original")
    plt.imshow(img, cmap="gray")
    
    plt.subplot(1,3,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Filtro")
    plt.imshow(img_f, cmap="gray")
    
    plt.subplot(1,3,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Máscara Difusa")
    plt.imshow(img_md, cmap="gray")
    
    plt.show()



if __name__ == "__main__":
    main()


