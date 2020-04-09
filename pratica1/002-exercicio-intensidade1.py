'''
Ejercicio 2: Información de intensidad.
1. Informe los valores de intensidad de puntos particulares de la imagen (opcional: determine la posición en base al click del mouse).
2. Obtenga y grafique los valores de intensidad (perfil de intensidad ) sobre una determinada fila o columna.
3. Grafique el perfil de intensidad para un segmento de interés cualquiera.
'''

import cv2 as cv
import math
import numpy as np
import argparse

# parametros
ap = argparse.ArgumentParser()
ap.add_argument("-img", "--imagem", required=True, help="Caminho da imagem")
args = vars(ap.parse_args())

# lendo imagens ; 0 p/ ler em escala de cinzas
img = cv.imread(args["imagem"],0);

#dimensões e tipo de dados
print("Dimensões: ", img.shape)
print("Tipo de Dados: ", img.dtype)


# callback mouse - coordenadas
def click(event, x, y, flags, param):
    global coord;
    
    #guarda localização click
    if event == cv.EVENT_LBUTTONDOWN:
        coord = (x, y)
        pxl = img[coord[1],coord[0]]
        print(pxl)

# janela e callback mouse
str_win="Perfis de Intensidade em um Ponto"
cv.namedWindow(str_win)
cv.setMouseCallback(str_win, click)


while True:
    # muestra la imagen y espera una tecla
    cv.imshow(str_win, img)
    key = cv.waitKey(1) & 0xFF
    
    #sair == pressionando q
    if key == ord("q"):
        break


