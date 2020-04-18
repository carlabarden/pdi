'''
2. A partir de un video (pedestrians.mp4) de una cámara de seguridad, debe
obtener solamente el fondo de la imagen. Incorpore un elemento TrackBar
que le permita ir eligiendo el número de frames a promediar para observar
los resultados instantáneamente.
import numpy as np
import cv2
'''

#import math
import cv2 as cv
import numpy as np
#from matplotlib import pyplot as plt 
import argparse

'''
   Argumentos
'''
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",  required=True, help="Video")


'''
    Retornar frames lidos em uma lista.
'''
def obter_frames(video):
        
    cap = cv.VideoCapture(video) 
    frames = [] 
 
    while(cap.isOpened()):
        ret, frm = cap.read()
        if ret == False:
            break

        frames.append(frm)
    
    cap.release()    
    return frames 


'''
    Soma de imagens. Todas as imagens tem o mesmo peso, conforme o número de
imagens selecionadas na trackbar.
'''
def soma(imagens, qtd_imgs):
    soma = imagens[0]

    for x in range(1, qtd_imgs, 1):
        beta  = 1/(x + 1)
        alpha = 1 - beta
        soma = cv.addWeighted(soma, alpha, imagens[x], beta, 0.0)

    return soma    

 
'''
    Callback trackbar - Faz nada. 
'''
def tkb(x):
    pass


'''
    MAIN
'''
def main():

    args = vars(ap.parse_args())
    imagens = obter_frames(args["video"])  
    nome_jan = "Soma de Imagens para Eliminar Ruido"
    tam = len(imagens)
    res = np.zeros_like(imagens[0])
    
    #opencv
    cv.namedWindow(nome_jan)
    cv.createTrackbar("qtd imgs",nome_jan, 1, tam, tkb)
    
    while(True):
        qtd_imgs = cv.getTrackbarPos("qtd imgs", nome_jan)
        
        if qtd_imgs == 0 or qtd_imgs == 1:
            cv.imshow(nome_jan, imagens[0])
        else:
            res = soma(imagens, qtd_imgs)    
            cv.imshow(nome_jan, res)

        #cv.imshow(nome_jan, res)   
        key = cv.waitKey(1) & 0xFF
        if key == ord("q"):
            break 
    
    cv.destroyAllWindows()         

if __name__ == '__main__':
    main() 


