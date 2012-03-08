#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""density.py: Takes end data file and plots bin radius vs density"""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi"]
__email__       = "toyorhan@gmail.com"
__version__     = "0.9"

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

from bruteforce import *
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
    
    binnedIndices, distances = binnedIndicesAndDistances(data, nBins = nBins, useCM = useCM)
    
    binRadius = np.array([])
    binDensity = np.array([])
    for particleIndices in binnedIndices:
        binRadius = np.append(binRadius, np.sum(distances[particleIndices])/particleIndices.shape[0])
        
        m = np.sum(data[particleIndices][:, 6]) # Total mass of particles in bin
        rInner = distances[particleIndices[0]]
        rOuter = distances[particleIndices[-1]]
        V = 4.0/3.0*np.pi*(rOuter**3 - rInner**3)
        binDensity = np.append(binDensity, m/V)

    plt.close('all')
    ax = plt.subplot(111)
    ax.set_xlabel('Bin radius')
    ax.set_ylabel('Density')
    ax.set_title('N-body simulation with ' + str(N) + ' particles')
    
    ax.loglog(binRadius, binDensity, 'bo:')
    
    ## Fit
    ## ----------------------------------------------------------------
    ## Nedenstående kode fitter ikke, men er bare det som Mossa skrev,
    ## da vi var hos Steen i onsdags d. 7. marts
    ## ----------------------------------------------------------------
    ##
    #rho_fig,rho_ax = plot_density(pos,bin_indices)
    #rho_0 = 1/(2 * np.pi)
    #r_s = 1
    #bin_distances = [r for r in map(lambda bin: bin_distance(pos,bin),bin_indices)]
    #
    #rho_function = lambda r: rho_0/((r/r_s)*(1 + r/r_s)**3 )
    #rho_ax.loglog(bin_distances,map(rho_function,bin_distances),'x')
    #rho_ax.set_xlim(0.01,100)
    #rho_fig.savefig("Tætheden som funktion af middel radius.png")
    
    plt.show()
