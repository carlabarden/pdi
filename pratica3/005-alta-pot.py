'''
2. Una forma de enfatizar las altas frecuencias sin perder los detalles de
bajas frecuencias es el filtrado de alta potencia. Implemente este 
procesamiento como la operación aritmética:
g(x, y) = Af (x, y) − P B(f (x, y)), con A ≥ 1.
* Investigue y pruebe métodos alternativos de cálculo en una pasada.
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
    Gerar kernel para filtro espacial. Tamanho ÍMPAR.
Filtro de promediado: pesos iguais, com soma sempre igual à um.
'''
def gen_kernel(tam_jan, peso, cruz=False):
    if not cruz:
        kernel = np.ones((tam_jan, tam_jan), np.float32)/peso
        return kernel
    else:
        kernel = np.zeros((tam_jan, tam_jan), np.float32)
        # Fazer cruz, posição centro
        centro = tam_jan // 2
        # Qtd elementos presentes na cruz: 2 * tam_jan - 1,
        
        # Para todos os elementos terem o mesmo peso:
        qtd_cruz = 2 * tam_jan - 1
        elm = 1/(peso/qtd_cruz)
        for x in range(-centro, centro + 1, 1):
            # Linha
            kernel[centro + x, centro] = elm
            # Coluna
            kernel[centro, centro + x] = elm
        
        return kernel


'''
    MAIN
'''
def main():
    # Argumento e Imagem
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"], 0)
    
    # Definir máscara
    k = gen_kernel(5, (5*5))
    # Imagem filtrada
    img_f = cv.filter2D(img, -1, k)
    # Alta Potência
    A = 9
    img_hb = cv.subtract(float(A)*img, 1.0*img_f)
    
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
    plt.title("Alta Potência")
    plt.imshow(img_hb, cmap="gray")
    
    plt.show()



if __name__ == "__main__":
    main()


