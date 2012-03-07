# -*- coding: iso-8859-1 -*-
from __future__ import division
import numpy as np
import scipy
import scipy.spatial.distance as dist
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#Version: 0.2

def GetParticleData(data):
    """ Takes a parameter called data that consists of a matrix with
    6 columns and N rows, where N is the number of particles.
    Returns three variables, the positions, the velocity and the mass"""
    pos = data[:, :3]
    vel = data[:, 3:6]
    m = data[:,6]
    return pos, vel, m

def bins_indices(pos, npb):
    """ Returns a list of indices for bins, where each bin has npb particles 
    
    Keyword arguments:
    pos -- positions of the particles, columns is components and rows is different particles.
    npb -- No. of particles in a bin
    """ 
    #Calculate the distance from 0,0,0 to all the points
    distances = GetDistancesFromOrigo(pos)
    #Sort the particles in term of 
    sort_i = np.argsort(distances)
    #NPB = No. of particles in each bin
    bins_i = [i for i in chunks(sort_i, npb)]
    return bins_i

def GetDistancesFromOrigo(pos):
    """ Returns a list of distances for the positions given in param pos."""
    return [scipy.spatial.distance.euclidean(np.array([0, 0, 0]), pos[i, :]) for i in range(len(pos))];

def GetDistancesFromPoint(P, pos):
    """ Finds the euclidiean distance between point P and all points in Positions matrix.
    
    Keyword arguments:
    P -- should be a N-D array with N coordinates.
    pos --  should be a MxN-matrix, where columns correspond to the coordinate in that dimension, 
         and rows correspond to points. 
         
         """
    return [scipy.spatial.distance.euclidean(P, pos[i, :]) for i in range(len(pos))];

def argsort(seq):
    """ Returns the indices of the elements of the iterable, such that the indices correspond to the sorted iterable."""
    return sorted(range(len(seq)), key=seq.__getitem__)

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    
    Comments: This returns an iterator, meaning it is only useable in iterative expressions.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def bin_mass(mass, bin):
    """ Given all the particles masses, it gives the sum of all masses in the given bin's indices.
    
    Keyword arguments:
    mass -- consists of all the particles masses
    bin_indices -- consist of the given bins indices
    
    """
    return sum(mass[bin,:])

def bin_velocity(velocities, bin_indices):
    """ Returns the sum of square of all velocities in the given bin 
       
    Keyword arguments:
    velocities -- consists of all the particles masses
    bin_indices -- consist of the given bins indices
    
    """
    return np.sum(np.power(velocities,2))

def bin_sigma(velocities,bin_indices):
    """ Returns sigma squared of the given bin.
    
    Keyword arguments:
    velocities -- all the velocities for all particles
    bin_indices -- indices for the particles
    
    """
    return bin_velocity(velocities,bin_indices)/(velocities.shape[0])

def bin_volume(positions, bin):
    """ Returns the volume of the bin.
    
    Assumption: Each bin is of a spherical shape, thus one substract two spheres from each other."""
    r_a = dist.euclidean(np.array([0,0,0]), positions[bin[0],:])
    r_b = dist.euclidean(np.array([0,0,0]), positions[bin[-1],:])
    return 4.0/3.0 * np.pi * (r_b**3 - r_a**3)
def bin_density(positions, bin):
    """ Returns density of the given bin. """
    return len(bin)*10**(-4)/bin_volume(positions,bin)
    
def bin_distance(pos,bin):
    """ """
    return np.sum(GetDistancesFromOrigo(pos[bin,:]))/len(bin)

if __name__ == "__main__":
    #Loads the data...
    data = np.loadtxt("mossa.e3.12.txt");
    
    #Splits the data, so it is in three different variables
    pos, vel, m = GetParticleData(data);

    N = data.shape[0]
    npb = int(N/5);
    
    fig = plt.figure(1)
    color = ['y','r','c','g','b']
    j = 0
    ax = fig.add_subplot(111, projection='3d')
    for bin in bins_indices(pos,npb):
        #print "Bin has particles with following indices:\n",bin
        #print "Velocity of bin particles:",bin_velocity(vel,bin)
        #print "Sigma squared:",bin_sigma(vel,bin)
        #print "Volume of bin:",bin_volume(pos, bin)
        print 
        ax.scatter(pos[bin,0],pos[bin,1],pos[bin,2], c=color[j])
        j += 1
        
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
