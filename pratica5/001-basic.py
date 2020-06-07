'''
Construya imágenes binarias de: una lı́nea horizontal, una lı́nea vertical, un
cuadrado centrado, un rectángulo centrado, un cı́rculo.
¿Qué espera ver en las TDF de cada una de estás? ¿Cómo estima que estará
distribuida la energı́a?
Utilice cada una de las imágenes anteriores para calcular la TDF y visualice.
¿Se cumplieron sus pronósticos respecto de sus definiciones?
Varı́e las dimensiones y localización de los objetos en estas imágenes y repita
el análisis.
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


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
    lin_v = np.zeros([512,512], dtype=np.uint8)
    lin_v[256, 0:512] = 255
    # Linha horizontal
    lin_h = np.zeros([512,512], dtype=np.uint8)
    lin_h[0:512, 256] = 255
    # Círculo
    circ = np.zeros([512,512], dtype=np.uint8)
    cv.circle(circ, (256,256), 50, 255, -1)
    cv.circle(circ, (256,256), 49, 0, -1)
    # Quadrado
    quad = np.zeros([512,512], dtype=np.uint8)
    cv.rectangle(quad, (206,206), (306,306), 255, 1)
    # Retângulo
    ret = np.zeros([512,512], dtype=np.uint8)
    cv.rectangle(ret, (156,206), (356,306), 255, 1)
    # Retângulo transladado
    rett = np.zeros([512,512], dtype=np.uint8)
    cv.rectangle(rett, (100,100), (300,200), 255, 1)
    
    # Transformadas 
    lin_vf = tf_complexa(lin_v)
    lin_hf = tf_complexa(lin_h)
    circ_f = tf_complexa(circ)
    quad_f = tf_complexa(quad)
    ret_f  = tf_complexa(ret)
    rett_f = tf_complexa(rett)

    # Mostrar
    plt.subplot(2,6,1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(lin_v, cmap="gray")

    plt.subplot(2,6,2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(lin_h, cmap="gray")

    plt.subplot(2,6,3)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(circ, cmap="gray")

    plt.subplot(2,6,4)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(quad, cmap="gray")

    plt.subplot(2,6,5)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(ret, cmap="gray")

    plt.subplot(2,6,6)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(rett, cmap="gray")

    plt.subplot(2,6,7)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(lin_vf, cmap="bone")
    plt.colorbar()

    plt.subplot(2,6,8)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(lin_hf, cmap="bone")
    plt.colorbar()

    plt.subplot(2,6,9)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(circ_f, cmap="bone")
    plt.colorbar()

    plt.subplot(2,6,10)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(quad_f, cmap="bone")
    plt.colorbar()

    plt.subplot(2,6,11)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(ret_f, cmap="bone")
    plt.colorbar()
    
    plt.subplot(2,6,12)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(rett_f, cmap="bone")
    plt.colorbar()

    plt.show()



if __name__ == "__main__":
    main()


