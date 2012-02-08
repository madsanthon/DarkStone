## Project: Dark Stone, NBI
## Script: Generate start data
## Description: This file generates n particle start positions and
##  velocities. The data is saved into a file called my_data_<n>.txt, where n
##  is the number of particles generated. 
## Group: Mads Anthon, Orhan Toy, Mossa Merhi. 
## Date: 8/02-2012

import numpy as np

print("n:")
n = input()

data = np.random.rand(n,6);

np.savetxt('my_data_'+str(n)+'.txt',data);
