#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""initialDataGenerator.py: This file generates <N> particle start
positions and velocities. The data is saved into a file called 
initialData-N<N>.txt, where <N> is the number of particles generated."""

__author__      = "Orhan Toy"
__credits__     = ["Mads Anthon", "Mossa Merhi", "Orhan Toy"]
__version__     = "0.7"

import numpy as np
from numpy import linalg as la
import sys

N = 1000 # Default
epsilon = 10**(-6)

if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
    N = int(sys.argv[1])

# Generate a N x 6 matrix and save it
pos = np.random.rand(N,3) - (1./2) * np.ones((N,3))
vel = np.zeros((N,3))
m = np.random.rand(N,1)
m = m/la.norm(m,1);
#
# Test!
#
print "All positioner er i [-0.5,0.5]",
if filter(lambda a: 0.5-abs(a) < epsilon, pos.ravel()) == []:
    print "Ja"
else:
    print "Nej!"
print "Måske?"
print "Summen af alle partiklers hastigheder er", np.sum(vel)
print "Sum af alle masser",np.sum(m)

data = np.hstack((pos,vel,m))

np.savetxt('initialData-N' + str(N) + '.txt', data)

print 'Data file with', N, 'particles has been generated.'
