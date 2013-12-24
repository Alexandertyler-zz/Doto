import pylab as pl
import numpy as np

n = 300                                     #number of sample data
x,y = np.random.rand(2,n)                   #generate random sample locations

pl.subplot(121)                             #sub-plot area 1 out of 2
pl.scatter(x,y,lw=0,c='k')                  #draw sample points
pl.axis('image')                            #necessary for correct aspect ratio

pl.subplot(122)                             #sub-plot area 2 out of 2

pl.hexbin(x,y,C=None,gridsize=15,bins=None,mincnt=1)        #hexbinning

pl.scatter(x,y,lw=0.5,c='k',edgecolor='w')  #overlaying the sample points
pl.axis('image')                            #necessary for correct aspect ratio

pl.show()                                   #to show the plot
