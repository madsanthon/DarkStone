#!/usr/bin/env python

"""OT-BruteForceWithAnimation.py: Brute force implementation of a n-body simulator"""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi"]
__email__       = "toyorhan@gmail.com"
__version__     = "0.5"

import numpy as np
import time
import sys
import os
import visual

path = os.path.dirname(os.path.realpath(__file__))
dataFile = path + '/initialData-N10.txt' # Default test file

if len(sys.argv) > 1:
    dataFile = sys.argv[1]

data = np.loadtxt(dataFile)

dt = 10000      # Time step, seconds

G = 6.67e-11    # Gravitational constant
N = len(data)   # Number of points

print 'Simulating', N, 'particles...'

# Initial particle positions
particles = []
for i in range(N):
    # Set initial velocities to zero
    data[i][3:6] = np.zeros(3)
    particle = visual.sphere(pos=tuple(data[i][0:3]), radius=0.5)
    particles.append(particle)

while 1:
    dataCopy = np.copy(data)
    for i in range(N):
        # Latest position and velocity (of i'th particle)
        xi = data[i][0:3]
        vi = data[i][3:6]
        
        # Determine acceleration (of i'th particle)
        a = np.zeros(3)
        for j in range(N):
            # Resulting vector between the i'th and the j'th particle.
            # We use dataCopy because we do not want the updated positions.
            r = dataCopy[j][0:3] - xi
            if np.linalg.norm(r) > 0.0: # Avoid division by zero
                a = a + (1.0/np.linalg.norm(r)**2)*r
        
        a = G*a
        
        # New position and velocity
        xii = xi + vi*dt
        vii = vi + a*dt
        
        # Store back in data matrix
        data[i][0:3] = xii
        data[i][3:6] = vii
        
        particles[i].pos = visual.vector(xii)