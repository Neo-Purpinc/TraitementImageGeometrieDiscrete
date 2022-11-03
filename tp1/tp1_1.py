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

img_test = io.imread('./tp1/lines.png', as_gray=True)

# def debug():
#     Y = np.array([
#         [0,0,1,0,0],
#         [0,1,0,1,0],
#         [1,1,1,1,1],
#         [0,1,1,1,0],
#         [0,0,1,0,0]
#     ])
#     b3 = np.array([
#         [0,1,0],
#         [0,0,0],
#         [0,0,1]
#     ])
#     fig, ax = plt.subplots(2, 3, figsize=(10, 10))
#     ax[0, 0].imshow(1-Y, cmap='gray')
#     ax[0, 0].set_title('Y')
#     ax[0, 1].imshow(Y, cmap='gray')
#     ax[0, 1].set_title('opposé de Y')
#     ax[1, 0].imshow(1-dilatation(Y, b3), cmap='gray')
#     ax[1, 0].set_title('dilatation(-Y, b3)')
#     ax[1, 1].imshow(1-dilatation(1-Y, b3), cmap='gray')
#     ax[1, 1].set_title('dilatation(Y, b3)')    
#     ax[1, 2].imshow(dilatation(Y, b3), cmap='gray')
#     ax[1, 2].set_title('1-dilatation(1-Y, b3)')
#     ax[1, 2].imshow(dilatation(1-Y, b3), cmap='gray')
#     ax[1, 2].set_title('1-dilatation(Y, b3)')
#     ax[0, 2].imshow(1-erosion(Y, b3), cmap='gray')
#     ax[0, 2].set_title('erosion(1-Y, b3)')
#     for i in range(2):
#         for j in range(3):
#             ax[i, j].axis('off')
#     plt.show()

