'''
Ejercicio 1: Transformaciones lineales de una imagen
Conociendo la ecuación general de una transformación lineal:
s = ar + c
con r: valor de entrada, a: factor de ganancia y c: offset,
realice los siguientes ejercicios:
1. Implemente una LUT del mapeo entre la entrada y la salida.
2. Pruebe la rutina con diferentes juegos de coeficientes a y c, sobre diversas
imágenes, y muestre en una misma ventana la imagen original, el mapeo
aplicado y la imagen obtenida.
3. Implemente el negativo de la imagen de entrada.
4. Genere diversas LUT con estiramientos y compresiones lineales por tramos
de la entrada, y pruebe los resultados sobre diversas imágenes.
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
ap.add_argument("-img", "--imagem",  required=True, help="Imagem")

'''
True color: o pixel contém a intensidade em nível de cinza (ou a cor) que
deve ser usada para visualizar a imagem.

Color table: o pixel contém um índice de uma tabela de cores
(look-up table = LUT). Cada entrada da LUT pode conter 1 ou
mais elementos.
'''
def negativo():
    #vetor com a escala de cores
    s = np.zeros(256)
    
    for r in range(len(s)):
        s[r] = 255 - r
    
    return s


'''
    MAIN
'''
def main():

    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"],0) 
   
    #negativo
    lk_n = negativo()
    img_n = cv.LUT(img, lk_n)
    
    #mostrar
    plt.subplot(1,3,1)  
    plt.imshow(img, cmap='gray')
    plt.title("Imagem Original")

    plt.subplot(1,3,2)
    #graf lookup
    x = range(len(lk_n))
    plt.plot(x, lk_n) 
    plt.title("Negativo")

    plt.subplot(1,3,3)  
    plt.imshow(img_n, cmap='gray')
    plt.title("Imagem Transformada")

    plt.show()


if __name__ == '__main__':
    main() 


