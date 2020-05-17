'''
Ejercicio 1: Filtros pasa-bajos
4. Los filtros pasa-bajos pueden utilizarse para localizar objetos grandes en
una escena. Aplique este concepto a la imagen ’hubble.tif’ y obtenga una ima-
gen de grises cuyos objetos correspondan solamente a los de mayor tamaño
de la original.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


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

       

def main():
    img = cv.imread("../imgs/hubble.tif", 0)
    
    # Gerar kernel
    k = gen_kernel(10, (10*10))
    # Aplicar filtro
    dst = cv.filter2D(img, -1, k) 
    # Limiar em 150
    ret, lim = cv.threshold(dst, 150, 255, cv.THRESH_BINARY)
    # Evitar "overflow"
    lim = lim/255
    # Multiplicar
    mul = lim * img

    # Mostrar
    plt.subplot(1,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Imagem Original")
    plt.imshow(img, cmap="gray")
    
    plt.subplot(1,3,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Filtro de Média e Limiar")
    plt.imshow(lim, cmap="gray")
    
    plt.subplot(1,3,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Multiplicação")
    plt.imshow(mul, cmap="gray")

    plt.show()



if __name__ == "__main__":
    main()


