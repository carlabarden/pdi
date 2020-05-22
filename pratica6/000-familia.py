'''
Para las imágenes FAMILIA a.jpg, FAMILIA b.jpg y FAMILIA c.jpg, identifique el
tipo de ruido que afecta a cada una y calcule los parámetros estadı́sticos para
dichos ruidos. Elija apropiadamente el mejor filtro para cada caso, ajuste los
parámetros y restaure las imágenes.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
    Ler imagens.
'''
def ler_imgs():
    fa = cv.imread("../imgs/FAMILIA_a.jpg", 0)
    fb = cv.imread("../imgs/FAMILIA_b.jpg", 0)
    fc = cv.imread("../imgs/FAMILIA_c.jpg", 0)
    
    return fa, fb, fc


'''
    Definir janelas de análise. Uma janela de 50x50, localizada em uma área 
uniforme em p1 = (220, 500) e p2 = (270, 550).
'''    
def sub_img(img):
    p1 = (220, 500)
    p2 = (270, 550)
    roi = img[p1[1]:p2[1], p1[0]:p2[0]].copy()
    return roi


'''
    Cálculo e gráfico de histograma.
'''
def hist(img):
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    return hist 


'''
    Parâmetros estatísticos (média e variância).
'''
def stats(img):
    med = np.mean(img)
    var = np.var(img)
    return med, var    


'''
    Filtro espacial de ponto médio, 3x3. 
'''
def pto_med(img):
    dst = img.copy().astype(np.uint16)
    [lin,col] = img.shape[:2]
    # Criando kernel
    m = [img[0, 0]] * 9
    for y in range(1, lin - 1):
        for x in range(1, col - 1):
            # Inicializando kernel
            m[0] = img[y - 1, x - 1]
            m[1] = img[y, x - 1]
            m[2] = img[y + 1, x - 1]
            m[3] = img[y - 1, x]
            m[4] = img[y, x]
            m[5] = img[y + 1, x]
            m[6] = img[y - 1, x + 1]
            m[7] = img[y, x + 1]
            m[8] = img[y + 1, x + 1]

            a = np.max(m)
            b = np.min(m)
            c = (a.astype(int) + b.astype(int)) / 2
            dst[y, x] = c

    dst.astype(np.uint8)
    return dst 


'''
    Filtro espacial de média, 5x5.
'''
def med(img):
    # Kernel
    k = np.ones((5,5), np.float32)/25
    dst = cv.filter2D(img, -1, k)
    return dst



'''
    MAIN
'''
def main():
    
    # Ler imagens
    a, b, c = ler_imgs()
    
    # Janelas "homogêneas" para a análise
    ja = sub_img(a)
    jb = sub_img(b)
    jc = sub_img(c)

    # Histogramas
    ha = hist(ja)
    hb = hist(jb)
    hc = hist(jc)

    # Parâmetros estatítsicos de cada janela
    ma, va = stats(ja)
    mb, vb = stats(jb)
    mc, vc = stats(jc)

    print("Média e Variância, antes da restauração:")
    print(ma, va)
    print(mb, vb)
    print(mc, vc)
    
    # Restauração A
    ra = cv.medianBlur(a, 5)
    # Restauração B
    #rb = pto_med(b)
    rb = med(b) 
    # Restauração C
    rc = cv.medianBlur(c, 5)

    # Janelas "homogêneas" para a análise - restauradas
    jra = sub_img(ra)
    jrb = sub_img(rb)
    jrc = sub_img(rc)

    # Histogramas Imagens Restauradas
    hra = hist(jra)
    hrb = hist(jrb)
    hrc = hist(jrc)

    # Parâmetros estatítsicos de cada janela, depois da restauração
    mra, vra = stats(jra)
    mrb, vrb = stats(jrb)
    mrc, vrc = stats(jrc)
   
    print(" ") 
    print("Média e Variância, depois da restauração:")
    print(mra, vra)
    print(mrb, vrb)
    print(mrc, vrc)
    
    # Mostrar
    plt.subplot(3,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Restauração A")
    plt.imshow(ra, cmap="gray")

    plt.subplot(3,3,2)
    plt.xticks([])
    plt.yticks([])
    plt.title("Restauração B")
    plt.imshow(rb, cmap="gray")

    plt.subplot(3,3,3)
    plt.xticks([])
    plt.yticks([])
    plt.title("Restauração C")
    plt.imshow(rc, cmap="gray")

    plt.subplot(3,3,4)
    plt.xticks([])
    plt.yticks([])
    plt.title("Janela Filtrada A")
    plt.imshow(jra, cmap="gray")

    plt.subplot(3,3,5)
    plt.xticks([])
    plt.yticks([])
    plt.title("Janela Filtrada B")
    plt.imshow(jrb, cmap="gray")

    plt.subplot(3,3,6)
    plt.xticks([])
    plt.yticks([])
    plt.title("Janela Filtrada C")
    plt.imshow(jrc, cmap="gray")

    plt.subplot(3,3,7)
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hra[x], colors="c")
    plt.title("Histograma Restauração A")
    plt.grid()

    plt.subplot(3,3,8)
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hrb[x], colors="c")
    plt.title("Histograma Restauração B")
    plt.grid()
    
    plt.subplot(3,3,9)
    for x in range(256):
        plt.vlines(x=x, ymin=0, ymax=hrc[x], colors="c")
    plt.title("Histograma Restauração C")
    plt.grid()
    
    plt.show()



if __name__ == "__main__":
    main()


