#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""initial.py: This file generates <N> particle start
positions and velocities. The data is saved into a file called 
initialData-N<N>.txt, where <N> is the number of particles generated."""

__author__      = "Mossa Merhi"
__credits__     = ["Mads Anthon", "Mossa Merhi", "Orhan Toy"]
__version__     = "0.7"

import numpy as np
import sys

N = 1000 # Default

if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
    N = int(sys.argv[1])

# Generate N random positions in the interval -0.5..0.5 for x, y and z
pos = np.random.rand(N, 3) - 0.5*np.ones((N, 3))

# Generate N random masses, summing to 1
m = np.random.rand(N, 1)
m = m/np.linalg.norm(m, 1) # (Sum) normalization

# Generate velocities, initially set to zero
vel = np.zeros((N, 3))

data = np.hstack((pos, vel, m))
np.savetxt('initialData-N' + str(N) + '.txt', data)

print 'Data file with', N, 'particles has been generated.'
