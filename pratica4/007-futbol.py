'''
Este proceso permite separar la imagen en regiones utilizando información del
color. En este ejercicio usted debe implementar la segmentación de imágenes
para los modelos de color RGB y HSV. En cada caso deberá determinar el 
subespacio a segmentar para generar una máscara, que luego utilizará para 
extraer sólo la información de interés de la imagen original.
En cuanto a la metodologı́a, le proponemos que utilice la imagen ‘futbol.jpg’ y
defina una ROI representativa del color a segmentar, luego
• para el modelo RGB: use la información para calcular el centro de la esfera
y su radio. Podrı́a reemplazar la fórmula de la esfera por la de una elipsoide.
• para el modelo HSV: Utilice las componentes H y S para determinar el
subespacio rectangular a segmentar.
Consejo: utilizar los histogramas puede ser una buena alternativa.
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt




def main():





if __name__ == "__main__":
    main()


