#!/usr/bin/env python

"""MA-BruteForce.py: Brute force implementation of a n-body simulator"""

__author__      = "Mads Anthon"
__credits__     = ["Orhan Toy", "Mossa Merhi"]
__email__       = "madsanthon@gmail.com"
__version__     = "1.1"

import numpy as np
import time

print 'Script running...'

TIME_START = time.time() # Used for benchmarking

data = np.loadtxt('initialData-N10.txt')

T = 10          # Total time, seconds
dt = 0.1        # Time step, seconds
t = 0           # Start time

G = 6.67e-11    # Gravitational constant
N = len(data)   # Number of points


while t < T: #setting time of run
  for i in range(N):

    #initializing data
    xi = data[:,:3]
    vi = data[:,3:6]
    inv_r = []
    a = [0,0,0]

    #calculating accereration
    #ma = (Gm/(r*r))*|r| -> a = G*|r|/(r*r)
    
    for j in range(N):
      r = xi[j]-xi[i]
      if np.linalg.norm(r) > 0:
        inv_r = 1.0/np.linalg.norm(r) #invers distance from xi[j] to xi[j]
    a = G*(inv_r*inv_r)*r

    #updating data for next loop
    data[:,:3] = xi + vi*dt + 0.5*a*dt*dt
    data[:,3:6] = vi + a*dt

  t += dt #counter
  
#saving result in txt file
np.savetxt('MA-BruteForce-EndData-N10.txt',data)

print 'Run time:', time.time() - TIME_START
