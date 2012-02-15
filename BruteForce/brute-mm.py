## Project: Dark Stone, NBI
## Script: Brute-Force method to solving N-body
## Description: ...
## Group: Mossa Merhi. 
## Date: 8/02-2012

import numpy as np
from scipy.spatial.distance import *
mass = 1;
G = 6.67384*10**-11
start_t = 0
slut_t = 10
dt = 0.1

data = np.loadtxt('initialData-N10.txt');

a = np.zeros((10,3));
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        a[i,:] += G/(euclidean(data[i,:3],data[j,:3])**2) * (data[j,:3] - data[i,:3])

print a
print a.shape
print

t = 0
while t <= slut_t:
    for i in range(0,10):
        data[i,3:] = data[i,3:] + a[i] * dt             # Opdatér hastigheder
        data[i,:3] = data[i,:3] + data[i,3: ]* dt       # Opdatér positioner
    t += dt
print data

np.savetxt('MM-BruteForce-EndData-N10.txt',data);
