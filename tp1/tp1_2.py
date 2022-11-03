import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from skimage import (io, morphology)

def dilatation(img:np.ndarray, struct:np.ndarray):
    res = np.zeros(img.shape, dtype=np.uint8)
    padded = np.pad(img, tuple(item//2 for item in struct.shape), mode='constant', constant_values=0)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
                res[i, j] = np.max(padded[i:i+struct.shape[0], j:j+struct.shape[1]]*struct)
    return res

def test():
    struct = np.array([
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ])
    img_test = io.imread('./tp1/lines.png', as_gray=True)
    fig, ax = plt.subplots(1, 4, figsize=(10, 10))
    ax[0].imshow(img_test, cmap='gray')
    ax[0].set_title('Image de base (Grayscale)')
    #img_test to binary
    img_test = (img_test > 0.5).astype(np.uint8)
    
    res_scikit = np.copy(img_test)
    res = np.copy(img_test)
    for i in range(4):
        res = dilatation(res, struct)
        res_scikit = morphology.binary_dilation(res_scikit, struct)
    ax[2].imshow(res, cmap='gray')
    ax[2].set_title('Suppression des diagonales')
    ax[3].imshow(res_scikit, cmap='gray')
    ax[3].set_title('Version SCKIT')
    for i in range(4):
        ax[i].set_axis_off()
    plt.show()
test()