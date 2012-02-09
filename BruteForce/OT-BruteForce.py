#!/usr/bin/env python

"""OT-BruteForce.py: Brute force implementation of a n-body simulator"""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi"]
__email__       = "toyorhan@gmail.com"
__version__     = "0.7"

import numpy as np
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

G = 6.67e-11    # Gravitational constant
N = len(data)   # Number of points

print 'Simulating', N, 'particles...'

for t in np.arange(0, T, dt):
    for i in range(N):
        # Latest position and velocity (of i'th particle)
        xi = data[i][0:3]
        vi = data[i][3:6]
        
        # Determine acceleration (of i'th particle)
        a = np.zeros(3)
        for j in range(N):
            # Resulting vector between the i'th and the j'th particle
            r = data[j][0:3] - xi
            if np.linalg.norm(r) > 0.0: # Avoid division by zero
                a = a + (1.0/np.linalg.norm(r))*r
        
        a = G*a
        
        # New position and velocity
        xii = xi + vi*dt
        vii = vi + a*dt
        
        # Store back in data matrix
        data[i][0:3] = xii
        data[i][3:6] = vii

# Output data
np.savetxt(path + '/OT-BruteForce-EndData-N' + str(N) + '.txt', data);
print 'Run time:', time.time() - TIME_START