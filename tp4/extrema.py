import numpy as np
import matplotlib.pyplot as plt
import skimage

def minima_regionaux(img):
    return np.logical_and(img, np.logical_not(skimage.morphology.local_maxima(img)))

def maxima_regionaux(img):
    # create a binary image with the same shape as img and fill it with 1
    img_bin = np.ones(img.shape, dtype=np.uint8)
    fifo = []
    # for all points p in img, if img_bin[P] is 1 and there is a neighbor q of p such that img[q] > img[p], then set img_bin[p] to 0
    for p in np.ndindex(img.shape):
        if img_bin[p] == 1:
            for q in voisins(p, img.shape):
                if img[q] > img[p]:
                    img_bin[p] = 0
                    fifo.append(p)
                    while not fifo.empty():
                        p = fifo.pop()
                        for q in skimage.util.neighbors(img, p):
                            if img_bin[q] == 255 and img[q] < img[p]:
                                img_bin[q] = 0
                                fifo.append(q)
def display(img):
    fig,ax = plt.subplots(3, 3, figsize=(10, 10))
    # fig.set_facecolor('gray')
    
    ax[0, 1].imshow(img, cmap='gray')
    ax[0, 1].set_title('Image de base')

    ax[1, 0].imshow(minima_regionaux(img), cmap='gray')
    ax[1, 0].set_title('Minima régionaux')
    ax[1, 2].imshow(skimage.morphology.local_minima(img), cmap='gray')
    ax[1, 2].set_title('Skimage minima régionaux')

    ax[2, 0].imshow(maxima_regionaux(img), cmap='gray')
    ax[2, 0].set_title('Maxima régionaux')
    ax[2, 2].imshow(skimage.morphology.local_maxima(img), cmap='gray')
    ax[2, 2].set_title('Skimage maxima régionaux')
    for i,j in np.ndindex(ax.shape):
        ax[i, j].axis('off')
    for i in range(3):
        if not np.equal(ax[i, 0].get_images(), ax[i, 2].get_images()).all():
            ax[i,1].set_facecolor('red')
    fig.tight_layout()
    plt.show()

display(skimage.data.camera())