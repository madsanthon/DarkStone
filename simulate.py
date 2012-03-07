#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
N = data.shape[0]

T = 10   # Total time, seconds
dt = 0.1 # Time step, seconds

print 'Simulating', N, 'particles...'

TIME_START = time.time() # Used for benchmarking

for t in np.arange(0, T, dt):
    print t
    nBody(data, dt)

print 'Run time:', time.time() - TIME_START

np.savetxt('endData-N' + str(N) + '.txt', data)