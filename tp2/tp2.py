import numpy as np
import matplotlib.pyplot as plt
from skimage import (io, morphology)

def hit_or_miss_transform(img:np.ndarray, struct1:np.ndarray, struct2:np.ndarray):
    return np.logical_and(morphology.erosion(img, struct1), morphology.erosion(1-img, struct2))

def white_tophat(img:np.ndarray, struct:np.ndarray):
    print(img - morphology.opening(img, struct))
    return img - morphology.opening(img, struct)

def black_tophat(img:np.ndarray, struct:np.ndarray):
    return morphology.closing(img, struct) - img   

def ouverture_annulaire(img:np.ndarray, diametre:int):
    return morphology.opening(img, morphology.disk(diametre))

def gradient_morphologique_interne(img:np.ndarray, struct:np.ndarray):
    return img - morphology.erosion(img, struct)   

def gradient_morphologique_externe(img:np.ndarray, struct:np.ndarray):
    return morphology.dilation(img, struct) - img

def debug():
    fig,ax = plt.subplots(7, 3, figsize=(10, 10))
    fig.set_facecolor('gray')
    img = io.imread('./tp2/amas.png', as_gray=True)
    # img = np.array([
    #     [0,0,0,0,1,0,0,0,1,1],
    #     [0,1,1,1,0,1,0,0,0,1],
    #     [0,1,0,1,0,1,0,0,0,1],
    #     [0,1,1,1,0,1,0,0,0,1],
    #     [0,0,0,0,1,0,0,0,1,1],
    #     [0,0,0,0,1,0,0,0,1,1],
    #     [0,1,0,0,1,0,0,0,1,1],
    #     [0,1,1,0,1,0,0,0,1,1],
    #     [0,1,1,1,1,0,0,0,1,1],
    #     [0,1,1,1,1,1,1,0,1,1],
    # ], dtype=np.uint8)
    # img = np.array([[2, 3, 3, 3, 2],
    #                 [3, 4, 5, 4, 3],
    #                 [3, 5, 9, 5, 3],
    #                 [3, 4, 5, 4, 3],
    #                 [2, 3, 3, 3, 2]], dtype=np.uint8)
    # add a white square
    ax[0, 1].imshow(img, cmap='gray')
    ax[0, 1].set_title('Image de base')

    ax[1, 0].imshow(hit_or_miss_transform(img, np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]), np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]])), cmap='gray')
    ax[1, 0].set_title('HMT')
    ax[1, 2].imshow(img, cmap='gray')
    ax[1, 2].set_title('Pas de fonction HMT dans skimage')

    ax[2, 0].imshow(white_tophat(img, morphology.square(3)), cmap='gray')
    ax[2, 0].set_title('White tophat')
    ax[2, 2].imshow(morphology.white_tophat(img, morphology.square(3)), cmap='gray')
    ax[2, 2].set_title('Skimage White tophat')

    ax[3, 0].imshow(black_tophat(img, np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]])), cmap='gray')
    ax[3, 0].set_title('Black tophat')
    ax[3, 2].imshow(morphology.black_tophat(img, np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]])), cmap='gray')
    ax[3, 2].set_title('Skimage Black tophat')

    ax[4, 0].imshow(ouverture_annulaire(img, 3), cmap='gray')
    ax[4, 0].set_title('Ouverture annulaire ')
    ax[4, 2].imshow(morphology.diameter_opening(img, 3), cmap='gray')
    ax[4, 2].set_title('Skimage Ouverture annulaire (TODO)')

    ax[5, 0].imshow(gradient_morphologique_interne(img, np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]])), cmap='gray')
    ax[5, 0].set_title('Gradient morphologique interne')
    ax[5, 2].imshow(morphology.erosion(img, np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]])), cmap='gray')
    ax[5, 2].set_title('Skimage Gradient morphologique interne (TODO)')

    ax[6, 0].imshow(gradient_morphologique_externe(img, np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]])), cmap='gray')
    ax[6, 0].set_title('Gradient morphologique externe')
    ax[6, 2].imshow(morphology.dilation(img, np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]])), cmap='gray')
    ax[6, 2].set_title('Skimage Gradient morphologique externe (TODO)')

    for i in range(1, 7):
        if not np.array_equal(ax[i, 0].get_images()[0].get_array(), ax[i, 2].get_images()[0].get_array()):
                # show plain red image
                ax[i, 1].imshow(np.array([[[1,0,0]]], dtype=np.uint8), cmap='Reds')
    for i,j in np.ndindex(ax.shape):
        ax[i, j].axis('off')
    fig.tight_layout()
    plt.show()

debug()