'''
Ejercicio 2: Filtros pasa-altos
1. Defina máscaras de filtrado pasa-altos cuyos coeficientes sumen 1 y
aplı́quelas sobre diferentes imágenes. Interprete los resultados.
2. Repita el ejercicio anterior para máscaras cuyos coeficientes sumen 0. Com-
pare los resultados con los del punto anterior.
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
    
    # Definir máscaras soma 1
    k1_sum1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    k2_sum1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

    # Definir máscaras soma 0
    k1_sum0 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    k2_sum0 = np.array([[-5, -1, 5], [-2, 6, -2], [1, -1, -1]])
    
    # Imagens filtradas
    img1 = cv.filter2D(img, -1, k1_sum1)
    img2 = cv.filter2D(img, -1, k2_sum1)
    img3 = cv.filter2D(img, -1, k1_sum0)
    img4 = cv.filter2D(img, -1, k2_sum0)

    
    # Mostrar
    plt.subplot(3,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Imagem Original")
    plt.imshow(img, cmap="gray")
    
    plt.subplot(3,2,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Soma 1 - Kernel 1")
    plt.imshow(img1, cmap="gray")
    
    plt.subplot(3,2,4)
    plt.xticks([])
    plt.yticks([])
    plt.title("Soma 1 - Kernel 2")
    plt.imshow(img2, cmap="gray")

    plt.subplot(3,2,5)
    plt.xticks([])
    plt.yticks([])
    plt.title("Soma 0 - Kernel 1")
    plt.imshow(img3, cmap="gray")

    plt.subplot(3,2,6)
    plt.xticks([])
    plt.yticks([])
    plt.title("Soma 0 - Kernel 2")
    plt.imshow(img4, cmap="gray")
    plt.show()



if __name__ == "__main__":
    main()


