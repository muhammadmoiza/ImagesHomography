import matplotlib.pyplot as plt
import matplotlib.image as img
import time
import math
import numpy as np
import cv2


def calculate_homography(image, frame):
    x1, y1, x2, y2, x3, y3, x4, y4, x11, y11, x12, y12, x13, y13, x14, y14 = image[0][0], image[0][1], image[1][0], image[1][1], image[2][0], image[2][1], image[3][0], image[3][1], frame[0][0], frame[0][1], frame[1][0], frame[1][1], frame[2][0], frame[2][1], frame[3][0], frame[3][1]
    A = np.array([
        [-x1, -y1, -1, 0, 0, 0, x1*x11, y1*x11, x11],
        [0, 0, 0, -x1, -y1, -1, x1*y11, y1*y11, y11],
        [-x2, -y2, -1, 0, 0, 0, x2*x12, y2*x12, x12],
        [0, 0, 0, -x2, -y2, -1, x2*y12, y2*y12, y12],
        [-x3, -y3, -1, 0, 0, 0, x3*x13, y3*x13, x13],
        [0, 0, 0, -x3, -y3, -1, x3*y13, y3*y13, y13],
        [-x4, -y4, -1, 0, 0, 0, x4*x14, y4*x14, x14],
        [0, 0, 0, -x4, -y4, -1, x4*y14, y4*y14, y14],
        [0, 0, 0, 0, 0, 0, 0, 0, 1]
    ])

    b = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1])
    x = np.matmul(np.linalg.inv(A), b)
    x = np.reshape(np.asarray(x), (3, 3))
    return x


def main():

    im1 = cv2.imread('Frame.jpg')
    im2 = cv2.imread('Audrey.jpg')

    size_x, size_y = len(im2), len(im2[0])

    x1, y1 = 187, 153   # top left
    x2, y2 = 343, 175   # top right
    x3, y3 = 185, 461   # bottom left
    x4, y4 = 343, 432   # bottom right
    #x5, y5 = (x1 + x3) / 2, (y1 + y3) / 2   # top middle x6, y6 = (x2 + x4) / 2, (y2 + y4) / 2   # bottom middle x7, y7 = (x1 + x2) / 2, (y1 + y2) / 2   # left middle x8, y8 = (x3 + x4) / 2, (y3 + y4) / 2   # right middle

    # x = 508, y = 500 long pic
    x11, y11 = 0, 0  # top left
    x12, y12 = size_y, 0  # top right
    x13, y13 = 0, size_x  # bottom left
    x14, y14 = size_y, size_x  # bottom right
    #x15, y15 = (x11 + x13) / 2, (y11 + y13) / 2   # top middle x16, y16 = (x12 + x14) / 2, (y12 + y14) / 2   # bottom middle x17, y17 = (x11 + x12) / 2, (y11 + y12) / 2   # left middle x18, y18 = (x13 + x14) / 2, (y13 + y14) / 2   # right middle

    frame = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    image = np.array([[x11, y11], [x12, y12], [x13, y13], [x14, y14]])
    h = calculate_homography(image, frame)

    for i in range(size_y):
        for j in range(size_x):
            P = np.matmul(h, np.array([i, j, 1]))
            #print(P)
            x, y, z = P[0], P[1], P[2]
            x = int(x/z)
            y = int(y/z)
            im1[y][x] = im2[j][i]

    cv2.imshow('image', im1)
    cv2.waitKey(0)
    cv2.imwrite('Image1.jpg', im1)

main()
