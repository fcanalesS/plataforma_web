import cv2, os
import numpy as np

imagenes = []
img_t = []

for i in os.listdir(os.getcwd() + ' /images/'):
    if 'regionEditada' in i:
        imagenes.append(i)

imagenes.sort()

for i in imagenes:
    aux = cv2.imread(i, cv2.IMREAD_COLOR)
    img_t.append(aux)

tuple(img_t)

aux = np.vstack(img_t)

cv2.imwrite('ImagenLista.jpg' , aux)

# cv2.namedWindow('res', cv2.WINDOW_KEEPRATIO)
# cv2.imshow('res', aux)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
