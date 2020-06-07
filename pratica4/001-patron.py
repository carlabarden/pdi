'''
Ejercicio 1: Modelos de color y análisis
1. El archivo ‘patron.tif’ corresponde a un patrón de colores que varı́an por
columnas de rojo a azul. En este ejercicio se estudiará la información que con-
tienen las componentes de los diferentes modelos de color:
>> Visualice el patrón junto a las componentes [R, G, B] y [H, S, V]
>> Analice cómo varı́a la imagen en función de los valores de sus planos de
color. ¿Qué información brinda cada canal?

#TODO
>> Modifique las componentes H, S e V de la imagen para obtener un patrón
en RGB que cumpla con las siguientes condiciones:
– Variación de matices de azul a rojo.
– Saturación y brillo máximos.
>> Vizualice la nueva imagen y sus componentes en ambos modelos. Analice y
saque conclusiones.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def main():
    
    img = cv.imread("../imgs/patron.tif")
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Brilho máximo à imagem - componente V
    img_v = img_hsv.copy()
    #img_v[:,:, 2] = 255
    
    # Mostrar
    img = img[:,:,::-1]
    
    plt.subplot(4,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.imshow(img)
   
    # RGB
    plt.subplot(4,3,4)
    plt.xticks([])
    plt.yticks([])
    plt.title("R")
    plt.imshow(img[:,:,0])

    plt.subplot(4,3,5)
    plt.xticks([])
    plt.yticks([])
    plt.title("G")
    plt.imshow(img[:,:,1])

    plt.subplot(4,3,6)
    plt.xticks([])
    plt.yticks([])
    plt.title("B")
    plt.imshow(img[:,:,2])

    # HSV
    plt.subplot(4,3,7)
    plt.xticks([])
    plt.yticks([])
    plt.title("H")
    plt.imshow(img_hsv[:,:,0])

    plt.subplot(4,3,8)
    plt.xticks([])
    plt.yticks([])
    plt.title("S")
    plt.imshow(img_hsv[:,:,1])

    plt.subplot(4,3,9)
    plt.xticks([])
    plt.yticks([])
    plt.title("V")
    plt.imshow(img_hsv[:,:,2])


    plt.show()



if __name__ == "__main__":
    main()


