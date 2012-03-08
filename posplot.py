#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""posplot.py: Plots the particles colored according to their bin"""

__author__      = "Mossa Merhi"
__email__       = "cgmossa@gmail.com"
__version__     = "0.5"

import time
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D
from bins import *

if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__))
    dataFile = path + '/test/data.e2.12.txt' # Default test file

    if len(sys.argv) > 1:
        dataFile = sys.argv[1]

    data = np.loadtxt(dataFile)
    N = data.shape[0]
    
    nBins = 5
    useCM = False

    plt.close('all')
    
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    binnedIndices, distances = binnedIndicesAndDistances(data, nBins = nBins, useCM = useCM)
    
    for particleIndices in binnedIndices:
        color = colors.rgb2hex(np.random.rand(3))
        pos = data[particleIndices][:, 0:3]
        ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=color)
        ## ----------------------------------------------------------------
        ## Skal nedenstående bruges?
        ## ----------------------------------------------------------------
        ##
        #absLogPos = np.log(np.abs(pos[:, 0:3]))
        #ax.scatter(absLogPos[:, 0], absLogPos[:, 1], absLogPos[:, 2], c=color)
    
    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10, 10)
    ax.set_zlim3d(-10, 10)
    plt.show()