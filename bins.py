#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""bins.py: Bin particles in a fixed number of bins"""

__author__      = "Mossa Merhi"
__email__       = "cgmossa@gmail.com"
__version__     = "0.4"

import numpy as np

def binnedIndicesAndDistances(data, nBins = 5, useCM = False):
    N = data.shape[0]
    
    sortedIndices, distances = particleSortedIndicesAndDistances(data, useCM)
    return np.array_split(sortedIndices, nBins), distances

def particleSortedIndicesAndDistances(data, useCM = False):
    N = data.shape[0]
    
    center = np.zeros(3) # Origo is the default (bin) center
    
    if useCM:
        # Determine center of mass
        center = np.sum([data[i][6]*data[i][0:3] for i in range(N)])

    # Determine euclidean distances from center of mass to particles
    distances = np.array([np.linalg.norm(data[i][0:3] - center) for i in range(N)])
    indices = np.argsort(distances)
    
    return indices, distances

if __name__ == '__main__':
    import time
    import sys
    import os

    path = os.path.dirname(os.path.realpath(__file__))
    dataFile = path + '/test/data.e2.12.txt' # Default test file

    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    
    data = np.loadtxt(dataFile)
    
    TIME_START = time.time() # Used for benchmarking
    print binnedIndicesAndDistances(data)
    print 'Run time:', time.time() - TIME_START