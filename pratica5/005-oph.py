'''
Reproduzca el experimento de Openheim utilizando las imágenes puente.jpg
y ferrari-c.png. Visualice y comente los resultados.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


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
    
    # Imagens
    img1 = cv.imread("../imgs/puente.jpg", 0)
    img2 = cv.imread("../imgs/ferrari-c.png", 0)

    # Transformada 
    m1, f1 = tf_complexa(img1)
    m2, f2 = tf_complexa(img2)

    # Montando  
    x0, y0 = cv.polarToCart(m1, f2, angleInDegrees=False)
    x1, y1 = cv.polarToCart(m2, f1, angleInDegrees=False)
    im0 = cv.merge([x0, y0])
    im1 = cv.merge([x1, y1])

    # Inversa
    inv0 = cv.idft(im0, cv.DFT_COMPLEX_OUTPUT)
    inv1 = cv.idft(im1, cv.DFT_COMPLEX_OUTPUT)

    # Combinar imagens para mostrar
    r1 = cv.magnitude(inv0[:,:,0], inv0[:,:,1])
    r2 = cv.magnitude(inv1[:,:,0], inv1[:,:,1])
    
    # Normalizar
    r1 = cv.normalize(r1, 0, 255, cv.NORM_MINMAX)
    r2 = cv.normalize(r2, 0, 255, cv.NORM_MINMAX)

    #escala logaritmica
    #magn = cv.log(magn + 1)
    #centralizar
    #magn = np.fft.fftshift(magn, axes=None)
   

    # Mostrar
    plt.subplot(2,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Imagem 1")
    plt.imshow(img1, cmap="gray")
  
    plt.subplot(2,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Imagem 2")
    plt.imshow(img2, cmap="gray")

    plt.subplot(2,2,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("M1 + F2")
    plt.imshow(r1, cmap="gray")

    plt.subplot(2,2,4)
    plt.xticks([])
    plt.yticks([])
    plt.title("M2 + F1")
    plt.imshow(r2, cmap="gray")

    plt.show()



if __name__ == "__main__":
    main()


