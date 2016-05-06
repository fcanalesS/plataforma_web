import cv2
import numpy as np


def Enhanced(img):
    b, g, r = cv2.split(img)

    equb = cv2.equalizeHist(b)
    equg = cv2.equalizeHist(g)
    equr = cv2.equalizeHist(r)

    res_bgr = cv2.merge((equb, equg, equr))

    return res_bgr