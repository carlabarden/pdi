'''
Ejercicio 1: Filtros pasa-bajos
1. Genere diferentes máscaras de promediado, utilizando filtro de promediado o
caja (box filter) y el formato cruz.
Aplique los filtros sobre una imagen y verifique los efectos de aumentar el
tamaño de la máscara en la imagen resultante.
Ayuda: mask = np.ones((3,3),np.float32)/9

2. Genere máscaras de filtrado gaussianas con diferente σ y diferente tamaño.
Visualice y aplique las máscaras sobre una imagen. Compare los resultados
con los de un filtro de promediado del mismo tamaño.

3. Utilice el filtro de mediana sobre una imagen con diferentes tamaños de ven-
tana. Compare los resultados con los filtros anteriores para un mismo tamaño.
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

        # Para elemento central do kernel ter peso maior:
        '''
        # Para desconsiderar elemento central: -2
        qtd_cruz = 2 * tam_jan - 2
        # Elemento central da cruz
        elm_cen = 1/(peso/2)
        # Outros elementos:
        elm = 1/(elm_cen/qtd_cruz)
        
        for x in range(centro, centro + 1, 1):
            # Preencher cruz:
            # Linha 
            kernel[centro + x, centro] = elm
            # Coluna
            kernel[centro, centro + x] = elm

        # Elemento central
        kernel[centro, centro] = elm_cen
        '''
       

def main():
    # Argumentos e Imagem
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"], 0)
    
    # Gerar kernel
    k = gen_kernel(25, (25*25))
    # Aplicar filtro
    dst = cv.filter2D(img, -1, k) 
    # Filtro Gaussiano 
    gauss = cv.GaussianBlur(img, (25,25), 0)   
    # Filtro de Mediana
    med = cv.medianBlur(img, 25)


    # Mostrar
    plt.subplot(2,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Imagem Original")
    plt.imshow(img, cmap="gray")
    
    plt.subplot(2,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Filtro de Média")
    plt.imshow(dst, cmap="gray")
    
    plt.subplot(2,2,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Filtro Gaussiano ")
    plt.imshow(gauss, cmap="gray")
    
    plt.subplot(2,2,4)
    plt.xticks([])
    plt.yticks([])
    plt.title("Filtro de Mediana")
    plt.imshow(med, cmap="gray")

    plt.show()



if __name__ == "__main__":
    main()


