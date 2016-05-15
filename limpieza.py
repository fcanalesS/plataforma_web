# coding=utf-8
import cv2, os
import numpy as np

imagenes = []
img_t = []

for i in os.listdir(os.getcwd() + '/images/'):
    if 'regionEditada' in i:
        imagenes.append(i)

imagenes.sort()

for i in imagenes:
    print "IMAGENES", i
    aux = cv2.imread(os.getcwd() + '/images/' + i, cv2.IMREAD_COLOR)
    #print aux
    img_t.append(aux)

# print img_t
tuple(img_t)
#
# print img_t
#
aux = np.vstack(img_t)
#
cv2.imwrite(os.getcwd() + '/images/imagenLista.jpg', aux)

"""
Pendiente borrar las imágenes extra
"""
