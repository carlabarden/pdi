'''
Realce mediante acentuado: utilice la imagen ‘camino.tif’ que se observa de-
senfocada. Usted debe mejorar la imagen aplicando un filtro pasa altos de suma
1. Compare los resultados de procesar la imagen en los modelos RGB, HSV y
HSI.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


'''
    Aplicar filtro k em imagem RGB (por canal).
'''
def filtrar_rgb(img, k):
    img[:, :, 0] = cv.filter2D(img[:,:,0], -1, k)
    img[:, :, 1] = cv.filter2D(img[:,:,1], -1, k)
    img[:, :, 2] = cv.filter2D(img[:,:,2], -1, k)
    return img


'''
    MAIN
'''
def main():
   
    img = cv.imread("../imgs/camino.tif")
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Filtro Passa Alto 3x3 com soma 1
    k = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]],dtype=np.uint8)
    # Imagem RGB filtrada
    rgb_f = filtrar_rgb(img, k)
    # Imagem HSV filtrada (canal V)
    hsv_f = hsv.copy()
    hsv_f[:,:,2] = cv.filter2D(hsv_f[:,:,2], -1, k)
    # Para exibir imagens hsv
    hsv_f = cv.cvtColor(hsv_f, cv.COLOR_BGR2HSV)
    
    # Mostrar
    plt.subplot(1,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.imshow(img)#[:,:,::-1])
    
    plt.subplot(1,3,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Fitro RGB")
    plt.imshow(rgb_f[:,:,::-1])

    plt.subplot(1,3,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Filtro HSV")
    plt.imshow(hsv_f[:,:,::-1])
    
    plt.show()


if __name__ == "__main__":
    main()


