import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from skimage import (io, morphology)

def carre(x:int):
    return np.ones((x, x), dtype=np.uint8)

def rectangle(x:int, y:int):
    return np.ones((x, y), dtype=np.uint8)

def erosion(img:np.ndarray, struct:np.ndarray):
    return 1-dilatation(1-img, struct)

def dilatation(img:np.ndarray, struct:np.ndarray):
    res = np.zeros(img.shape, dtype=np.uint8)
    padded = np.pad(img, tuple(item//2 for item in struct.shape), mode='constant', constant_values=0)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
                res[i, j] = np.max(padded[i:i+struct.shape[0], j:j+struct.shape[1]]*struct)
    return res


def ouverture(img:np.ndarray, struct:np.ndarray):
    return dilatation(erosion(img, struct), struct)

def fermeture(img:np.ndarray, struct:np.ndarray):
    return erosion(dilatation(img, struct), struct)

def test():
    struct = np.array([
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1]
    ])
    struct = carre(5)
    img_test = io.imread('./tp1/lines.png', as_gray=True)
    fig, ax = plt.subplots(1, 3, figsize=(10, 10))
    ax[0].imshow(img_test, cmap='gray')
    ax[0].set_title('Image de base')
    for i in range(1):
        img_test = fermeture(img_test, struct)
    ax[1].imshow(img_test, cmap='gray')
    ax[1].set_title('Suppression des diagonales')
    ax[2].imshow(morphology.closing(img_test, struct), cmap='gray')
    ax[2].set_title('Version SCKIT')
    for i in range(3):
        ax[i].set_axis_off()
    plt.show()
test()