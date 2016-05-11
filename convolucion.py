import sys
from mpi4py import MPI
import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def convolucion(img):
    kernel = np.ones((5, 5), np.float32) / 25  # Matriz de convolucion
    dst = cv2.filter2D(img, -1, kernel)

    return dst

image_path = os.getcwd() + '/images/'
img = cv2.imread(image_path + '001.jpg', cv2.IMREAD_COLOR)
alt, ancho, canales = img.shape

if alt < size:
    print "Imagen muy pequena"
else:
    regionEditada = convolucion(img)
    cv2.imwrite(image_path + "regionConvolucion.jpg", regionEditada)