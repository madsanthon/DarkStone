#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""MM-BruteForce.py: Brute-Force method to solving N-body"""

__author__      = "Mossa Merhi"
__credits__     = ["Mads Anthon", "Orhan Toy"]
__email__       = "cgmossa@gmail.com"
__version__     = "0.8"

import numpy as np
from scipy.spatial.distance import *
import sys
import os

path = os.path.dirname(os.path.realpath(__file__))
dataFile = path + '/../initialData-N10.txt' # Default test file

if len(sys.argv) > 1:
    dataFile = sys.argv[1]

data = np.loadtxt(dataFile)

G = 6.67384*10**-11

a = np.zeros((10,3));
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        a[i,:] += G*data[j,6]/(euclidean(data[i,:3],data[j,:3])**2) * (data[j,:3] - data[i,:3])

def nBody(data, dt):
    for i in range(0,10):
        data[i,3:6] = data[i,3:6] + a[i] * dt             # Opdatér hastigheder
        data[i,:3] = data[i,:3] + data[i,3:6]* dt       # Opdatér positioner

    return data

if __name__ == '__main__':
    import time
    
    TIME_START = time.time() # Used for benchmarking
    
    start_t = 0
    slut_t = 10
    dt = 0.1
    
    print 'Simulating', data.shape[0], 'particles...'
    
    print 'Data before:'
    print data

    t = 0
    while t <= slut_t:
        data = nBody(data, dt)
        t += dt

    print 'Data after', slut_t, 'seconds:'
    print data

    print
    print 'Run time:', time.time() - TIME_START