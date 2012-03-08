#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""velocity.py: Takes particle data file, runs N-body simulation and then splits particles into bins and plots density"""

__author__      = "Mossa Merhi"
__email__       = "cgmossa@gmail.com"
__version__     = "0.6"

import time
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from bins import *

if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    dataFile = path + '/test/data.e2.12.txt' # Default test file

    if len(sys.argv) > 1:
        dataFile = sys.argv[1]

    data = np.loadtxt(dataFile)

    nBins = 5
    useCM = False
    noOfHistBins = 20

    plt.close('all')

    binnedIndices, distances = binnedIndicesAndDistances(data, nBins = nBins, useCM = useCM)

    binHistograms = []
    for i, particleIndices in enumerate(binnedIndices):
        ## ----------------------------------------------------------------
        ## Skal de nedenstående bin parametre bruges?
        ## ----------------------------------------------------------------
        ##
        #ssVelocity = np.sum(np.power(data[particleIndices][3:6], 2)) # Sum of particle velocities squared, in bin
        #sigmaSq = ssVelocity/particleIndices.shape[0]
        #
        #binRadius = np.sum(distances[particleIndices])/particleIndices.shape[0]
        #m = np.sum(data[particleIndices][:, 6]) # Total mass of particles in bin
        #rInner = distances[particleIndices[0]]
        #rOuter = distances[particleIndices[-1]]
        #V = 4.0/3.0*np.pi*(rOuter**3 - rInner**3)
        #binDensity = m/V

        # Plot histograms of velocity components
        fig, axs = plt.subplots(nrows=1, ncols=3)
        fig.suptitle('Histogram of velocity distributions in bin ' + str(i), fontsize=14, fontweight='bold', y = 0.95)

        for j, coordName in enumerate(['v_x', 'v_y', 'v_z']):
            axs[j].hist(data[particleIndices][:, 3 + j], noOfHistBins)
            axs[j].set_xlabel(coordName)
            axs[j].set_ylabel('f')
            axs[j].locator_params(nbins=5)

            ## Fit
            ## ----------------------------------------------------------------
            ## Vi skal fitte histogrammerne!
            ## ----------------------------------------------------------------

        plt.tight_layout()
        fig.subplots_adjust(top=0.90)
        # fig.savefig('%s/result/velocity-b%02d-hist.png' % (path, i))

    plt.show()