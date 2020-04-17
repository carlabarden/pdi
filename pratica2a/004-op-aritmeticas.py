'''
Ejercicio 3: Operaciones aritméticas
1. Implemente una función que realice las siguientes operaciones aritméticas
sobre dos imágenes que sean pasadas como parámetros:
a) Suma. Normalice el resultado por el número de imágenes.
b) Diferencia. Aplique las dos funciones de reescalado usadas tı́picamente
para evitar el desborde de rango (sumar 255 y dividir por 2, o restar el
mı́nimo y escalar a 255).
c) Multiplicación. En esta operación la segunda imagen deberá ser una
máscara binaria, muy utilizada para la extracción de la región de interés
(ROI) de una imagen.
'''

import math
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 
import argparse

'''
   Argumentos
'''
ap = argparse.ArgumentParser()
ap.add_argument("-img1", "--imagem1",  required=True, help="Imagem1")
ap.add_argument("-img2", "--imagem2",  required=True, help="Imagem2")


'''
    Soma
'''
def soma(img1, img2):
    #soma de duas imagens, normalizada
    img = 0.5 * img1 + 0.5 * img2
    return img 


'''
    Diferença
'''
def dif(img1, img2):
    
    img = img1 - img2
    #para evitar estouro do intervalo 0-255
    img += 255
    img = img/2 
    return img


'''
    Multiplicação
'''
def mul(img1, img2):
    img = img1 * img2
    return img


'''
    MAIN
'''
def main():

    args = vars(ap.parse_args())
    img1 = cv.imread(args["imagem1"],0) 
    img2 = cv.imread(args["imagem2"],0)  
 
    #operações
    s = soma(img1, img2)
    d = dif(img1, img2)
    m = mul(img1, img2)   
 
    #mostrar
    plt.subplot(1,3,1)  
    plt.imshow(s, cmap='gray')
    plt.title("Soma")

    plt.subplot(1,3,2)
    plt.imshow(d, cmap='gray') 
    plt.title("Diferença")

    plt.subplot(1,3,3)  
    plt.imshow(m, cmap='gray')
    plt.title("Multiplicação")

    plt.show()


if __name__ == '__main__':
    main() 


