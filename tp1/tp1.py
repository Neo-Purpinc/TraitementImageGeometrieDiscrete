import numpy as np
import matplotlib.pyplot as plt
import skimage

def carre(x:int):
    return np.ones((x, x))

def rectangle(x:int, y:int):
    return np.ones((x, y))

def erosion(img, struct):

def dilation(img, struct):

def ouverture(img, struct):

def fermeture(img, struct):

def afficher(img):
    plt.imshow(img, cmap='gray')
    plt.show()