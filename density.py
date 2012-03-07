#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""density.py: Takes particle data file, runs N-body simulation and then splits particles into bins and plots density"""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi"]
__email__       = "toyorhan@gmail.com"
__version__     = "0.9"

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from bruteforce import *

def densityPlot(data, t):
    # Determine center of mass
    centerOfMass = np.zeros(3)
    for i in range(N):
        centerOfMass = centerOfMass + data[i][6]*data[i][0:3]
    print 'Center of mass:', centerOfMass

    # Determine euclidean distances from center of mass to particles
    distances = np.zeros(N)
    for i in range(N):
        distances[i] = np.linalg.norm(data[i][0:3] - centerOfMass)

    distances = np.sort(distances) # Sort

    # Split particles into bins
    nBins = 5
    particlesPerBin = N / nBins
    binRadius = np.zeros(nBins)
    binDensity = np.zeros(nBins)
    for i in range(nBins):
        if i < nBins - 1:
            binRadius[i] = distances[particlesPerBin]
            binDensity[i] = particlesPerBin / (4.0/3.0*np.pi*binRadius[i]**3)
            distances = distances[particlesPerBin:]
        else:
            binRadius[i] = np.max(distances)
            binDensity[i] = len(distances) / (4.0/3.0*np.pi*binRadius[i]**3)
    
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(binRadius, np.log(binDensity), 'bo:')
    ax.set_xlabel('Bin radius')
    ax.set_ylabel('Density')
    ax.set_xlim([0, 2])
    ax.set_ylim([-10, 10])
    ax.set_title('N-body simulation with ' + str(N) + ' particles @ t = ' + str(t))
    plt.savefig("density-%02d.png" % (t, ))

path = os.path.dirname(os.path.realpath(__file__))
dataFile = path + '/initialData-N10.txt' # Default test file

if len(sys.argv) > 1:
    dataFile = sys.argv[1]

data = np.loadtxt(dataFile)

G = 6.67e-11              # Gravitational constant
N = data.shape[0]         # Number of particles
rho = N/1.0               # Number of particles per 1m^3
dynT = 1.0/np.sqrt(G*rho) # Dynamic time
dt = 0.1                  # Time step, relative to the dynamic time
T = 16                    # Number of dynamic times to iterate over

print 'T =', T

# Iterate over T (theoretic) dynamic times
for t in np.arange(0, T, dt):
    print t
    data = nBody(data, dynT*dt)
    
    if 0.0 + int(t) == t:
        densityPlot(data, t)

# Save end data
np.savetxt('endData-N' + str(N) + '.txt', data)