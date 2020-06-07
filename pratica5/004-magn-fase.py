'''
Calcule la TDF de una imagen, obtenga magnitud y fase.
Genere una imagen reconstruida sólo con la magnitud considerando fase cero
y genere otra imagen reconstruida usando sólo fase de la imagen considerando
magnitud unitaria.
Visualice las imágenes y saque conclusiones sobre el aporte de ambas compo-
nentes a la reconstrucción de la imagen.
'''
# python 004-magn-fase.py -i ../imgs/coins.tif


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
    Realiza a Transformada de Fourier e retorna a magnitude e a fase.
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
    return magn, fase



'''
    MAIN
'''
def main():
    
    # Argumentos e Imagem
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"], 0)
    [alt, larg] = img.shape

    # Transformada 
    magn, fase = tf_complexa(img)

    # Montando  
    fase0 = np.zeros([alt,larg], dtype=np.float32)
    magn1 = np.ones([alt,larg],  dtype=np.float32)
    x0, y0 = cv.polarToCart(magn, fase0, angleInDegrees=False)
    x1, y1 = cv.polarToCart(magn1, fase, angleInDegrees=False)
    im0 = cv.merge([x0, y0])
    im1 = cv.merge([x1, y1])

    # Inversa
    inv0 = cv.idft(im0, cv.DFT_COMPLEX_OUTPUT)
    inv1 = cv.idft(im1, cv.DFT_COMPLEX_OUTPUT)

    # Combinar imagens para mostrar
    img0 = cv.magnitude(inv0[:,:,0], inv0[:,:,1])
    img1 = cv.magnitude(inv1[:,:,0], inv1[:,:,1])
    
    # Normalizar
    img0 = cv.normalize(img0, 0, 255, cv.NORM_MINMAX)
    img1 = cv.normalize(img1, 0, 255, cv.NORM_MINMAX)

    #escala logaritmica
    #magn = cv.log(magn + 1)
    #centralizar
    #magn = np.fft.fftshift(magn, axes=None)
   

    # Mostrar
    plt.subplot(1,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.imshow(img, cmap="gray")
  
    plt.subplot(1,3,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Preservando Magnitude")
    plt.imshow(img0, cmap="gray")
    
    plt.subplot(1,3,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Preservando Fase")
    plt.imshow(img1, cmap="gray")

    '''
    plt.subplot(1,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imgf, cmap="bone")
    plt.colorbar()
    '''

    plt.show()



if __name__ == "__main__":
    main()


