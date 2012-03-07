#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""bruteforce.py: Brute force implementation of a n-body simulator"""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi"]
__email__       = "toyorhan@gmail.com"
__version__     = "1.0"

import numpy as np

def nBody(data, dt, G=6.67e-11):
    N = data.shape[0] # Number of particles

    dataCopy = np.copy(data)
    for i in range(N):
        # Latest position and velocity (of i'th particle)
        si = data[i][0:3]
        vi = data[i][3:6]

        # Determine acceleration (of i'th particle)
        a = np.zeros(3)
        for j in range(N):
            # Resulting vector between the i'th and the j'th particle.
            # We use dataCopy because we do not want the updated positions.
            r  = dataCopy[j][0:3] - si
            mj = dataCopy[j][6] # Mass of j'th particle
            if np.linalg.norm(r) > 0.0: # Avoid division by zero
                a = a + mj/(np.linalg.norm(r)**2)*r

        a = G*a

        # New position and velocity
        sii = si + vi*dt
        vii = vi + a*dt

        # Store back in data matrix
        data[i][0:3] = sii
        data[i][3:6] = vii

    return data

if __name__ == '__main__':
    import time
    import sys
    import os
    
    TIME_START = time.time() # Used for benchmarking

    path = os.path.dirname(os.path.realpath(__file__))
    dataFile = path + '/initialData-N10.txt' # Default test file
    
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    
    data = np.loadtxt(dataFile)
    
    T = 10          # Total time, seconds
    dt = 0.1        # Time step, seconds
    
    print 'Simulating', data.shape[0], 'particles...'
    
    print 'Data before:'
    print data
    
    for t in np.arange(0, T, dt):
        data = nBody(data, dt)
    
    print 'Data after', T, 'seconds:'
    print data
    
    print
    print 'Run time:', time.time() - TIME_START