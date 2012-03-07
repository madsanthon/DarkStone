#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import time
import os
from BruteForce.ot import *

path = os.path.dirname(os.path.realpath(__file__))
dataFile = path + '/initialData-N10.txt' # Default test file

if len(sys.argv) > 1:
    dataFile = sys.argv[1]

data = np.loadtxt(dataFile)

T = 10   # Total time, seconds
dt = 0.1 # Time step, seconds

print 'Simulating', data.shape[0], 'particles...'

print 'Data before:'
print data

for t in np.arange(0, T, dt):
    print t
    data = nBody(data, dt)

print
print 'Data after', T, 'seconds:'
print data

print 'Done.'