'''
Mejore la función para trazar los perfiles de intensidad que realizó en guı́as
previas, para que en la misma gráfica
• se visualicen simultáneamente los perfiles de cada canal: R, G y B.
• se visualicen los perfiles de los canales H, S y V.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse


'''
    Argumentos
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagem", required=True, help="Imagem")


'''
    MAIN
'''
def main():
    args = vars(ap.parse_args())   
    img = cv.imread(args["imagem"])
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    [alt, larg, ch] = img.shape
    
    # Perfis de intensidade da linha central da imagem
    lin = alt // 2
    r = np.zeros(larg, dtype = np.uint8)
    r = img[lin, 0:larg, 2]
    g = np.zeros(larg, dtype = np.uint8)
    g = img[lin, 0:larg, 1]
    b = np.zeros(larg, dtype = np.uint8)
    b = img[lin, 0:larg, 0]
    
    h = np.zeros(larg, dtype = np.uint8)
    h = hsv[lin, 0:larg, 0]
    s = np.zeros(larg, dtype = np.uint8)
    s = hsv[lin, 0:larg, 1]
    v = np.zeros(larg, dtype = np.uint8)
    v = hsv[lin, 0:larg, 2]
    

    # Mostrar
    x = range(256)
    
    plt.subplot(1,3,1)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.imshow(img[:,:,::-1])

    plt.subplot(1,3,2)
    plt.title("RGB")
    plt.plot(r, color="red", ls="--")
    plt.plot(g, color="green", ls="--")
    plt.plot(b, color="blue", ls="--")

    plt.subplot(1,3,3)
    plt.title("HSV")
    plt.plot(h, color="red", ls="--")
    plt.plot(s, color="green", ls="--")
    plt.plot(v, color="blue", ls="--")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()


