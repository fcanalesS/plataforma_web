from mpi4py import MPI
from time import time

import cv2, os
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

file_path = os.getcwd() + '/bulletTime/'
imgs = os.listdir(file_path)
imgs.sort()
img_list = [cv2.imread(file_path + fn) for fn in imgs]

start = time()
height, width, layers = img_list[0].shape

fourcc = cv2.VideoWriter_fourcc(*'MPEG')
video = cv2.VideoWriter(os.getcwd() + '/static/video/bulletTime.mp4', fourcc, 60, (width, height))

for i in img_list:
    video.write(i)

elapsed = time() - start

print "TIEMPO BULLET: ", elapsed


os.system('rm ' + file_path + '*.jpg')

