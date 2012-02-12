#!/usr/bin/env python

"""initialDataGenerator.py: This file generates <N> particle start
positions and velocities. The data is saved into a file called 
initialData-N<N>.txt, where <N> is the number of particles generated."""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi", "Orhan Toy"]
__version__     = "0.7"

import numpy as np
import sys

N = 10 # Default

if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
    N = int(sys.argv[1])

# Generate a N x 6 matrix and save it
data = np.random.rand(N, 6)
np.savetxt('initialData-N' + str(N) + '.txt', data)

print 'Data file with', N, 'particles has been generated.'