# -*- coding: iso-8859-1 -*-
import numpy as np
from scipy.spatial.distance import *

def pair_algorithm(data, G, dt, t_end):
    """ """
    a = np.zeros((10,3));
    for i in range(10):
        for j in range(10):
            if i == j:
                continue
            a[i,:] += G/(euclidean(data[i,:3],data[j,:3])**2) * (data[j,:3] - data[i,:3])
    
    t = 0
    while t <= t_end:
        for i in range(0,10):
            data[i,3:6] = data[i,3:6] + a[i] * dt             # Opdater hastigheder
            data[i,:3] = data[i,:3] + data[i,3:6]* dt       # Opdatér positioner
        t += dt

if __name__ == "__main__":
    pass
    