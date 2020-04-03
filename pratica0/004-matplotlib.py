#biblioteca
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

##### ERRO  #######
'''
#ler a img
img = cv.imread("../imgs/chairs.jpg")
# Las figuras se declaran como en Matlab
plt.figure()
# Para cargar una imagen en la figura
plt.imshow(img)
# Se pueden asignar falsos colores a imágenes de grises
plt.imshow(img, cmap= 'gray')
#Se pueden utilizar subfiguras con plt.subplot(num filas,num columnas,actual):
plt.subplot(1,3,1)
plt.imshow(img)
plt.subplot(1,3,2)
plt.imshow(img, cmap = 'gray')
plt.subplot(1,3,3)
plt.imshow(img)
plt.show()

'''
