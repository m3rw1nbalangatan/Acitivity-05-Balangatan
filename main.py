import cv2 as cv
import numpy as np


def start():
    readImage()


def readImage():

    img = cv.imread('nobita.jpg')

    st = img.shape

    if len(st) == 3:
        modifyPx(img)

    else:
        print("Image can't reload")


def modifyPx(img):
    x = int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Color attributes: "))

    cv.imshow("BEFORE ", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    px = img.item(x, y, z)
    print("IMAGE VALUE: ", x, y, z)
    print("PIXEL VALUE: ", px)

    img.itemset((x, y, z), 200)
    px = img.item(x, y, z)
    print("Modified Pixel Value: ", px)

    dimention(img)


def dimention(img):

    size = img.shape

    x = 1000
    y = 1000

    if size[0] > x and size [1] > y:
        print("Invalid image dimention!!!!!")

    else:
        imageType(img)


def imageType(img):
    dtype = img.dtype
    print("Image data type: ", dtype)

    imagesize(img)


def imagesize(img):

    requiredsize = 20000000
    size = img.size

    if size <= requiredsize:
        print("Image size validated!!!")
        cv.imshow("AFTER", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("Image size invalid!!!!")


start()
