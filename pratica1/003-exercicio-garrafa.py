'''
Ejercicio 3: Aplicación
    Utilice las herramientas aprendidas en esta unidad para implementar un sistema que permita identificar una botella que no está correctamente llena. Las imágenes que se proporcionarán son capturadas con una cámara fija, en escala de grises y directamente de la lı́nea de envasado. Para implementar el sistema deberá bastarle una imagen de ejemplo “botella.tif” (que encontrará en el repositorio). Adicionalmente, se espera que el sistema pueda:
    >> identificar una botella no-llena en cualquier posición de la imagen.
    >> indicar la posición de la botella en la imagen (podrı́a ser con un recuadro,informando la posición relativa entre botellas, la posición absoluta en pixels, etc).
    >> informar el porcentaje de llenado de la botella no-llena.
'''
# coding:utf-8
import cv2 as cv
import math
import numpy as np
#from matplotlib import pyplot as plt

''' 
    A imagem encontra-se em escala de cinzas. Para encontrar as garrafas,
pode-se medir, através de um vetor de intensidade, com uma varredura
horizontal, grandes diferenças de intensidade (já que o fundo é preto e as
garrafas são cinzas-claras/brancas). Aqui, optou-se por realizar a varredura
horizontal na linha central da imagem, considerando que a câmera que captura
as imagens é fixa. Empiricamente, definiu-se que a intensidade do fundo é 
menor que 5 (quase preto). A intensidade que for maior que 5 será 
considerada garrafa.
''' 

# armazenar os pontos de início e fim de cada garrafa 
# bool in_garrafa: para armazenar somente os pontos de início e 
# fim de cada garrafa (e não todos os pontos do intervalo)
def encontrar_coord_garrafas(imagem):
    [altura,largura] = imagem.shape
    linha_centro = int(altura/2)
    
    coord_garrafas = []
    in_garrafa = False
    
    vpi_g = np.zeros(largura, dtype = np.uint8)
    vpi_g = imagem[linha_centro, 0:largura]  
    
    # inicializando in_garrafa corretamente
    if (vpi_g[0] > 5):
        in_garrafa = True
        coord_garrafas.append(0)
    else:
        in_garrafa = False
    
    for x in range(largura):
        if (vpi_g[x] > 5 and not in_garrafa):
            in_garrafa = True
            coord_garrafas.append(x)
        elif (vpi_g[x] <= 5 and in_garrafa):
            in_garrafa = False
            coord_garrafas.append(x - 1)
    
    # o tamanho de garrafas[] ser ímpar significa que a fotografia
    # "cortou" a garrafa final; tratamento:
    if (len(coord_garrafas) % 2 == 1):
        coord_garrafas.append(largura)
        
    return coord_garrafas


'''
    Aqui, encontra-se o ponto médio horizontal de cada garrafa, com base nos
pontos encontrados anteriormente. Servirão para definir a coluna em que se 
fará a varredura (vertical desta vez) - descobrindo-se, assim, o tamanho da
garrafa, o que é uma garrafa cheia, o que é uma garrafa não cheia, etc.
'''
def ponto_medio(coord_garrafas):
    pto_med = []
    
    for x in range(0,len(coord_garrafas),2):
        pto_med.append(int((coord_garrafas[x] + coord_garrafas[x+1])/2))
        
    return pto_med
    
    
'''
    Varredura "vertical" da garrafa propriamente dita. Valores usados
escolhidos de maneira empírica. Para conhecer o conteúdo da garrafa, aplica-se
uma transformação de intensidade - limiar (linear), gerando uma imagem 
binária,para facilitar a distinção entre garrafa cheia e vazia. A função
trabalhará com o perfil de intensidade transformado (vpi_t), já que há dois
pixeis brancos ao fim da imagem, depois da transformação (condizendo com o
fim da garrafa). Retorna as coordenadas onde começam e terminam os "brancos"
do vetor.
''' 
# bool in_garrafa: para armazenar somente os pontos de início e 
# fim de cada garrafa (e não todos os pontos do intervalo)
def coord_nivel_garrafa(ponto, imagem):
    [altura,largura] = imagem.shape
     
    in_garrafa = False
    
    #transformar imagem em imagem binária
    ret,timg = cv.threshold(imagem,200,255,cv.THRESH_BINARY)
    # perfis de intensidade da imagem transformada - vetor
    vpi_t = np.zeros(altura, dtype = np.uint8)
    # varredura 'vertical' da imagem transformada
    vpi_t = timg[0:altura, ponto]

    # processando imagem transformada para descobrir o quanto de cada 
    # garrafa está "vazio" (branco)
    coord_branco = []
    # inicializando in_garrafa corretamente
    if (vpi_t[0] == 255):
        in_garrafa = True
        coord_branco.append(0)
    else:
        in_garrafa = False
    
    for x in range(altura):
        if (vpi_t[x] == 255 and not in_garrafa):
            in_garrafa = True
            coord_branco.append(x)
        elif (vpi_t[x] == 0 and in_garrafa):
            in_garrafa = False
            coord_branco.append(x - 1)
            
    #cv.imshow("imgt", timg)
    return coord_branco   


