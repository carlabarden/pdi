'''
Ejercicio 4.2:
Al final del proceso de manufactura de placas madres, de marca ASUS modelo
A7V600, se obtienen dos clases de producto final: A7V600-x y A7V600-SE.
Implemente un algoritmo, que a partir de una imagen, determine que tipo de
placa es. Haga uso de las técnicas de realce apendidas y utilice las imágenes
a7v600-x.gif y a7v600-SE.gif. Adapte el método de forma que contemple el
reconocimiento de imágenes que han sido afectadas por un ruido aleatorio
impulsivo (a7v600-x(RImpulsivo).gif y a7v600-SE(RImpulsivo).gif ).
'''

# coding:utf-8
import cv2 as cv
import math
import numpy as np
# para ler gifs
import gif2numpy
from matplotlib import pyplot as plt

#TODO: PASSAR POR ARGUMENTO AO PROG A IMAGEM A SER ANALISADA DA PLACA

'''
    Main
'''
def main():

    # ler gifs
    np_frames_x,  ext_x,  img_spec_x  = gif2numpy.convert("../imgs/a7v600-X.gif")
    np_frames_se, ext_se, img_spec_se = gif2numpy.convert("../imgs/a7v600-SE.gif")

    #ruido
    np_frames_x_ruido,  ext_x_ruido,  img_spec_x_ruido  = gif2numpy.convert("../imgs/a7v600-X(RImpulsivo).gif")
    np_frames_se_ruido, ext_se_ruido, img_spec_se_ruido = gif2numpy.convert("../imgs/a7v600-SE(RImpulsivo).gif")

    # só há um frame na imagem
    img_x  = np_frames_x[0]
    img_se = np_frames_se[0]

    # ruido
    x_ruido  = np_frames_x_ruido[0]
    se_ruido = np_frames_se_ruido[0]

    #todas as imagens tem o mesmo tamanho
    altura = ext_x[0]['height']
    largura = ext_x[0]['width']

    # limiar, para binarizar imgs
    ret, bin_x  = cv.threshold(img_x,50,255,cv.THRESH_BINARY)
    ret, bin_se = cv.threshold(img_se,50,255,cv.THRESH_BINARY)

    ret, bin_x_ruido  = cv.threshold(x_ruido, 50, 255, cv.THRESH_BINARY)
    ret, bin_se_ruido = cv.threshold(se_ruido, 50, 255, cv.THRESH_BINARY)

    # diferença, para criar máscaras
    mask_x  = bin_se - bin_x
    mask_se = bin_x  - bin_se

    # teste
    tst1 = cv.bitwise_and(mask_x,  bin_x)
    tst2 = cv.bitwise_and(mask_se, bin_x)
    tst3 = cv.bitwise_and(mask_x,  bin_se)
    tst4 = cv.bitwise_and(mask_se, bin_se)
    # ruido
    tst5 = cv.bitwise_and(mask_x, bin_x_ruido)
    tst6 = cv.bitwise_and(mask_x, bin_se_ruido)
    tst7 = cv.bitwise_and(mask_se, bin_x_ruido)
    tst8 = cv.bitwise_and(mask_se, bin_se_ruido)

    # descobrir porcentagem de limiar
    c_xr = np.count_nonzero(tst5)
    c_ser= np.count_nonzero(tst8)

    ctst6 = np.count_nonzero(tst6)
    ctst7 = np.count_nonzero(tst7)

    print("non zero x: ", c_xr)
    print("non zero se: ", c_ser)
    print("non zero tst6: ", ctst6)
    print("non zero tst7: ", ctst7)
    print("percent x ruido: ", round((c_xr/(altura*largura)*100),2))
    print("percent se ruido: ", round((c_ser/(altura*largura)*100),2))
    print("tst6: ",  round((ctst6/(altura*largura)*100),2))
    print("tst7: ",  round((ctst7/(altura*largura)*100),2))

    #mostrar figuras
    plt.figure()

    plt.subplot(2,4,1)
    plt.imshow(tst1)
    plt.title("mask_x and bin_x")

    plt.subplot(2,4,2)
    plt.imshow(tst4)
    plt.title("mask_se and bin_se")

    plt.subplot(2,4,3)
    plt.imshow(tst3)
    plt.title("mask_x and bin_se")

    plt.subplot(2,4,4)
    plt.imshow(tst2)
    plt.title("mask_se and bin_x")

    # ruido
    plt.subplot(2,4,5)
    plt.imshow(tst5)
    plt.title("mask_x and bin_x_ruido")

    plt.subplot(2,4,6)
    plt.imshow(tst6)
    plt.title("mask_x and bin_se_ruido")

    plt.subplot(2,4,7)
    plt.imshow(tst7)
    plt.title("mask_se and bin_x_ruido")

    plt.subplot(2,4,8)
    plt.imshow(tst8)
    plt.title("mask_se and bin_se_ruido")

    plt.show()


if __name__ == '__main__':
    main()
