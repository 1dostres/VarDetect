import numpy as np
import cv2
import os
from os import listdir
import matplotlib.pyplot as plt



## Bucle para obtener posicion bolita en cada momento y devuelve lista con los valores y max frame
def posBolita(folder_dir, bolitaPath):
    valores = []
    maxAcLoc = 99999
    maxFrame = ""
    for images in os.listdir(folder_dir):
        
        if(images.endswith(".jpg")):

            imgDir = folder_dir+"/"+images
            img = cv2.imread(imgDir, 0)

            bolita = cv2.imread(bolitaPath, 0)
            h,w = bolita.shape

            method = cv2.TM_CCOEFF

            img2 = img.copy()
            result = cv2.matchTemplate(img2, bolita, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            valores.append(-max_loc[1])
            if maxAcLoc > max_loc[1]:
                maxAcLoc = max_loc[1]
                maxFrame = imgDir

            location =  max_loc
            bottom_right = (location[0] + w, location[1] + h)

    return valores, maxFrame



## Normalizar entre 0 y valor maximo:

def normVal(valores, maxBolita):
    valoresN = np.interp(valores, (min(valores), max(valores)), (0, maxBolita))
    plt.plot(range(len(valoresN)), valoresN)
    plt.show()