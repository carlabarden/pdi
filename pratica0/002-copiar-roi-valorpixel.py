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
#imgn = np.zeros_like(img)

#carregar imagem em tons de cinza
#img_cinza = cv2.imread("../imgs/chairs.jpg",cv2.IMREAD_GRAYSCALE)

#gerar uma imagem em cinza a partir de um BGR ERRO
#img_cinza = cv2.imread("../imgs/snowman.png", cv2.IMREAD_BGR2GRAY)

#copiar imagens
#img2 = img.copy()

#ROI - Região de Interesse da imagem
#para copiar somente a ROI da imagem
#nesse caso, pontos aleatorios (400x400px, centro da imagem)

x0 = 330;
x1 = 630;
y0 = 490;
y1 = 790;


img2 = img[x0:x1,y0:y1].copy()


#ler e escrever um pixel
#valor_px: "uint8" p/ tons de cinza , 3 valores para imgs coloridas
valor_px = img2[86,13]
img2[219,198] = valor_px


#mostrar a imagem em uma janela, ate que se pressione uma tecla
cv2.imshow("Hello World ", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

