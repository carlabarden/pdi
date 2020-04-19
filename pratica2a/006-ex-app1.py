'''
Ejercicio 4: Trabajos de aplicación
1. Utilizando las técnicas aprendidas, descubra que objetos no están perceptibles en la imagen earth.bmp y realce la imagen de forma que los objetos se
vuelvan visibles con buen contraste sin realizar modificaciones sustanciales
en el resto de la imagen.
'''

import math
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 


'''
    Transformação Logarítmica: s = c * log(1+r), com r > 0 e c = 1
'''
def trans_log(c):
    s = np.zeros(256)
    
    for r in range(len(s)):
        s[r] = c * math.log(1+r)

    #"normalizar"
    s = 255 * s / s.max()

    return s


'''
    Transformação Exponencial: s = c * r ^ Y (Y = gama) , c e y > 0
    OU s = c (r + E) ^ Y, sendo E (epsilon) um offset.
'''    
def trans_exp(c, y):
    s = np.zeros(256)
    
    for r in range(len(s)):
        s[r] = c * (r ** y)

    #"normalizar"
    s = 255 * s / s.max()

    return s


'''
    MAIN
'''
def main():

    img = cv.imread("../imgs/earth.bmp", 0)
   
    #log
    log = trans_log(1)
    img_l = cv.LUT(img, log)
    #gama
    exp = trans_exp(1,1.5)
    img_g = cv.LUT(img, exp)
    
    #mostrar
    plt.subplot(1,3,1)  
    plt.imshow(img, cmap='gray')
    plt.title("Imagem Original")

    plt.subplot(1,3,2)  
    plt.imshow(img_l, cmap='gray')
    plt.title("LOG")

    plt.subplot(1,3,3)  
    plt.imshow(img_g, cmap='gray')
    plt.title("GAMA")

    plt.show()


if __name__ == '__main__':
    main() 


