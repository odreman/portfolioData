import matplotlib.pyplot as plt

from skimage import io

import warnings
warnings.filterwarnings("ignore")


def dibujar_img(img, size=(7,7)):
    fig = plt.figure(figsize=size)
    io.imshow(img)
    io.show()
    
def dibujar_imgs(left, right, size=(10,10)):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=size)
    ax[0].imshow(left)
    ax[1].imshow(right)
    io.show()

