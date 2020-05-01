'''
2. El gobierno de la provincia de Misiones lo ha contratado para realizar una
aplicación que sea capaz de detectar zonas deforestadas. Para desarrollar un
primer prototipo le han suministrado una imagen satelital (Deforestacion.png)
en la que un experto ya delimitó el área donde deberı́a existir monte nativo y
sobre la cual usted debe trabajar. Se requiere que su aplicación:
• Segmente y resalte en algún tono de rojo el área deforestada.
• Calcule el área total (hectáreas) de la zona delimitada, el área de la zona
que tiene monte y el área de la zona deforestada.
• (Opcional) Detecte automáticamente la delimitación de la zona.
Ayuda:
• Explore todos los canales de los diferentes modelos de color para determinar
cual (o que combinación de ellos) le proporciona más información.
• Como su objetivo es la segmentación de las distintas zonas, piense que her-
ramienta (de las que ya conoce) le permitirı́a lograr zonas más homogéneas.
• Utilice la referencia de la esquina inferior izquierda para computar los
tamaños de las regiones.
'''

import math
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 


'''
    Detecção automática de bordas: perfis de intensidade horizontal e vertical
para calcular ROI através das bordas internas do quadrado demarcado.
'''
def detecta_roi(img_roi):
    
    img_roi = cv.cvtColor(img_roi, cv.COLOR_BGR2GRAY)
    ret, img = cv.threshold(img_roi, 200, 255, cv.THRESH_BINARY)
    [altura, largura] = img.shape

    #linha do centro da imagem
    vpi_lin = np.zeros(largura, dtype=np.uint8)
    vpi_lin = img[int(altura/2), 0:largura]
    
    #coluna do centro da imagem
    vpi_col = np.zeros(altura, dtype=np.uint8)
    vpi_col = img[0:altura, int(largura/2)]

    roi_x = []
    roi_y = [] #correspondência pelo índice
    
    linha = False
    for x in range(largura):
        if vpi_lin[x] == 255 and not linha: 
            linha = True
            roi_x.append(x)
        elif vpi_lin[x] != 255 and linha:
            linha = False
            roi_x.append(x - 1)
    
    linha = False
    for x in range(altura):
        if vpi_col[x] == 255 and not linha:
            linha = True
            roi_y.append(x)
        elif vpi_col[x] != 255 and linha:
            linha = False
            roi_y.append(x - 1)

    # filtra as coordenadas da parte interna do quadrado
    # as coordenadas centrais são as que interessam
    del roi_x[0]
    del roi_x[2]
    del roi_y[0]
    del roi_y[2]

    return roi_x, roi_y
        

'''
    Cálculo da área total da zona delimitada, da zona com floresta e da zona
desmatada.
'''
def calc_areas(img):
    
    # área total = área da imagem
    [altura, largura] = img.shape
    area_t = altura * largura
    # área florestada = branca
    area_f = cv.countNonZero(img)
    # área desmatada = negro
    area_d = area_t - area_f 
    
    #perc_f = area_f / area_t * 100           
    perc_d = area_d / area_t * 100

    # 90px = 200m : área do pixel
    area_p = pow(200/90, 2)
    # hectares
    hect   = area_p * area_t * 0.0001
    hect_d = area_p * area_d * 0.0001
    hect_f = area_p * area_f * 0.0001

    print("Área Total ROI - hectares: ", round(hect, 2))
    print("Área Desmatada - hectares: ", round(hect_d, 2))
    print("Área Florestada- hectares: ", round(hect_f, 2))
    print("Percentual desmatado: ",      round(perc_d, 2))


'''
    MAIN
'''
def main():

    img_bgr = cv.imread("../imgs/Deforestacion.png")

    # para ver qual canal contém mais informações
    img = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)  
    x, y = detecta_roi(img_bgr)
    img = img[y[0]:y[1], x[0]:x[1]]
    
    h, s, v = cv.split(img) 
    
    n = 33    
    # filtro passa baixa para diminuir ruído
    s_f = cv.GaussianBlur(s, (n,n), 0)
    
    # limiar
    ret, limiar = cv.threshold(s_f, 50, 255, cv.THRESH_BINARY)

    # calcular áreas
    calc_areas(limiar) 
    
    # parte desmatada em vermelho
    roi  = img_bgr[y[0]:y[1], x[0]:x[1]]
    roi  = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    roi  = cv.merge((roi, roi, roi))
    mask = cv.merge((limiar, limiar, limiar))
    # trocar preto por vermelho
    mask[:,:,0] = 255 
    alpha = 0.7
    soma = cv.addWeighted(roi, alpha, mask, (1 - alpha), 0.0)

    plt.imshow(soma)#[:,:,::-1])
    plt.title("ROI")
    
    plt.show()




if __name__ == '__main__':
    main() 


