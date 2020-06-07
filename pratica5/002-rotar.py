'''
Construya una imagen de 512x512, que contenga una lı́nea vertical blanca
centrada y de un pixel de ancho sobre un fondo negro.
Rote la imagen 20 grados y extraiga una sección de 256x256 de la imagen
original y de la imagen rotada, de manera que las lı́neas tengan sus extremos
en los bordes superior e inferior, sin márgenes.
Visualice la TDF de ambas imágenes. Explique, utilizando argumentos in-
tuitivos, por qué las magnitudes de Fourier aparecen como lo hacen en las
imágenes, y a qué se deben las diferencias.
Ayuda: utilice dst = imutils.rotate(src, angle) de la biblioteca imutils
(https://github.com/jrosebr1/imutils).
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import imutils


'''
    Extrai ROI.
'''
def sub_img(img):
    p1 = (128, 128)
    p2 = (384, 384)
    roi = img[p1[1]:p2[1], p1[0]:p2[0]].copy()
    return roi


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
    # Linha vertical
    lin = np.zeros([512,512], dtype=np.uint8)
    lin[0:512, 256] = 255
    # Rotação
    rot = lin.copy()
    rot = imutils.rotate(rot, 20)
    # ROI
    im1 = sub_img(lin)
    im2 = sub_img(rot)
    # Transformadas 
    im1f = tf_complexa(lin)
    im2f = tf_complexa(rot)

    # Mostrar
    plt.subplot(2,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(im1, cmap="gray")

    plt.subplot(2,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(im2, cmap="gray")

    plt.subplot(2,2,3)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(im1f, cmap="bone")
    plt.colorbar()

    plt.subplot(2,2,4)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(im2f, cmap="bone")
    plt.colorbar()

    plt.show()



if __name__ == "__main__":
    main()


