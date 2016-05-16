import sys
from mpi4py import MPI
import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

image_path = os.getcwd() + '/images/'
img = cv2.imread(image_path + '001.jpg', cv2.IMREAD_COLOR)
alt, ancho, canales = img.shape

if alt < size:
    print "Imagen muy pequena"
else:
    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), float(sys.argv[1]), 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imwrite(image_path + "regionRotada.jpg", dst)
