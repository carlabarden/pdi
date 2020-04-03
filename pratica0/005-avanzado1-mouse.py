#biblioteca
import cv2 as cv
import numpy as np

#ler a img
img = cv.imread("../imgs/chairs.jpg")

#dimensoes e tipo de dados
print("Dimensoes: ", img.shape)
print("Tipo de Dados: ", img.dtype)


#ROI - Região de Interesse da imagem
#para copiar somente a ROI da imagem
#nesse caso, pontos aleatorios (400x400px, centro da imagem)

x0 = 330;
x1 = 630;
y0 = 490;
y1 = 790;


img2 = img[x0:x1,y0:y1].copy()

# Exemplo de uso dos eventos do mouse para desenhar uma linha
refPt = []
# Primero se define la función:
def click(event, x, y, flags, param):
    
    # si se presiona el botón izquierdo, se guarda la localización (x,y)
    if event == cv.EVENT_LBUTTONDOWN:
        refPt.append((x, y))
        print(refPt)
    # si se libera el botón, se guarda la localización (x,y)
    elif event == cv.EVENT_LBUTTONUP:
        refPt.append((x, y))
        print(refPt)
        # dibuja la linea entre los puntos
        cv.line(img2, refPt[0], refPt[1], (0, 255, 0), 5)
        cv.imshow(str_win, img2)
        refPt[:] = []
        
        
# defino una ventana y le asigno el manejador de eventos
str_win="Desenho"
cv.namedWindow(str_win)
cv.setMouseCallback(str_win, click)


while True:
    # muestra la imagen y espera una tecla
    cv.imshow(str_win, img2)
    key = cv.waitKey(1) & 0xFF
    # si la tecla c es presionada sale del while
    if key == ord("c"):
        break







