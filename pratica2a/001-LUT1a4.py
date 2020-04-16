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
ap.add_argument("-a", "--fator_a",  required=False, help="int: a")
ap.add_argument("-c", "--offset_c",  required=False, help="int: c")
#para passar números negativos
ap.add_argument("-na", "--n_fator_a",  required=False, help="int: -a")
ap.add_argument("-nc", "--n_offset_c",  required=False, help="int: -c")


'''
True color: o pixel contém a intensidade em nível de cinza (ou a cor) que
deve ser usada para visualizar a imagem.

Color table: o pixel contém um índice de uma tabela de cores
(look-up table = LUT). Cada entrada da LUT pode conter 1 ou
mais elementos.
'''
# s = a*r + c
# a = fator de amplificação
# c = offset 
def lut_linear(a, c):
    #vetor com a escala de cores
    s = np.zeros(256)
    
    for r in range(len(s)):
        s[r] = a * r + c
        
        # evitar estouro do intervalo [0,255]
        if s[r] > 255:
            s[r] = 255
        if s[r] < 0:
            s[r] = 0
    
    return s


'''
    Tratar argumentos. Padrão: a = 1 e c = 0
'''
def tratar_args(args):
    
    a = 1
    c = 0
   
    if args["fator_a"] is None and args["n_fator_a"] is None and \
       args["offset_c"] is None and args["n_offset_c"] is None:
        return a, c

    if args["fator_a"]:
        a = int(args["fator_a"])
    elif args["n_fator_a"]:
        a = -1 * int(args["n_fator_a"])

    if args["offset_c"]:
        c = int(args["offset_c"])
    elif args["n_offset_c"]:
        c = -1 * int(args["n_offset_c"])             

    return a, c


'''
    MAIN
'''
def main():

    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"],0) 
    a, c = tratar_args(args)
   #print(a, c)
   
    #lookup
    lk = lut_linear(a, c)
    img_lut = cv.LUT(img, lk)
    
    #mostrar
    plt.subplot(1,3,1)  
    plt.imshow(img, cmap='gray')
    plt.title("Imagem Original")

    plt.subplot(1,3,2)
    #graf lookup
    x = range(len(lk))
    plt.plot(x, lk) 
    plt.title("LUT")

    plt.subplot(1,3,3)  
    plt.imshow(img_lut, cmap='gray')
    plt.title("Imagem Transformada")

    plt.show()


if __name__ == '__main__':
    main() 


