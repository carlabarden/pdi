#biblioteca
import cv2
import numpy as np

#ler a img
img = cv2.imread("../imgs/chairs.jpg")

#dimensoes e tipo de dados
print("Dimensoes: ", img.shape)
print("Tipo de Dados: ", img.dtype)

x0 = 330;
x1 = 630;
y0 = 490;
y1 = 790;

#desenhando linha
#parm: img, pto inicial, pto final, cor - BGR, espessura, *tipo de linha)
cv2.line(img, (x0,y0), (x1,y1), (255,0,0), 3) 

#desenhando círculo
#parm img, pto centro, raio, cor, espessura, *tipo de linha)
cv2.circle(img,(430,680),50,(0,255,0), 2) 

#desenhando retângulo
#parm img, pto inicial, pto final, cor, espessura)
cv2.rectangle(img, (100,100), (200,200), (0,0,255), 3)

#mostrar a imagem em uma janela, ate que se pressione uma tecla
cv2.imshow("Hello World ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

