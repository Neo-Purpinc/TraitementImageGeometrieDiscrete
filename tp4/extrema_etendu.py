import numpy as np
import matplotlib.pyplot as plt
import skimage

def hminima(img,depth):
    return img

def hmaxima(img,height):
    return img

def display():
    img = skimage.data.camera()
    thresh = 10
    fig,ax = plt.subplots(3, 3, figsize=(10, 10))
    skimage_hmin = skimage.morphology.h_minima(img, thresh)
    skimage_hmax = skimage.morphology.h_maxima(img, thresh)
    hmin = hminima(img, thresh)
    hmax = hmaxima(img, thresh)

    ax[0, 1].imshow(img, cmap='gray')
    ax[0, 1].set_title('Image de base')

    ax[1, 0].imshow(hmin, cmap='gray')
    ax[1, 0].set_title('H-minima')

    ax[2, 0].imshow(hmax, cmap='gray')
    ax[2, 0].set_title('H-maxima')

    ax[1, 2].imshow(skimage_hmin, cmap='gray')
    ax[1, 2].set_title('H-minima skimage')

    ax[2, 2].imshow(skimage_hmax, cmap='gray')
    ax[2, 2].set_title('H-maxima skimage')

    for i in range(3):
        for j in range(3):
            ax[i, j].axis('off')
    plt.tight_layout()
    plt.show()

display()