# python 001-exercicio-ler-ver-esc.py -img1 ../imgs/imagen1.jpg -img2 ../imgs/imagen2.jpg -n asdf.jpg

'''
1. Realice la carga y visualización de diferentes imágenes.
2. Muestre en pantalla información sobre las imágenes.
3. Investigue los formatos la imagen y como leer y como escribir un valor puntual
de la imagen.
4. Utilice el pasaje por parámetros para especificar la imagen a cargar.
5. Defina y recorte una subimagen de una imagen (vea ROI, Region Of Interest).
6. Investigue y realice una función que le permita mostrar varias imágenes en
una sóla ventana.
7. Dibuje sobre la imagen lı́neas, cı́rculos y rectángulos (opcional: defina la posición en base al click del mouse).
'''
# o programa carregará duas imagens passadas por parâmetro e mostrará as 
# informações na linha de comando;
# definirá uma ROI com base no centro da imagem, para ter duas imagens do mesmo tamanho;
# mostrará as duas imagens, lado a lado, usando np.hstack;
# permitirá desenhar sobre as imagens;
# salvará as imagens ao fechar;
# formas
# #n = nenhuma, c = círculo, r = retangulo, l = linha

import cv2 as cv
import math
import numpy as np
import argparse

# parametros
ap = argparse.ArgumentParser()
ap.add_argument("-img1", "--imagem_um", required=True, help="Caminho da primeira imagem")
ap.add_argument("-img2", "--imagem_dois", required=True, help="Caminho da segunda imagem")
ap.add_argument("-n", "--nome", required=True, help="Nome da imagem a ser salva, no formato <nome.extensão>")
args = vars(ap.parse_args())

#nome imagem final
img_final = args["nome"]

# lendo imagens
img1 = cv.imread(args["imagem_um"]);
img2 = cv.imread(args["imagem_dois"]);

# mostrando info
print("Imagem 1 - Dimensões: ",img1.shape, "   Tipo de Dados:", img1.dtype)
print("Imagem 2 - Dimensões: ",img2.shape, "   Tipo de Dados:", img2.dtype)

# definindo ROI a partir do centro da imagem
# dimensão no opencv é altura x largura e num de bytes por pixel
tam_roi = 200
centro1 = (int(img1.shape[0]/2) , int(img1.shape[1]/2))
centro2 = (int(img2.shape[0]/2),  int(img2.shape[1]/2))

# ROI 
# pontos ax e ay  da img1
ax1 = centro1[1] - tam_roi
ay1 = centro1[0] - tam_roi
ax2 = centro2[1] + tam_roi
ay2 = centro2[0] + tam_roi

roi1 = img1[ax1:ax2,ay1:ay2].copy()

#pontos bx e by da img2
bx1 = centro1[1] - tam_roi
by1 = centro1[0] - tam_roi
bx2 = centro2[1] + tam_roi
by2 = centro2[0] + tam_roi

roi2 = img2[bx1:bx2,by1:by2].copy()

#imagem vazia
#numpy: np.zeros((alt,larg,canais), tipo_dados)
#dst = np.zeros(((tam_roi*2),(tam_roi*4),3), uint8)
# numpy: concatenar matrizes horizontalmente
dst = np.hstack((roi1, roi2))

#EU ODEIO MUITO VARIÁVEIS GLOBAIS
#coordenadas 
ref_pt = []
#n = nenhuma, c = círculo, r = retangulo, l = linha
forma = "n"  

def click(event, x, y, flags, param):
    global ref_pt, forma
    
    #guarda localização click
    if event == cv.EVENT_LBUTTONDOWN:
        ref_pt.append((x, y))
    # si se libera el botón, se guarda la localización (x,y)
    elif event == cv.EVENT_LBUTTONUP:
        ref_pt.append((x, y)) 
        
        if forma == "l" or forma == "c" or forma == "r":
            desenho(dst,str_win)
        else:
            forma = "n"
            ref_pt[:] = []
        
#para ter ctrl+z, é só salvar a img anterior e mandar mostrá-la ao comando?
#para desenhar a forma       
def desenho(img, win):
     global ref_pt, forma
     
     if forma == "l":
        linha(img, win)
     
     if forma == "r":
        retangulo(img, win)
        
     if forma == "c":
        circulo(img, win)
        
     forma = "n"
     ref_pt[:] = []
        
       
# funções de desenho...
def linha (img, win):
    global ref_pt
    cv.line(img, ref_pt[-2], ref_pt[-1], (255,0,0), 1)
    cv.imshow(win , img)
    
def retangulo (img, win):
    global ref_pt
    cv.rectangle(img, ref_pt[-2], ref_pt[-1], (0,255,0), 1)
    cv.imshow(win , img)

def circulo (img, win):
    global ref_pt
    #tupla grrr
    raio = abs(int(ref_pt[-1][0] - ref_pt[-2][0]))
    cv.circle(img, ref_pt[-2], raio, (0,0,255), 1)
    cv.imshow(win , img)    

# defino una ventana y le asigno el manejador de eventos
str_win="Desenho em Duas Imagens"
cv.namedWindow(str_win)
cv.setMouseCallback(str_win, click)

while True:
    # muestra la imagen y espera una tecla
    cv.imshow(str_win, dst)
    key = cv.waitKey(1) & 0xFF
    
    #n = nenhuma, c = círculo, r = retangulo, l = linha
    #forma = "n"    
    if key == ord("l"):
        forma = "l"
    if key == ord("c"):
        forma = "c"
    if key == ord("r"):
        forma = "r"
    if key == ord("n"):
        forma = "n"         
    # si la tecla c es presionada sale del while
    if key == ord("q"):
        cv.imwrite(img_final, dst);
        break




