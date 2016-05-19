import sys
from mpi4py import MPI
from time import time

import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def border(img):

    edges = cv2.Canny(img, int(sys.argv[1]), int(sys.argv[2]))

    return edges

image_path = os.getcwd() + '/images/'
img = cv2.imread(image_path + '001.jpg', cv2.IMREAD_COLOR)
alt, ancho, canales = img.shape

if alt < size:
    print "Imagen muy pequena"
else:
    start = time()
    regionEditada = border(img)
    cv2.imwrite(image_path + "regionBorder.jpg", regionEditada)
    elapsed = time() - start
    print "TIEMPO BORDER: ", elapsed