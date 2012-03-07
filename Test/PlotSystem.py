import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import numpy as np
from Bins import *

class PlotSystem(object):
    def __init__(self):
        self.num_of_figs = 0
    def add_plot(self):
        pass
    def save_all_plots(self):
        pass
    
if __name__ == "__main__":
    data = np.loadtxt("End_Result_2012-03-04")
    pos,vel,m = GetParticleData(data)
    
    npb = 200
    color = ['y','r','c','g','b']
    j = 0
    plt.close("all")
    grid = gridspec.GridSpec(1,3)
    bin_figures_vel = [];
    for bin in bins_indices(pos,npb):
        bin_figures_vel.append(plt.figure(j))
        bin_figures_vel[j].add_subplot(grid[0]).scatter(vel[bin,0],bin,axes = [-1, 1, 0, 1],c=color[j])
        bin_figures_vel[j].add_subplot(grid[1]).scatter(vel[bin,1],bin,axes = [-1, 1, 0, 1],c=color[j])
        bin_figures_vel[j].add_subplot(grid[2]).scatter(vel[bin,2],bin,axes = [-1, 1, 0, 1],c=color[j])
        grid.tight_layout(bin_figures_vel[j])
        j += 1
    plt.show()