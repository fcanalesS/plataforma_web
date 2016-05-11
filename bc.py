import sys
from mpi4py import MPI
import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def brilloContraste(img):
    img2hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img2hsv)

    s = cv2.multiply(s, np.array([float(sys.argv[1])]))
    v = cv2.multiply(v, np.array([float(sys.argv[2])]))

    res = cv2.merge((h, s, v))

    result = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)

    return result


image_path = os.getcwd() + '/images/'
img = cv2.imread(image_path + '001.jpg', cv2.IMREAD_COLOR)
alt, ancho, canales = img.shape

if alt < size:
    print "Imagen muy pequena"
else:
    region = img[(alt / size) * rank:(alt / size) * (rank + 1), 0:ancho]
    regionEditada = brilloContraste(region)
    cv2.imwrite(image_path + "regionEditada2_" + str(rank) + ".jpg", regionEditada)
