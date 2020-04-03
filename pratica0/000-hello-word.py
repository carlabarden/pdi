#biblioteca
import cv2

#ler a img
img = cv2.imread("../imgs/snowman.png")

#dimensões e tipo de dados
print("Dimensões: ", img.shape)
print("Tipo de Dados: ", img.dtype)

#mostrar a imagem em uma janela, até que se pressione uma tecla
cv2.imshow("Hello World ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


