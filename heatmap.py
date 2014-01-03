import pylab as pl
import matplotlib.pyplot as plt
import numpy as np

pl.rcParams['figure.figsize'] = 10, 10
im = plt.imread("dota_map.jpg") #get the image we are laying over
imgplot = plt.imshow(im, origin='upper')
plt.tick_params(
        bottom=0,
        top=0,
        left=0,
        right=0,
        labelbottom=0,
        labelleft=0)
plt.show()
