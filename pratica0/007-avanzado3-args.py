#biblioteca
import cv2 as cv
import numpy as np
import argparse


# se crea el analizador de parámetros y se especifican
ap = argparse.ArgumentParser()
ap.add_argument("-img1", "--imagem_um", required=True, help="Caminho da primeira imagem")
ap.add_argument("-img2", "--imagem_dois", required=True, help="Caminho da segunda imagem")

args = vars(ap.parse_args())

#print(args)

# se recuperan los parámetros en variables o directamente se utilizan
# imagen 2 = cv2.imread(args[‘‘imagen color’’])
nombre_img1 = args["imagem_um"]
nombre_img2 = args["imagem_dois"]

#ler a img
img1 = cv.imread(nombre_img1)
img2 = cv.imread(nombre_img2)

#Interação com trackbars
#evitar erro
dst =  cv.addWeighted(img1, 0.5 , img2, 0.5 , 0.0)
title_window = "Mixxxxtura"
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
