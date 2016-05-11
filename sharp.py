import sys
from mpi4py import MPI
import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def sharp(img):
    kernel = np.zeros((int(sys.argv[1]), int(sys.argv[1])), np.float32)
    kernel[int(sys.argv[1]) - 1, int(sys.argv[1]) - 1] = 2.0

    # Create a box filter:
    boxFilter = np.ones((int(sys.argv[1]), int(sys.argv[1])), np.float32) / float(pow(int(sys.argv[1]), 2))

    # Subtract the two:
    kernel = kernel - boxFilter

    # Note that we are subject to overflow and underflow here...but I believe that
    # filter2D clips top and bottom ranges on the output, plus you'd need a
    # very bright or very dark pixel surrounded by the opposite type.

    custom = cv2.filter2D(img, -1, kernel)

    return custom

image_path = os.getcwd() + '/images/'
img = cv2.imread(image_path + '001.jpg', cv2.IMREAD_COLOR)
alt, ancho, canales = img.shape

if alt < size:
    print "Imagen muy pequena"
else:
    regionEditada = sharp(img)
    cv2.imwrite(image_path + "regionEditada2_.jpg", regionEditada)