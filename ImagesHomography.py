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

    frame_path = input("Enter full path, frame image name along with extension, e.g, C://Pictures/Frame.png :")
    picture_path = input("Enter full path, picture name along with extension, e.g, C://Pictures/Picture.png :")

    if not frame_path or not picture_path:
        print('Images not provided')
        return

    try:
        im1, im2 = cv2.imread(str(frame_path)), cv2.imread(str(picture_path))
    except Exception as e:
        print('Could not resolve images')

    size_x, size_y = len(im2), len(im2[0])

    print('Now Enter Space-Separated Coordinates for Frame Image with')
    print('(x1, y1)--------(x2, y2)')
    print('   |                |')
    print('   |                |')
    print('(x3, y3)--------(x4, y4)')
    print('In the form: x1 y1 x2 y2 x3 y3 x4 y4')

    coordinates = input()
    if len(coordinates.split()) != 8:
        return
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, coordinates.split())

    print('Have patience!')

    x11, y11 = 0, 0  # top left
    x12, y12 = size_y, 0  # top right
    x13, y13 = 0, size_x  # bottom left
    x14, y14 = size_y, size_x  # bottom right

    frame = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    image = np.array([[x11, y11], [x12, y12], [x13, y13], [x14, y14]])
    h = calculate_homography(image, frame)

    for i in range(size_y):
        for j in range(size_x):
            P = np.matmul(h, np.array([i, j, 1]))
            x, y, z = P[0], P[1], P[2]
            x = int(x/z)
            y = int(y/z)
            im1[y][x] = im2[j][i]

    cv2.imshow('image', im1)
    cv2.waitKey(0)
    cv2.imwrite('Image1.jpg', im1)
    print('Image ready!')


main()
