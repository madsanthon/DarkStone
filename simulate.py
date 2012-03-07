#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""simulate.py: Simulation of n-body system"""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi"]
__email__       = "toyorhan@gmail.com"
__version__     = "0.8"

import numpy as np
import sys
import time
import os
from bruteforce import *

path = os.path.dirname(os.path.realpath(__file__))
dataFile = path + '/initialData-N10.txt' # Default test file

if len(sys.argv) > 1:
    dataFile = sys.argv[1]

data = np.loadtxt(dataFile)

G = 1                     # Gravitational constant
N = data.shape[0]         # Number of particles
rho = N/1.0               # Number of particles per 1m^3
dynT = 1.0/np.sqrt(G*rho) # Dynamic time
dt = 0.1                  # Time step, relative to the dynamic time
T = 4                     # Number of dynamic times to iterate over

print 'Simulating', N, 'particles...'

TIME_START = time.time() # Used for benchmarking

for t in np.arange(0, T, dt):
    print t, time.time() - TIME_START
    nBody(data, dynT*dt, G)

print 'Run time:', time.time() - TIME_START

np.savetxt(path + '/Test/endData-N' + str(N) + '-' + time.strftime('%Y-%m-%d %H:%M') + '.txt', data)
