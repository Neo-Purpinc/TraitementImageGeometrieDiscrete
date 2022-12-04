import numpy as np
import matplotlib.pyplot as plt
import skimage

def reconstruction_geodesique(marker,mask,method='dilation',footprint=None):
    # scan mask in raster order and let p be the current pixel
    kernel = np.ones(shape=(2 + 1,) * 2, dtype=np.uint8)
    while True:
        expanded = skimage.morphology.dilation(marker, kernel)
        np.bitwise_and(expanded, mask, out=expanded)

        # Termination criterion: Expansion didn't change the image at all
        if (marker == expanded).all():
            return expanded
        marker = expanded