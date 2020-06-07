'''
Cargue diferentes imágenes y visualice la magnitud de la TDF. Infiera, a
grandes rasgos, la correspondencia entre componentes frecuenciales y detalles
de las imágenes.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse

'''
    Argumentos
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagem", required=True, help="Imagem")


'''
    Realiza a Transformada de Fourier e retorna a magnitude (já com a função
de log aplicada e centralizada) e a fase.
''' 
def tf_complexa(im):
    # Para armazenar resultado da transformação
    planos = [np.float32(im), np.zeros(im.shape, np.float32)]
    tf = cv.merge(planos)
    # Transformada 
    tf = cv.dft(tf, cv.DFT_COMPLEX_OUTPUT)
    #calcular magnitude, planos[0] = real, planos[1] = imaginário
    planos = cv.split(tf)
    magn, fase = cv.cartToPolar(planos[0],planos[1], angleInDegrees=False)
    #escala logaritmica
    magn = cv.log(magn + 1)
    #centralizar
    magn = np.fft.fftshift(magn, axes=None)
    #return magn, fase
    return magn



'''
    MAIN
'''
def main():
    
    # Argumentos e Imagem
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"])
    
    # Transformada 
    img_pb = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    imgf = tf_complexa(img_pb)

    # Mostrar
    plt.subplot(1,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img[:,:,::-1])

    plt.subplot(1,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imgf, cmap="bone")
    plt.colorbar()

    plt.show()



if __name__ == "__main__":
    main()


