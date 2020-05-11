'''
2. Realice una aplicación de preprocesamiento para OCR.
La imagen de entrada es un texto escaneado (puede utilizar parrafo0.jpg
y parrafo1.jpg), usted debe identificar si el texto está rotado y de ser ası́,
debe corregir la orientación del texto.
(Opcional): busque otras imágenes en peores condiciones, o genere algunas
utilizando escaners o cámaras, y agregue algunas funcionalidades al código
que le permita realzar la imagen, utilizando todo lo que ya conoce.
'''

import imutils 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse

'''
    Argumentos
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagem", required=True, help="Caminho da Imagem")


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
    return magn, fase


'''
    Recebe o Espectro de Fourier da imagem e devolve o ângulo (em graus)
em que ela está rotacionada. Isso é feito através da limiarização, para
encontrar as componentes do espectro que contém mais energia (em branco).
Após, são feitos dois perfis de intensidade verticais a +5 e -5 píxeis de 
distância do ponto x central da imagem, para obter as coordenadas dos pontos
em branco. Através dessas coordenadas, é gerado um vetor e calculado a arctang
de suas componentes x e y, para enfim obter o ângulo de rotação.
'''
def encontrar_angulo(magn, cx, alt):
    # Perfis de Intensidade 
    vpi1 = np.zeros(alt, dtype=np.float32)
    vpi2 = np.zeros(alt, dtype=np.float32)
    vpi1 = magn[0:alt, cx - 5]
    vpi2 = magn[0:alt, cx + 5]
    
    # Coordenadas das maiores intensidades 
    coord1 = (np.where(vpi1>0))
    coord2 = (np.where(vpi2>0))
    ind1 = cx-5, coord1[0][0]
    ind2 = cx+5, coord2[0][0]
    
    # Vetor normalizado para obter a direção
    # V = B - A
    vx  = ind1[0] - ind2[0]
    vy  = ind1[1] - ind2[1]
    vxn = vx/(vx**2 + vy**2)**(1/2)
    vyn = vy/(vx**2 + vy**2)**(1/2)
    
    # Ângulo em graus
    ang = np.arctan(vy/vx)*180/np.pi
    return ang


'''
    MAIN
'''
def main():
    # Argumentos e Imagem
    args = vars(ap.parse_args())
    img = cv.imread(args["imagem"], 0)

    # Transformada 
    magn, fase = tf_complexa(img)
    
    norm = cv.normalize(magn, 0, 1, cv.NORM_MINMAX)
    ret, magn_t = cv.threshold(norm,0.0015 , 1,  cv.THRESH_BINARY)
    
    [alt, larg] = magn.shape
    [cy, cx] = alt // 2, larg // 2

    # Perfil de intensidade vertical do centro da magnitude após o limiar
    vpi_c = np.zeros(alt, dtype=np.float32)
    vpi_c = magn_t[0:alt, cx]
        
    # Verificar se é a imagem 0 ou a 1. A que está reta contém muitos
    # elementos "1" na coluna central da magnitude.
    if np.count_nonzero(vpi_c) < 10:
        ang =  encontrar_angulo(magn_t, cx, alt) 
        print("O ângulo de rotação é: ", ang) 
        # Rotacionar
        img_r = imutils.rotate(img, ang * -0.5)

        # Mostrar
        plt.subplot(1,2,1)
        plt.xticks([])
        plt.yticks([])
        plt.title("Texto Original")
        plt.imshow(img, cmap="gray")
        
        plt.subplot(1,2,2)
        plt.xticks([])
        plt.yticks([])
        plt.title("Texto Rotacionado")
        plt.imshow(img_r, cmap="gray")

        plt.show()
    
    else:
        print("O texto está com a orientação correta")
       
        # Mostrar 
        plt.xticks([])
        plt.yticks([])
        plt.title("Texto Original")
        plt.imshow(img, cmap="gray")

        plt.show()



if __name__ == "__main__":
    main()


