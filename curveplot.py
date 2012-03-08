#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""curveplot.py: Plots the curves of one or more particles"""

__author__      = ""
__email__       = ""
__version__     = ""

import time
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D

try:
    dataFile = sys.argv[1]
    positions = np.loadtxt(dataFile)
except:
    sys.exit('Data file has to be specified.')

## ----------------------------------------------------------------
## Her skal vi visualisere partiklens bane.
## ----------------------------------------------------------------

print positions