'''
    Conhecendo as coordenadas "brancas", é possível calcular se a garrafa
está cheia ou não (em relação a ela mesma - nenhuma garrafa estará 100%
cheia):
'''
def conteudo_garrafas (ponto_medio, imagem):
    [altura, largura] = imagem.shape
    # coordenadas
    coord = []
    for x in range(len(ponto_medio)):
        coord.append(coord_nivel_garrafa(ponto_medio[x], imagem))
        
    # porcentagens de cada garrafa
    conteudo_percentual = []
    # % = parte/todo * 100
    for x in range(len(coord)):
        # considerando a câmera fixa na vertical, a base da garrafa 
        # está na última linha da imagem, ou seja, sua altura
        # coord[x][0] == início da garrafa (tampa)
        todo  = altura - coord[x][0] 
        parte = coord[x][1] - coord[x][0]
        conteudo_percentual.append(round(100 - (parte/todo*100),2))
        
    return conteudo_percentual
    

'''
    Define os pontos onde os retângulos deverão ser desenhados -
a correspondência entre as listas é feita pelo índice.
'''
#def pontos_retangulos(im, garrafas, pto_medio, altura):
def pontos_retangulos(imagem):
    [alt, larg] = imagem.shape
    coord_garrafas_h = encontrar_coord_garrafas(imagem)
    pto_med  = ponto_medio(coord_garrafas_h)
    
    # definindo pontos do quadro    
    # obtendo a altura das garrafas
    # obtendo a altura das tampas
    tampas = []
    for x in range(len(pto_med)):    
        tampas.append(coord_nivel_garrafa(pto_med[x], imagem))
    
    # altura total
    altura = []
    for x in range(len(tampas)):
        altura.append([tampas[x][0],alt])
    
    # obtendo a largura das garrafas
    largura = []
    for x in range(0, len(coord_garrafas_h), 2):
        largura.append([coord_garrafas_h[x], coord_garrafas_h[x+1]])
         
    # obtendo coordenadas
    pontos = [] #altura x largura
    for x in range(len(largura)):
        pontos.append( [(largura[x][0],altura[x][0]),\
                        (largura[x][1],altura[x][1])])
            
    return pontos
    

'''
    Desenhar quadro em torno das garrafas. 
'''
def moldura (img, pontos, cor):
    if (cor == 1):        
        cv.rectangle(img, pontos[0], pontos[1], (0, 255, 0), 1)
    else:
        cv.rectangle(img, pontos[0], pontos[1], (0, 0, 255), 1)
        
'''
    Main
'''
def main():

    #ler
    img = cv.imread("../imgs/botellas.tif",0);
    #img = cv.imread("../imgs/botellas2.tif",0);
    #img = cv.imread("../imgs/botellas3.tif",0);
    #img = cv.imread("../imgs/botellas4.tif",0);
    #img = cv.imread("../imgs/botellas5.tif",0);
    #img = cv.imread("../imgs/botellas6.tif",0);
    #img = cv.imread("../imgs/botellas7.tif",0);

    #imagem com 3 canais de cor, para molduras coloridas
    imgc = cv.merge((img,img,img))

    coord_garrafas = encontrar_coord_garrafas(img)
    pto_med = ponto_medio(coord_garrafas)
    
    #para desenhar moldura
    pts = pontos_retangulos(img)
    
    #para efeitos práticos, foram consideradas cheias garrafas 
    #com mais de 80% do conteúdo
    percentual = conteudo_garrafas(pto_med, img)
    
    #desenhar
    for x in range(len(pts)):
        coord = pts[x]
        if (percentual[x] >= 80.00):
            moldura(imgc, coord, 1)
        else:
            moldura(imgc, coord, 0)
        
    #informações
    print("")
    print("Quantidade de garrafas: ",len(percentual))
    print(" ")
    #posição aproximada para um retângulo
    print("Posições das garrafas: ")
    print(pts)
    print(" ")
    print("% ocupadas: ")
    print(percentual)
    print(" ")
          
    while True:
        cv.imshow("Garrafas",imgc)
        key = cv.waitKey(1) & 0xFF
        #sair == pressionando q
        if key == ord("q"):
            break
    
    
if __name__ == '__main__':
    main()

