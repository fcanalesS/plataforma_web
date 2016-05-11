import sys
from mpi4py import MPI
import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def espejar(img):
    mirror = cv2.flip(img, 1)

    return mirror

image_path = os.getcwd() + '/images/'
img = cv2.imread(image_path + '001.jpg', cv2.IMREAD_COLOR)
alt, ancho, canales = img.shape

if alt < size:
    print "Imagen muy pequena"
else:
    region = img[(alt / size) * rank:(alt / size) * (rank + 1), 0:ancho]
    regionEditada = espejar(region)
    cv2.imwrite(image_path + "regionEditada2_" + str(rank) + ".jpg", regionEditada)