import sys
from mpi4py import MPI
from time import time

import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def convolucion(img):
    dst = cv2.GaussianBlur(img, (5, 5), 0)
    for i in xrange(1, 1000):  # Para aplicarl filtro n veces
        dst = cv2.GaussianBlur(dst, (5, 5), 0)

    return dst

image_path = os.getcwd() + '/images/'
img = cv2.imread(image_path + '001.jpg', cv2.IMREAD_COLOR)
alt, ancho, canales = img.shape

if alt < size:
    print "Imagen muy pequena"
else:
    start = time()
    regionEditada = convolucion(img)
    cv2.imwrite(image_path + "regionDisp.jpg", regionEditada)
    elapsed = time() - start

    print "TIEMPO DISPgaussian: ", elapsed