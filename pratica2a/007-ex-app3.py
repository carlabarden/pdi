'''
3. En una fábrica de medicamentos se desea implementar un sistema para la
inspección visual automática de blisters en la lı́nea de empaquetado. La ad-
quisición de la imagen se realiza en escala de grises mediante una cámara
CCD fija y bajo condiciones controladas de iluminación, escala y enfoque. El
objetivo consiste en determinar en cada instante si el blister que está siendo
analizado se encuentra incompleto, en cuyo caso la región correspondiente a
la pı́ldora faltante presenta una intensidad similar al fondo. Escriba una fun-
ción que reciba como parámetro la imagen del blister a analizar y devuelva
un mensaje indicando si el mismo contiene o no la totalidad de las pı́ldo-
ras. En caso de estar incompleto, indique la posición (x,y) de las pı́ldoras
faltantes. Verifique el funcionamiento con las imágenes blister completo.jpg y
blister incompleto.jpg.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#import math


'''
    Obter as imagens. Retorna Blister Completo, Blister Incompleto.
'''
def ler_imgs():
    img1 = cv.imread("../imgs/blister_completo.jpg",0)
    img2 = cv.imread("../imgs/blister_incompleto.jpg",0)
   #img2 = cv.imread("../imgs/blister_incompleto2.jpg",0)
   #img2 = cv.imread("../imgs/blister_incompleto3.jpg",0)
    return img1, img2 


'''
    Analisar o Blister. Binariza as imagens, obtém o perfil de intensidade
(linhas 52 e 99, definidas empiricamente) e executa uma operação de XOR para
obter as pílulas faltantes. Ao se retornar um perfil inteiro de zeros (preto),
indica que o blister está cheio.
'''
# torna a imagem binaria
def img_bin (img):
    ret, img_b = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
    return img_b


# aplica a máscara XOR bit a bit
def app_mask(img, mask):
    img_x = cv.bitwise_xor(img, mask)    
    return img_x


# retorna um vetor de perfil de intensidade da linha especificada
def vet_int(img, lin):
    [altura, largura] = img.shape
    vpi = np.zeros(largura, dtype = np.uint8)
    vpi = img[lin, 0:largura]
    return vpi


# calcula os pontos médios conforme a sequência do vetor de perfil de
# intensidade obtido.
def pto_med(vpi):
    #conta brancos
    n_br = np.count_nonzero(vpi == 255)
    #lista de coordenadas
    coord = []
    #lista de pontos médios
    ptos = []
    #flag para saber se é pílula ou fundo
    in_pil = False
    
    #descobrir coordenadas de início e fim das pílulas que faltam 
    if n_br > 0: 
        for x in range(len(vpi)):
            if vpi[x] == 255 and not in_pil:
                in_pil = True
                coord.append(x)
            elif vpi[x] == 0 and in_pil:
                in_pil = False
                coord.append(x-1)
    else:
        return [-1] 

    #calcular o ponto médio entre as coordenadas obtidas
    for x in range(0,len(coord),2):
        ptos.append(int((coord[x] + coord[x+1])/2))

    #retornar "centros" dos comprimidos
    return ptos


# verifica se o blister está completo ou incompleto
def verifica_blister(img, mask):
    img_b  = img_bin(img)
    vpi_m1 = vet_int(mask, 52)
    vpi_m2 = vet_int(mask, 99)
    vpi1   = vet_int(img_b, 52)
    vpi2   = vet_int(img_b, 99)
    v_xor1 = app_mask(vpi1, vpi_m1)
    v_xor2 = app_mask(vpi2, vpi_m2)

    # coordenada de "centro" das pílulas faltantes
    coord = []
    
    pto_med1 = pto_med(v_xor1)
    pto_med2 = pto_med(v_xor2)
    coord_y1 = [52  for x in pto_med1]
    coord_y2 = [100 for x in pto_med2]
    
    #coordenadas x, y
    for x in range(len(pto_med1)):
        coord.append((pto_med1[x],coord_y1[x]))

    for x in range(len(pto_med2)):
        coord.append((pto_med2[x],coord_y2[x]))

    return coord

'''
    Main
'''
def main():
    # blister completo, blister incompleto
    img_bc, img_bi = ler_imgs()
    #img_bc tem uma coluna a mais que img_bi
    #tratamento
    img_bc = np.delete(img_bc, img_bc.shape[1] - 1, axis=1)
    mask = img_bin(img_bc)

    coord = verifica_blister(img_bi, mask)
    
    for x in range(len(coord)):
        if coord[x][0] > -1: 
            print ("Coordenadas de centro do blister faltante: ", coord[x])
    
        
    #mostrar imagem colorida    
    img_cor = cv.merge((img_bi, img_bi, img_bi))
    #desenhar círculo ao redor do comprimido que falta
    for x in range(len(coord)):
        if coord[x][0] > -1:
            cv.circle(img_cor, coord[x], 15, (0, 0, 255), 1) 
    
    while True:
        cv.imshow("Blister", img_cor)
        key = cv.waitKey(1) & 0xFF
        # pressionar q para sair
        if key == ord("q"):
            break

    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
 
