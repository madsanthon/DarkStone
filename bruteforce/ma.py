#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""MA-BruteForce.py: Brute force implementation of a n-body simulator"""

__author__      = "Mads Anthon"
__credits__     = ["Orhan Toy", "Mossa Merhi"]
__email__       = "madsanthon@gmail.com"
__version__     = "0.9"

import numpy as np

def nBody(data, dt):
    G = 6.67e-11    # Gravitational constant
    N = len(data)   # Number of points

    for i in range(N):
        #initializing data
        xi = data[:,:3]
        vi = data[:,3:6]
        mi = data[:,6]
        inv_r = 0
        a = np.zeros(3)

        #calculating accereration
        #ma = (Gm/(r*r))*|r| -> a = G*|r|/(r*r)

        for j in range(N):
            r = xi[j] - xi[i]
            if np.linalg.norm(r) > 0:
                inv_r = 1.0/np.linalg.norm(r) #invers distance from xi[j] to xi[j]
                a += G*mi[j]*(inv_r*inv_r)*r

        #updating data for next loop
        data[:,:3] = xi + vi*dt
        data[:,3:6] = vi + a*dt
    
    return data

if __name__ == '__main__':
    import time
    import sys
    import os
    
    TIME_START = time.time() # Used for benchmarking

    path = os.path.dirname(os.path.realpath(__file__))
    dataFile = path + '/../initialData-N10.txt' # Default test file
    
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    
    data = np.loadtxt(dataFile)
    
    T = 10          # Total time, seconds
    dt = 0.1        # Time step, seconds
    t = 0           # Start time
    
    print 'Simulating', data.shape[0], 'particles...'
    
    print 'Data before:'
    print data
    
    while t < T: #setting time of run
        data = nBody(data, dt)
        t += dt #counter

    print 'Data after', T, 'seconds:'
    print data
    
    print
    print 'Run time:', time.time() - TIME_START