'''
2. Genere una función cuyo resultado sea una imagen donde los pixeles tengan 
los colores complementarios a los de la original. Utilice las componentes del
modelo HSV y la imagen ‘rosas.jpg’.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


'''
    Inverter cor (RGB)
'''
def invt_rgb(img):
    i_rgb = 255 - img
    return i_rgb


'''
    Inverter cor e intensidade (HSV)
'''
def invt_hsv(img):
    [alt, larg, ch] = img.shape
    i_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    i_hsv = i_hsv.astype(np.uint16)

    # Inverter componente H
    for x in range(alt):
        for y in range(larg):
            aux = img[x, y, 0] + 90
            aux = aux % 180
            i_hsv[x, y, 0] = aux
    
    # Inverter componente V
    i_hsv[:,:,2] = 255 - i_hsv[:,:,2]
    i_hsv = i_hsv.astype(np.uint8)
    return i_hsv


def main():
   
    img = cv.imread("../imgs/rosas.jpg")
    
    # Imagem invertida em RGB
    img_rgb = invt_rgb(img)

    # Imagem invertida HSV
    img_hsv = invt_hsv(img)
    # Para ver
    img_hsv = cv.cvtColor(img_hsv, cv.COLOR_HSV2BGR)

    # Mostrar
    plt.subplot(1,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.imshow(img[:,:,::-1])

    plt.subplot(1,3,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("RGB")
    plt.imshow(img_rgb[:,:,::-1])

    plt.subplot(1,3,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("HSV")
    plt.imshow(img_hsv[:,:,::-1])

    plt.show()


if __name__ == "__main__":
    main()


