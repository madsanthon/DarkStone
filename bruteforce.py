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
                a = a + mj/(np.linalg.norm(r)**3)*r

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

    path = os.path.dirname(os.path.realpath(__file__))
    dataFile = path + '/test/data.e1.12.txt' # Default test file
    
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    
    data = np.loadtxt(dataFile)
    N = data.shape[0]
    
    G = 1    # Gravitational constant
    dt = 0.1 # Time step, relative to the dynamic time
    T = 4    # Number of dynamic times to iterate over
    
    # We randomly choose 3 particles and follow their positions
    while True:
        iFollow = np.random.randint(0, high=N, size=3)
        if iFollow.shape == np.unique(iFollow).shape:
            break
    
    pFollow = np.array([np.zeros((np.floor(T/dt), 3)) for i in range(len(iFollow))])
    
    print 'Simulating', N, 'particles...'

    TIME_START = time.time() # Used for benchmarking

    for i, t in enumerate(np.arange(0, T, dt)):
        print t, time.time() - TIME_START
        
        # Store the randomly chosen particles positions at every time step
        for j in range(len(iFollow)):
            pFollow[j][i] = data[iFollow[j]][0:3]

        nBody(data, dt, G)

    print 'Run time:', time.time() - TIME_START
    
    print pFollow
    
    ts = time.strftime('%Y%m%d%H%M')
    np.savetxt(path + '/result/endData-N' + str(N) + '-' + ts + '.txt', data)
    
    # Save particle positions, individually
    for j in range(len(iFollow)):
        np.savetxt(path + '/result/logPos-N' + str(N) + '-' + str(j + 1) + '-' + ts + '.npz', pFollow[j])
