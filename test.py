import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import datetime

from Bins import *
from NBodySolver import *

now = datetime.datetime.now()

if __name__ == "__main__":
    #Loads the data...
    data = np.loadtxt("mossa.e3.12.txt");
    #Run the algorithm, with the data-structure, then 
    pair_algorithm(data, 1, 0.1, 4)
    #Splits the data, so it is in three different variables
    pos, vel, m = GetParticleData(data);

    npb = int(len(data)/5);
    
    fig = plt.figure(1)
    color = ['y','r','c','g','b']
    bin_distances = []
    bin_sigmas = []
    bin_indices = []
    j = 0
    ax = fig.add_subplot(111, projection='3d')
    plt.close("all")
    grid = gridspec.GridSpec(1,3)
    bin_figures_vel = [];
    for bin in bins_indices(pos,npb):
        print "Bin has particles with following indices:\n",bin
        print "Sum of velocities in the bin particles:",bin_velocity(vel,bin)
        print "Sigma squared:",bin_sigma(vel,bin)
        print "Volume of bin:",bin_volume(pos, bin)
        print "Middel afstand af bin:",bin_distance(pos,bin)
        bin_figures_vel.append(plt.figure(j))
        ax1 = bin_figures_vel[j].add_subplot(grid[0])
        ax1.scatter(vel[bin,0],bin,axes = [-1, 1, 0, 1],c=color[j])
        ax2 = bin_figures_vel[j].add_subplot(grid[1])
        ax2.scatter(vel[bin,1],bin,axes = [-1, 1, 0, 1],c=color[j])
        ax3 = bin_figures_vel[j].add_subplot(grid[2])
        ax3.scatter(vel[bin,2],bin,axes = [-1, 1, 0, 1],c=color[j])
        grid.tight_layout(bin_figures_vel[j])
        bin_indices.append(bin)
        bin_sigmas.append(bin_sigma(vel,bin)**0.5)
        bin_distances.append(bin_distance(pos,bin))
        ax.scatter(pos[bin,0],pos[bin,1],pos[bin,2], c=color[j])
        j += 1
    
    rho_fig = plt.figure(2)
    rho_ax = rho_fig.add_subplot(111)
    rho_ax.scatter(bin_density(pos,bin),bin_distances)
    np.save("End_Result_" + now.strftime("%Y-%m-%d_%H%M") + ".txt", data)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    
    plt.show()