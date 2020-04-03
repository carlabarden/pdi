#biblioteca
import cv2 as cv
import numpy as np

#ler a img
img1 = cv.imread("../imgs/imagen1.jpg")
img2 = cv.imread("../imgs/imagen2.jpg")
dst =  cv.addWeighted(img1, 0.5 , img2, 0.5 , 0.0)

#dst = np.zeros([480,640,4],dtype=np.uint8)
title_window = "Mixxxxtura"


#Interação com trackbars
# como usa valores naturales, ajusto la cantidad de valores a elegir
alpha_slider_max = 100
# se utilizan las 2 imágenes y se calculan los parámetros para combinarlas
def on_trackbar_alpha(val):
    global img1, img2, dst
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv.addWeighted(img1, alpha, img2, beta, 0.0)
    cv.imshow(title_window, dst)
    

cv.namedWindow(title_window)
cv.createTrackbar('Alpha', title_window, int(alpha_slider_max/2), alpha_slider_max, on_trackbar_alpha)


while True:
    cv.imshow(title_window, dst)
    key = cv.waitKey(1) & 0xFF
    # presione c para salir
    if key == ord("c"):
        break
