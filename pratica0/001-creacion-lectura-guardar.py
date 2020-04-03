#biblioteca
import cv2
import numpy as np

#ler a img
img = cv2.imread("../imgs/chairs.jpg")

#dimensoes e tipo de dados
print("Dimensoes: ", img.shape)
print("Tipo de Dados: ", img.dtype)

#criar imagem de zeros a partir de outra
#imgn = np.zeros(img.shape, img.dtype)
#ou
imgn = np.zeros_like(img)

#carregar imagem em tons de cinza
img_cinza = cv2.imread("../imgs/chairs.jpg",cv2.IMREAD_GRAYSCALE)

#gerar uma imagem em cinza a partir de um BGR ERRO
#img_cinza = cv2.imread("../imgs/snowman.png", cv2.IMREAD_BGR2GRAY)

#salvar a imagem
cv2.imwrite("../edt-imgs/chairs-gray.jpg", img_cinza);


#mostrar a imagem em uma janela, ate que se pressione uma tecla
cv2.imshow("Hello World ", img_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()

