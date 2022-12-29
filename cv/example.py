#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2


def io():
    img = cv2.imread("image.jpg")
    print(img.shape)
    cv2.imwrite("output.jpg", img)

  
def display():
    from matplotlib import pyplot as plt
    img = cv2.imread("image.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('My Image', img)  # 原始影像
    plt.imshow(img)
    plt.title('my picture')
    plt.show()


def morphology():
    img = cv2.imread("image.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    img = cv2.erode(img, kernel)   # 侵蝕
    img = cv2.dilate(img, kernel)  # 擴張

def morphology():
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)   # 開運算
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)  # 閉運算
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

#  Structural Analysis and Shape Descriptors
def contours():
    cv2.findContours(img)
    drawContours()
    moments()
    contourArea()
    arcLength()
    boundingRect()
    convexHull()
    fitEllipse()
