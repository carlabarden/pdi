'''
Construya un filtro pasa-bajos ideal (cı́rculo de altura 1 sobre una matriz de
ceros). Cargue una imagen y fı́ltrela en el dominio de frecuencias, y recupere
la imagen suavizada. Visualice las imágenes y compárelas.
Repita el ejercicio para diferentes frecuencias de corte y compruebe la
aparición del fenómeno de Gibbs.
'''
#python 006-pbi.py -i ../imgs/chairs.jpg

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
    #escala logaritmica
    #magn = cv.log(magn + 1)
    #centralizar
    magn = np.fft.fftshift(magn, axes=None)
    return magn, fase


'''
    Filtro Ideal.
'''
def filtro_ideal(alt, larg, corte):
    filtro = np.zeros((alt,larg), dtype=np.float32)
    filtro = cv.circle(filtro, (alt//2, larg//2), int(alt*corte), 1, -1)
    return filtro


'''
    Aplicar Filtro em domínio frequencial.
'''
def aplicar_filtro(magn, filtro):
    # Filtro para o domínio da frequência
    fmg, ffs = tf_complexa(filtro)
    # Aplicar
    rmg = cv.mulSpectrums(magn, fmg, cv.DFT_ROWS)
    rmg = np.fft.ifftshift(rmg, axes=None)
    return rmg



'''
    MAIN
'''
def main():
    
    # Imagens
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"], 0)
    [alt, larg] = img.shape
    corte = 0.00005
    
    # Transformada 
    m, f = tf_complexa(img)

    # Filtro
    ft = filtro_ideal(alt, larg, corte)
    mf = aplicar_filtro(m, ft) 

    # Montando  
    x, y = cv.polarToCart(mf, f, angleInDegrees=False)
    im = cv.merge([x, y])

    # Inversa
    inv = cv.idft(im, cv.DFT_COMPLEX_OUTPUT)

    # Combinar imagens para mostrar
    r = cv.magnitude(inv[:,:,0], inv[:,:,1])
    
    # Normalizar
    r = cv.normalize(r, 0, 255, cv.NORM_MINMAX)

    # Mostrar
    plt.subplot(1,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.imshow(img, cmap="gray")
  
    plt.subplot(1,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Filtrada")
    plt.imshow(r, cmap="gray")

    plt.show()



if __name__ == "__main__":
    main()