def printf():
    # Images binaires
    X = np.array([
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
    ])
    Y = np.array([
        [0,0,1,0,0],
        [0,1,0,1,0],
        [1,1,1,1,1],
        [0,1,1,1,0],
        [0,0,1,0,0]
    ])
    # Elements structurants
    b1 = np.array([
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ])
    b2 = np.array([
        [0,1,0],
        [1,1,0],
        [0,0,0]
    ])
    b3 = np.array([
        [0,1,0],
        [0,0,0],
        [0,0,1]
    ])
    fig,ax = plt.subplots(6,7)
    fig.set_size_inches(10, 6)
    fig.set_facecolor('gray')
    ax[0][1].imshow(1-X, cmap='gray')
    ax[0][1].set_title('X')
    ax[0][2].imshow(1-Y, cmap='gray')
    ax[0][2].set_title('Y')
    ax[0][3].imshow(1-b1, cmap='gray')
    ax[0][3].set_title('B1')
    ax[0][4].imshow(1-b2, cmap='gray')
    ax[0][4].set_title('B2')
    ax[0][5].imshow(1-b3, cmap='gray')
    ax[0][5].set_title('B3')
    ax[1][0].imshow(1-dilatation(X, b1), cmap='gray')
    ax[1][0].set_title('X \u2295 B1', fontsize=8)
    ax[1][1].imshow(1-dilatation(X, b2), cmap='gray')
    ax[1][1].set_title('X \u2295 B2', fontsize=8)
    ax[1][2].imshow(1-dilatation(X, b3), cmap='gray')
    ax[1][2].set_title('X \u2295 B3', fontsize=8)
    ax[1][4].imshow(1-morphology.dilation(X, b1), cmap='gray')
    ax[1][4].set_title('X \u2295 B1\nSkimage', fontsize=8)
    ax[1][5].imshow(1-morphology.dilation(X, b2), cmap='gray')
    ax[1][5].set_title('X \u2295 B2\nSkimage', fontsize=8)
    ax[1][6].imshow(1-morphology.dilation(X, b3), cmap='gray')
    ax[1][6].set_title('X \u2295 B3\nSkimage', fontsize=8)
    ax[2][0].imshow(1-erosion(Y, b1), cmap='gray')
    ax[2][0].set_title('Y \u2296 B1', fontsize=8)
    ax[2][1].imshow(1-erosion(Y, b2), cmap='gray')
    ax[2][1].set_title('Y \u2296 B2', fontsize=8)
    ax[2][2].imshow(1-erosion(Y, b3), cmap='gray')
    ax[2][2].set_title('Y \u2296 B3', fontsize=8)
    ax[2][4].imshow(1-morphology.erosion(Y, b1), cmap='gray')
    ax[2][4].set_title('Y \u2296 B1\nSkimage', fontsize=8)
    ax[2][5].imshow(1-morphology.erosion(Y, b2), cmap='gray')
    ax[2][5].set_title('Y \u2296 B2\nSkimage', fontsize=8)
    ax[2][6].imshow(1-morphology.erosion(Y, b3), cmap='gray')
    ax[2][6].set_title('Y \u2296 B1\nSkimage', fontsize=8)
    ax[3][0].imshow(1-fermeture(Y, b1), cmap='gray')
    ax[3][0].set_title('Y \u2219 B1', fontsize=8)
    ax[3][1].imshow(1-fermeture(Y, b2), cmap='gray')
    ax[3][1].set_title('Y \u2219 B2', fontsize=8)
    ax[3][2].imshow(1-fermeture(Y, b3), cmap='gray')
    ax[3][2].set_title('Y \u2219 B3', fontsize=8)
    ax[3][4].imshow(1-morphology.closing(Y, b1), cmap='gray')
    ax[3][4].set_title('Y \u2219 B1\nSkimage', fontsize=8)
    ax[3][5].imshow(1-morphology.closing(Y, b2), cmap='gray')
    ax[3][5].set_title('Y \u2219 B2\nSkimage', fontsize=8)
    ax[3][6].imshow(1-morphology.closing(Y, b3), cmap='gray')
    ax[3][6].set_title('Y \u2219 B3\nSkimage', fontsize=8)
    ax[4][0].imshow(1-ouverture(Y, b1), cmap='gray')
    ax[4][0].set_title('Y \u2218 B1', fontsize=8)
    ax[4][1].imshow(1-ouverture(Y, b2), cmap='gray')
    ax[4][1].set_title('Y \u2218 B2', fontsize=8)
    ax[4][2].imshow(1-ouverture(Y, b3), cmap='gray')
    ax[4][2].set_title('Y \u2218 B3', fontsize=8)
    ax[4][4].imshow(1-morphology.opening(Y, b1), cmap='gray')
    ax[4][4].set_title('Y \u2218 B1\nSkimage', fontsize=8)
    ax[4][5].imshow(1-morphology.opening(Y, b2), cmap='gray')
    ax[4][5].set_title('Y \u2218 B2\nSkimage', fontsize=8)
    ax[4][6].imshow(1-morphology.opening(Y, b3), cmap='gray')
    ax[4][6].set_title('Y \u2218 B3\nSkimage', fontsize=8)
    ax[5][0].imshow(1-fermeture(X, b1), cmap='gray')
    ax[5][0].set_title('X \u2219 B1', fontsize=8)
    ax[5][1].imshow(1-fermeture(X, b2), cmap='gray')
    ax[5][1].set_title('X \u2219 B2', fontsize=8)
    ax[5][2].imshow(1-fermeture(X, b3), cmap='gray')
    ax[5][2].set_title('X \u2219 B3', fontsize=8)
    ax[5][4].imshow(1-morphology.closing(X, b1), cmap='gray')
    ax[5][4].set_title('X \u2219 B1\nSkimage', fontsize=8)
    ax[5][5].imshow(1-morphology.closing(X, b2), cmap='gray')
    ax[5][5].set_title('X \u2219 B2\nSkimage', fontsize=8)
    ax[5][6].imshow(1-morphology.closing(X, b3), cmap='gray')
    ax[5][6].set_title('X \u2219 B3\nSkimage', fontsize=8)
    for i in range(6):
        for j in range(7):
            ax[i][j].axis('off')
    fig.tight_layout()
    plt.show()
printf()
# debug()