'''
Ejercicio 2: Transformaciones no lineales
1. Implemente la transformación logarı́tmica s = log(1 + r) y la transformación
de potencia s = r γ (c=1).
2. Realice el procesado sobre la imagen ’rmn.jpg’, utilizando los dos procesos
por separado.
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
ap.add_argument("-c", "--offset_c",  required=True, help="int: c")
ap.add_argument("-l", "--log",  required=False, help="True ou False")
ap.add_argument("-g", "--gama",  required=False, help="Expoente Gama")


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
    Tratar argumentos. Padrão: c = 1  e y = 1 
'''
def tratar_args(args):
    
    c = int(args["offset_c"])
    y = 1
   
    if args["log"] is None and args["gama"] is None: 
        return c, y

    if args["gama"]:
        y = float(args["gama"])
        return c, y

    return c, y 


'''
    MAIN
'''
def main():

    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"],0) 
    c, y = tratar_args(args)    
    img_t = np.zeros_like(img)
    transf = ""
     
    if args["log"]:
        lk = trans_log(c)
        img_t = cv.LUT(img, lk)
        transf = "LOG"
    elif args["gama"]:
        lk = trans_exp(c, y)
        img_t = cv.LUT(img, lk)
        transf = "GAMA"

    #mostrar
    plt.subplot(1,3,1)  
    plt.imshow(img, cmap='gray')
    plt.title("Imagem Original")

    plt.subplot(1,3,2)
    #graf lookup
    x = range(len(lk))
    plt.plot(x, lk) 
    plt.title(transf)

    plt.subplot(1,3,3)  
    plt.imshow(img_t, cmap='gray')
    plt.title("Imagem Transformada")

    plt.show()


if __name__ == '__main__':
    main() 


