import sys
from mpi4py import MPI
import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def blur(img):
    output = cv2.blur(img, (int(sys.argv[1]), int(sys.argv[1])))
    return output

image_path = os.getcwd() + '/images/'
img = cv2.imread(image_path + '001.jpg', cv2.IMREAD_COLOR)
alt, ancho, canales = img.shape

if alt < size:
    print "Imagen muy pequena"
else:
    regionEditada = blur(img)
    cv2.imwrite(image_path + "regionEditada2_.jpg", regionEditada)