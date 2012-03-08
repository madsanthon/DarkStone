#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""animation.py: Animation of a small n-body system"""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi"]
__email__       = "toyorhan@gmail.com"
__version__     = "0.6"

import numpy as np
import time
import sys
import os
import visual
from bruteforce import *

path = os.path.dirname(os.path.realpath(__file__))
dataFile = path + '/test/initialData-N10.txt'

data = np.loadtxt(dataFile)
N = data.shape[0] # Number of points

G = 1.0   # Gravitational constant
dt = 0.01 # Time step, seconds

print 'Simulating', N, 'particles...'

# Initial particle positions
particles = []
for i in range(N):
    # Set initial velocities to zero
    data[i][3:6] = np.zeros(3)
    particle = visual.sphere(pos=tuple(data[i][0:3]), radius=0.5)
    particles.append(particle)

while 1:
    data = nBody(data, dt, G=G)

    # Update positions
    for i in range(N):
        particles[i].pos = visual.vector(data[i][0:3])