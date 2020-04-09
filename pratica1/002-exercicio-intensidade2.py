'''
Ejercicio 2: Información de intensidad
2. Obtenga y grafique los valores de intensidad (perfil de intensidad) sobre una determinada fila o columna.
3. Grafique el perfil de intensidad para un segmento de interés cualquiera.
'''
# 2 y 3

import cv2 as cv
import math
import numpy as np
from matplotlib import pyplot as plt
import argparse

# parametros
ap = argparse.ArgumentParser()
ap.add_argument("-img", "--imagem", required=True, help="Caminho da imagem")
args = vars(ap.parse_args())

# lendo imagens
img = cv.imread(args["imagem"],0);

#dimensões e tipo de dados
print("Dimensões: ", img.shape)
print("Tipo de Dados: ", img.dtype)

##shape: altura x largura
[altura, largura] = img.shape
linha_centro = int(altura/2)
#vetor para um perfil de intensidade de uma linha
#incializando 
vpi = np.zeros(largura, dtype = np.uint8)
#calculando (varredura linha)
vpi = img[linha_centro, 0:largura]
x = range(largura)
plt.plot(x, vpi)
plt.show()

while True:
    # mostra a img e espera uma tecla
    cv.imshow("Perfil de Intensidade", img)
    key = cv.waitKey(1) & 0xFF
    
    #sair == pressionando q
    if key == ord("q"):
        break


