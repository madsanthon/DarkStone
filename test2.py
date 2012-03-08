# -*- coding: iso-8859-1 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import datetime

from Bins import *
from NBodySolver import *

now = datetime.datetime.now()

def plot_bin_components(components,bin,coordinate_names,title,format="png",axis=[-1, 1, 0, 12000]):
    if components.shape[1] != len(coordinate_names):
        raise InputError;
    fig = plt.figure()
    grid = gridspec.GridSpec(1, 3)
    subplots = [fig.add_subplot(grid[0]), fig.add_subplot(grid[1]), fig.add_subplot(grid[2])]
    
    for i,cname in enumerate(coordinate_names):
        subplots[i].scatter(components[bin, i], bin)
        
        subplots[i].set_xlabel(cname)
        subplots[i].set_ylabel('i')
        subplots[i].axis(axis)
        subplots[i].set_title(title + ' ' + cname)
    
    fig.savefig(title + '.' + format)
    return fig,subplots

def plot_bin_hist(components,bin,no_of_bins,coordinate_names,title,format="png",axis=[-1, 1, 0, 12000]):
    if components.shape[1] != len(coordinate_names):
        raise InputError;
    fig = plt.figure()
    grid = gridspec.GridSpec(1, 3)
    subplots = [fig.add_subplot(grid[0]), fig.add_subplot(grid[1]), fig.add_subplot(grid[2])]
    
    for i,cname in enumerate(coordinate_names):
        subplots[i].hist(components[bin, i], no_of_bins)
        
        subplots[i].set_xlabel(cname)
        subplots[i].set_ylabel('i')
        subplots[i].set_title(title + ' ' + cname)
    
    fig.savefig(title + '.' + format)
    return fig,subplots

def density_function(pos,bin):
    """ """
    return [bin_density(pos, bin) for bin in bin_indices], [bin_distance(pos, bin) for bin in bin_indices]

def plot_density(pos,bin_indices):
    """ """
    rho_fig = plt.figure()
    rho_ax = rho_fig.add_subplot(111)
    rho_ax.loglog([bin_distance(pos, bin) for bin in bin_indices], [bin_density(pos, bin) for bin in bin_indices],'o')
    
    #rho_fig.savefig("Taethed_som_funktion_af_middel_radius.png")
    
    return rho_fig,rho_ax

if __name__ == "__main__":
    import time
    print "Running script"
    #Loads the data...
    
    #data = np.loadtxt("mossa.e4.12.txt");
    print "Loading data."
    data = np.load("End_Result_data2012-03-06_2251.npy")
    print "Data loaded."
    #Run the algorithm, with the data-structure, then 
    #pair_algorithm(data, 1, 0.1, 4)
    #Splits the data, so it is in three different variables
    pos, vel, m = GetParticleData(data);
    print "Values extrated from data set."

    npb = int(len(data) / 20);
    
    log_file = file("End_Result_log_" + now.strftime("%Y-%m-%d_%H%M") + ".txt",'w') 
    
    fig = plt.figure()
    #TODO: Fremstil en funktion, givet et heltal, retunere en farve. Brug en formel eller kæmpe liste af farver. 
    color = ['y', 'r', 'c', 'g', 'b']
    format = "png"
    bin_indices = []
    j = 0
    ax = fig.gca(projection='3d')
    
    bin_hists = []
    bin_figures_vel = [];
    print "Processing bins."
    for bin in bins_indices(pos, npb):
        print >> log_file, "Number of particles in each bin:",npb
        print >> log_file, "Number of bins thus is:",int(len(data))/npb,"\n"
        print >> log_file, "-"*64
        print >> log_file, "Bin " + str(j+1) + " has this many particles:", len(bin)
        print >> log_file, "Sum of velocities in the bin particles:", bin_velocity(vel, bin)
        print >> log_file, "Sigma squared:", bin_sigma(vel, bin)
        print >> log_file, "Volume of bin:", bin_volume(pos, bin)
        print >> log_file, "Middel afstand af bin:", bin_distance(pos, bin),
        print >> log_file, "Taetheden af bin:",bin_density(pos, bin),
        print >> log_file, "-"*32
        
        #List of velocity figures
        #plot_bin_components(vel, bin, ["v_x","v_y","v_z"],"Hastigheder for bin" + str(j + 1))
        #bin_hists.extend(plot_bin_hist(vel, bin, 20, ["v_x","v_y","v_z"],"Hastigheder bin" + str(j + 1) + " binnede med 20 bins"))
        #grid.tight_layout(bin_figures_vel[j])
        
        bin_indices.append(bin)
        
        #ax.scatter(np.log(np.abs(pos[bin,0])),np.log(np.abs(pos[bin,1])),np.log(np.abs(pos[bin,2])), c=color[j])
        
        
        
        j += 1
    print np.sum([bin_mass(m,bin) for bin in bin_indices])
    print "Finished processing bins."
    rho_fig,rho_ax = plot_density(pos,bin_indices)
    rho_0 = 1/(2 * np.pi)
    r_s = 1
    bin_distances = [r for r in map(lambda bin: bin_distance(pos,bin),bin_indices)]
    
    print "Middelradius r_m",bin_distances
    print "Binnes tæthed rho",[bin_density(pos, bin) for bin in bin_indices]
    rho_function = lambda r: rho_0/((r/r_s)*(1 + r/r_s)**3 )
    rho_ax.loglog(bin_distances,map(rho_function,bin_distances),'x')
    rho_ax.set_xlim(0.01,100)
    rho_fig.savefig("Tætheden som funktion af middel radius.png")
    c = 50
    xlim, xmax = c,c
    ylim, ymax = c,c
    ax.set_xlim3d(-xlim, xmax)
    ax.set_ylim3d(-ylim, ylim)
    ax.set_zlim3d(0, 2*c)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    fig.savefig("3Dplot.png")
    plt.show()
    #np.save("End_Result_data" + now.strftime("%Y-%m-%d_%H%M"), data)
    log_file.close()
    print "Finished executing everything, and file saved. Press any key to continue."
    #print raw_input()