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

camera = skimage.data.camera()
plt.figure(figsize=(10, 10))
plt.subplot(221)
plt.imshow(camera, cmap='gray')
plt.title('Image de base')
plt.subplot(222)

# x = np.linspace(0, 4 * np.pi)
# y_mask = np.cos(x)
# y_seed = y_mask.min() * np.ones_like(x)
# y_seed[0] = 0.5
# y_seed[-1] = 0
# y_rec = skimage.morphology.reconstruction(y_seed, y_mask)
# y, x = np.mgrid[:20:0.5, :20:0.5]
# bumps = np.sin(x) + np.sin(y)
# h = 0.3
# seed = bumps - h
# background = skimage.morphology.reconstruction(seed, bumps)
# hdome = bumps - background
# plt.figure(figsize=(10, 10))
# plt.subplot(221)
# plt.imshow(bumps, cmap='gray')
# plt.title('Image de base')
# plt.subplot(222)
# plt.imshow(seed, cmap='gray')
# plt.title('Seed')
# plt.subplot(223)
# plt.imshow(background, cmap='gray')
# plt.title('Background')
# plt.subplot(224)
# plt.imshow(hdome, cmap='gray')
# plt.title('H-dome')
# plt.tight_layout()
# plt.show()
