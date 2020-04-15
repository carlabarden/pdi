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
from matplotlib import pyplot as plt
import argparse

'''
    Argumentos
'''
ap = argparse.ArgumentParser()
ap.add_argument("-ipx", "--imagem_placa_x",  required=True, help="Imagem Placa A7V600-X")
ap.add_argument("-ips", "--imagem_placa_se", required=True, help="Imagem Placa A7V600-SE")
ap.add_argument("-img", "--imagem_analise",  required=True, help="Imagem a ser analisada")


'''
    Ler um gif.
'''
def ler_gif(gif):
    aux = cv.VideoCapture(gif)
    ret, img = aux.read()
    return img


'''
    Torna a imagem binária executando a transformação de Limiar.
'''
def binarizar(img):
    ret, img_bin  = cv.threshold(img,50,255,cv.THRESH_BINARY)
    return img_bin


'''
    Cria uma máscara através da diferença entre duas imagens binárias.
'''
def criar_mascara(img1, img2):
    return img1 - img2


'''
    Aplica a máscara à imagem.
'''
def aplicar_mascara(img, mask):
    img_mask = cv.bitwise_and(mask, img)
    return img_mask


'''
    Verifica se é ruído, considerando até 1% como sendo ruído (valor empírico)
e valores maiores como sendo placas distintas.
'''
def verificar_ruido(placa):
    [altura, largura, canais] = placa.shape
    # Contando os pixeis brancos da imagem binaria
    n_brancos = np.count_nonzero(placa == 255)
    # Calculando o percentual que eles representam da imagem
    percentual = round((n_brancos/(altura*largura)*100),2)
    if (percentual < 1.00):
        return True
    else:
        return False


'''
    Main
'''
def main():
    # args
    args = vars(ap.parse_args())

    # ler imagens
    img_x  = ler_gif(args["imagem_placa_x"])
    img_se = ler_gif(args["imagem_placa_se"])
    # imagem a ser analisada
    img = ler_gif(args["imagem_analise"])

    str_x  = "A7V600-X"
    str_se = "A7V600-SE"
    veredicto = ""

    # imagens binárias - limiar
    bin_x   = binarizar(img_x)
    bin_se  = binarizar(img_se)
    bin_img = binarizar(img)

    # gerar máscaras
    mask_x  = criar_mascara(bin_se, bin_x)
    mask_se = criar_mascara(bin_x, bin_se)

    # aplicar máscaras
    img_mask_x  = aplicar_mascara(mask_x,  bin_img)
    img_mask_se = aplicar_mascara(mask_se, bin_img)

    # reconhecer qual placa é -- TRUE: < 1%    FALSE: >=1%
    if verificar_ruido(img_mask_x):
        veredicto = str_x
    elif verificar_ruido(img_mask_se):
        veredicto = str_se
    else:
        veredicto = "Imagem não reconhecida"

    print("")
    print(veredicto)
    print("")

    plt.figure()
    plt.imshow(img)
    plt.title(veredicto)
    plt.show()


if __name__ == '__main__':
    main()
