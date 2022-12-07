import numpy as np
import matplotlib.pyplot as plt
import skimage

def minima_regionaux(img):
    img_bin = np.ones(img.shape, dtype=np.uint8)
    img_padded = np.pad(img, 1, mode='constant', constant_values=1)
    fifo = []
    for p in np.ndindex(img.shape):
        if img_bin[p] == 1:
            for q in voisins(p):
                if img_padded[q] < img_padded[p]:
                    img_bin[p] = 0
                    fifo.append(p)
                    while not len(fifo):
                        p = fifo.pop()
                        for q in voisins(p):
                            if img_bin[q] == 1 and img_padded[q] >= img_padded[p]:
                                img_bin[q] = 0
                                fifo.append(q)
    return img_bin

def maxima_regionaux(img):
    img_bin = np.ones(img.shape, dtype=np.uint8)
    img_padded = np.pad(img, 1, mode='constant', constant_values=1)
    fifo = []
    for p in np.ndindex(img.shape):
        if img_bin[p] == 1:
            for q in voisins(p):
                if img_padded[q] > img_padded[p]:
                    img_bin[p] = 0
                    fifo.append(p)
                    while not fifo:
                        p = fifo.pop()
                        for q in voisins(p):
                            if img_bin[q] == 1 and img_padded[q] <= img_padded[p]:
                                img_bin[q] = 0
                                fifo.append(q)
    return img_bin

def voisins(p,voisinage=3,connexite=8):
    offset = voisinage//2
    liste = []
    for i in range(-offset, offset+1):
        for j in range(-offset, offset+1):
            if connexite == 8 and i != 0 and j != 0:
                liste.append((p[0]+i, p[1]+j))
            elif connexite == 4 and (i == 0 and j != 0 or j == 0 and i != 0):
                liste.append((p[0]+i, p[1]+j))
    print("p = ",p,"\nliste = ",liste,"\n")
    return liste

def display(img):
    fig,ax = plt.subplots(3, 3, figsize=(10, 10))
    minima = minima_regionaux(img)
    maxima = maxima_regionaux(img)
    skimage_minima = skimage.morphology.extrema.local_minima(img)
    skimage_maxima = skimage.morphology.extrema.local_maxima(img)
    # fig.set_facecolor('gray')
    ax[0, 1].imshow(img, cmap='gray')
    ax[0, 1].set_title('Image de base')

    ax[1, 0].imshow(minima, cmap='gray')
    ax[1, 0].set_title('Minima régionaux')
    ax[1, 2].imshow(skimage_minima, cmap='gray')
    ax[1, 2].set_title('Skimage minima régionaux')
    
    ax[2, 0].imshow(maxima, cmap='gray')
    ax[2, 0].set_title('Maxima régionaux')
    ax[2, 2].imshow(skimage_maxima, cmap='gray')
    ax[2, 2].set_title('Skimage maxima régionaux')

    ax[1,1].imshow(np.subtract(skimage_minima, minima), cmap='gray')
    ax[2,1].imshow(np.subtract(skimage_maxima, maxima), cmap='gray')
    for i,j in np.ndindex(ax.shape):
        ax[i, j].axis('off')
    fig.tight_layout()
    plt.show()

display(np.array([[0,0,0,1,0,0,0],
                    [0,0,0,1,0,0,0],
                    [0,0,0,1,0,0,0],
                    [1,1,1,1,1,1,1],
                    [0,0,0,1,0,0,0]], dtype=np.uint8))