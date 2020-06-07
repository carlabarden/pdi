'''
Habitualmente las imágenes que se relevan en partes no visibles del espectro
(como las de infrarrojos, radar, etc.) se encuentran en escala de grises. Para
resaltar zonas de interés, se pueden asignar colores a rangos especı́ficos de 
intesidades. Para este ejercicio debe utilizar la imagen ‘rio.jpg’ y resaltar
todas las áreas con acumulaciones grandes de agua (rı́o central, ramas mayores
y pequeños lagos) en color amarillo.

A continuación le proponemos una guı́a metodológica para resolver ésto, aunque
usted puede proponer otra:
(a)analizar el histograma y estimar el rango de valores en el que se 
representa el agua,
(b)generar una imagen color cuyos canales son copia de la imagen de intensidad,
(c) recorrer la imagen original y asignar el color amarillo a los pı́xeles cuyas
intensidades están dentro del rango definido,
(d)visualizar la imagen resultante y ajustar el rango de grises de ser 
necesario. Consejo: ésto se hace más simple utilizando trackbars.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def main():
   
    img = cv.imread("../imgs/rio.jpg", 0)
    img_c = cv.merge([img, img, img]) 
    [alt, larg, ch] = img_c.shape
   
    # Rio entre 0 e 10
    for x in range(alt):
        for y in range(larg):
            if img_c[x,y,0] < 15 and img_c[x,y,0]>=0:
                img_c[x,y,0] = 0
                img_c[x,y,1] = 255
                img_c[x,y,2] = 255

    # Mostrar
    plt.subplot(1,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.imshow(img, cmap="gray")
    
    # Histograma 
    plt.subplot(1,3,2)
    plt.title("Histograma")
    plt.hist(img.flatten(), 255)

    plt.subplot(1,3,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Rio Amarelo")
    plt.imshow(img_c[:,:,::-1])
    
    plt.show()


if __name__ == "__main__":
    main()


