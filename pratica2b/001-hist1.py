'''
1. Cargue y visualice la imágenes patron2.tif y patron.tif (a esta última 
utilı́cela a escala de grises).
>>>Reflexione acerca de que histograma espera obtener para cada una.
>>>Obtenga los histogramas y grafı́quelos.
histr = cv2.calcHist(images, channels, mask, histSize, ranges[,
hist[, accumulate]])
pyplot.plot(histr)
>>>Identifique la información suministrada y analı́cela en relación a su ex-
pectativa.
'''

#import math
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 


def ler_imgs():
    img1 = cv.imread("../imgs/patron.tif",0)
    img2 = cv.imread("../imgs/patron2.tif")
    return img1, img2


'''
    images : it is the source image of type uint8 or float32. it should be
given in square brackets, ie, "[img]".
    channels : it is also given in square brackets. It is the index of channel
for which we calculate histogram. For example, if input is grayscale image, 
its value is [0]. For color image, you can pass [0], [1] or [2] to calculate
histogram of blue, green or red channel respectively.
    mask : mask image. To find histogram of full image, it is given as "None".
But if you want to find histogram of particular region of image, you have to 
create a mask image for that and give it as mask. 
    histSize : this represents our BIN count. Need to be given in square 
brackets. For full scale, we pass [256].
    ranges : this is our RANGE. Normally, it is [0,256].
'''


'''
    MAIN
'''
def main():
    img1, img2 = ler_imgs()
    
    #numpy
    #hist,bins = np.histogram(img.ravel(),256,[0,256])
    #opencv
    hist1 = cv.calcHist([img1], [0], None, [256], [0, 256])
    hist2 = cv.calcHist([img2], [0], None, [256], [0, 256]) 

    #mostrar
    plt.subplot(1,4,1)
    plt.imshow(img1, cmap="gray")
    plt.title("Patron.tif")

    plt.subplot(1,4,2,)
    plt.imshow(img2)
    plt.title("Patron2.tif")
    
    #histograma 
    #plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
    plt.subplot(1,4,3)
    #valores discretos, mas gráfico contínuo
    plt.plot(hist1)
    plt.title("Hist-Patron")

    plt.subplot(1,4,4)
    plt.plot(hist2)
    plt.title("Hist-Patron2")
    
    '''
        plt.bar(edges[:-1], hist, width = 0.8, color='#0504aa')
        plt.xlim(min(edges), max(edges))
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value',fontsize=15)
        plt.ylabel('Frequency',fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.ylabel('Frequency',fontsize=15)
        plt.title('Document Image Histogram',fontsize=15)
        plt.show()
    '''
    plt.title("Patron 1 - Histograma")
    
    
     
    plt.show()      
    


if __name__ == '__main__':
    main() 


