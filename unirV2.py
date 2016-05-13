import cv2, os
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print "COMM: ", comm
print "RANK: ", rank
print "SIZE: ", size

while rank <= size:
    print "HOLA"


img = cv2.imread('regionEditada2_0.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('regionEditada2_1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('regionEditada2_2.jpg', cv2.IMREAD_COLOR)
img3 = cv2.imread('regionEditada2_3.jpg', cv2.IMREAD_COLOR)

alt,ancho,canales = img.shape

# aux = np.vstack((img, img1, img2, img3))
aux = np.concatenate((img, img1, img2, img3), axis=0)

#cv2.namedWindow('res', cv2.WINDOW_KEEPRATIO)
#cv2.imshow('res', aux)

#cv2.waitKey(0)
#cv2.destroyAllWindows()









