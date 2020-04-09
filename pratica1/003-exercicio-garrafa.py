'''
Ejercicio 3: Aplicación
    Utilice las herramientas aprendidas en esta unidad para implementar un sistema que permita identificar una botella que no está correctamente llena. Las imágenes que se proporcionarán son capturadas con una cámara fija, en escala de grises y directamente de la lı́nea de envasado. Para implementar el sistema deberá bastarle una imagen de ejemplo “botella.tif” (que encontrará en el repositorio). Adicionalmente, se espera que el sistema pueda:
    >> identificar una botella no-llena en cualquier posición de la imagen.
    >> indicar la posición de la botella en la imagen (podrı́a ser con un recuadro,informando la posición relativa entre botellas, la posición absoluta en pixels, etc).
    >> informar el porcentaje de llenado de la botella no-llena.
'''

import cv2 as cv
import math
import numpy as np
from matplotlib import pyplot as plt

'''
    A imagem encontra-se em escala de cinzas. Para encontrar as garrafas, pode-se medir, através de um vetor de intensidade, com uma varredura horizontal, 
grandes diferenças de intensidade (já que o fundo é preto e as garrafas são cinzas-claras/brancas). Aqui, optou-se por realizar a varredura horizontal
na linha central da imagem, considerando que a câmera que captura as imagens é fixa. Empiricamente, definiu-se que a intensidade do fundo é menor que 5
(preto). A intensidade que for maior que 5 será considerada garrafa.
'''

# armazenar os pontos de início e fim de cada garrafa 
# bool in_garrafa: para armazenar somente os pontos de início e fim de cada garrafa (e não todos os pontos do intervalo)
def encontrar_garrafas(imagem, largura, linha_centro):
    garrafas = []
    in_garrafa = False
    
    vpi_g = np.zeros(largura, dtype = np.uint8)
    vpi_g = imagem[linha_centro, 0:largura]  
    
    # inicializando in_garrafa corretamente
    if (vpi_g[0] > 5):
        in_garrafa = True
        garrafas.append(0)
    else:
        in_garrafa = False
    
    for x in range(largura):
        if (vpi_g[x] > 5 and not in_garrafa):
            in_garrafa = True
            garrafas.append(x)
        elif (vpi_g[x] <= 5 and in_garrafa):
            in_garrafa = False
            garrafas.append(x - 1)
    
    # o tamanho de garrafas[] ser ímpar significa que a fotografia "cortou" a garrafa; tratamento:
    if (len(garrafas) % 2 == 1):
        garrafas.append(largura)
        
    return garrafas


'''
   Aqui, encontra-se o ponto médio horizontal de cada garrafa, com base nos pontos encontrados anteriormente. Servirão para definir a coluna em que se fará a 
varredura (vertical desta vez) - descobrindo-se, assim, o tamanho da garrafa, o que é uma garrafa cheia, o que é uma garrafa não cheia, etc.      
'''
def ponto_medio(garrafas):
    pto_med = []
    
    for x in range(0,len(garrafas),2):
        pto_med.append(int((garrafas[x] + garrafas[x+1])/2))
        
    return pto_med
    
    
'''
    Varredura "vertical" da garrafa propriamente dita. Valores usados escolhidos de maneira empírica.
Para conhecer o conteúdo da garrafa, aplica-se aplicar uma transformação de intensidade - limiar (linear), gerando uma imagem binária,para facilitar a distinção
entre garrafa cheia e vazia. A função trabalhará com o perfil de intensidade transformado (vpi_t), já que há dois pixeis brancos ao fim da imagem, depois da
transformação (condizendo com o fim da garrafa). Retorna as coordenadas onde começam e terminam os "brancos" do vetor.
'''
# bool in_garrafa: para armazenar somente os pontos de início e fim de cada garrafa (e não todos os pontos do intervalo)
def vv_garrafa(pto, img, alt):
    in_garrafa = False
    
    # varredura 'vertical' da imagem transformada
    ret,timg = cv.threshold(img,200,255,cv.THRESH_BINARY)
    # perfis de intensidade da imagem transformada
    vpi_t = np.zeros(alt, dtype = np.uint8)
    vpi_t = timg[0:alt, pto]

    # processando imagem transformada para descobrir o quanto de cada garrafa está "vazio" (branco)
    branco = []
    # inicializando in_garrafa corretamente
    if (vpi_t[0] == 255):
        in_garrafa = True
        branco.append(0)
    else:
        in_garrafa = False
    
    for x in range(alt):
        if (vpi_t[x] == 255 and not in_garrafa):
            in_garrafa = True
            branco.append(x)
        elif (vpi_t[x] == 0 and in_garrafa):
            in_garrafa = False
            branco.append(x - 1)
            
    #cv.imshow("imgt", timg)
    return branco

        
'''
    Conhecendo as coordenadas "brancas", é possível calcular se a garrafa está cheia ou não (em relação a ela mesma - nenhuma garrafa estará 100% cheia):
'''
def conteudo_garrafas (pto_med, img, alt):
    # coordenadas
    coord = []
    for x in range(len(pto_med)):
        coord.append(vv_garrafa(pto_med[x], img, alt))
        
    # porcentagens
    conteudo_per = []
    # % = parte/todo * 100
    for x in range(len(coord)):
        todo  = coord[x][2] - coord[x][0]
        parte = coord[x][1] - coord[x][0]
        conteudo_per.append(round(100 - (parte/todo*100),2))
        
    return conteudo_per
 
   
'''
    Define os pontos onde os retângulos deverão ser desenhados - a correspondência entre as listas é feita pelo índice.
'''
def pontos_retangulos(im, garrafas, pto_medio, altura):
    # definindo pontos do quadro    
    # obtendo a altura das garrafas (a partir do centro) - usar alt[0]  e alt [2]:
    aux = []
    for x in range(len(pto_medio)):    
        aux.append(vv_garrafa(pto_medio[x], im, altura))
    alt = []
    for x in range(len(aux)):
        alt.append([aux[x][0],aux[x][2]])
    
    # obtendo a largura das garrafas
    larg = []
    for x in range(0, len(garrafas), 2):
        larg.append([garrafas[x], garrafas[x+1]])
         
    # obtendo coordenadas
    pts = [] #altura x largura
    for x in range(len(larg)):
        pts.append( [(larg[x][0],alt[x][0]), (larg[x][1],alt[x][1])] )
            
    return pts
    

'''
    Desenhar quadro em torno das garrafas.       
'''
def moldura (img, pontos, cor):        
        cv.rectangle(img, pontos[0], pontos[1], (0, 0, 0), 1)
        
        
       
def main():

    # ler
    img = cv.imread("../imgs/botellas.tif",0);
    
    # altura x largura
    [alt, larg] = img.shape
    # linha do centro
    lin_cen = int(alt/2)

    garrafas = encontrar_garrafas(img, larg, lin_cen)
    pto_med = ponto_medio(garrafas)
    
    pts = pontos_retangulos(img, garrafas, pto_med, alt)
    
    #para efeitos práticos, foram consideradas cheias garrafas com mais de 80% do conteúdo
    percentual = conteudo_garrafas(pto_med, img, alt)
    
    #desenhar
    for x in range(len(pts)):
        coord = pts[x]
        moldura(img, coord, 1)
        
    #informações
    print("Posições das garrafas: ")
    print(pts)
    print(" ")
    print("% ocupadas: ")
    print(percentual)
    print(" ")
          
    while True:
        cv.imshow("Garrafas",img)
        key = cv.waitKey(1) & 0xFF
        #sair == pressionando q
        if key == ord("q"):
            break
    
    
if __name__ == '__main__':
    main()


