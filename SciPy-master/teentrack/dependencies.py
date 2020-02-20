#
# SciPy 2019 Teen Track
# Checks to make sure you have the correct dependencies installed
#

import sys
import os
from subprocess import check_call, CalledProcessError
import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt

pyversion = sys.version.split()[0]
assert (pyversion >= "3.6"), "You have Python "+str(pyversion)+" installed. Please install Python 3.6 or above."
nversion = np.version.version
assert (nversion >= "1.15"), "You have NumPy "+str(nversion)+" installed. Please install NumPy 1.15 or above."
sversion = scipy.version.version
assert (sversion >= "1.0"), "You have SciPy "+str(sversion)+" installed. Please install SciPy version 1.0 or above."
try:
    jversion = check_call(["jupyter", "--version"])
    print("Success - all dependencies are present!")
except:
    print("You do not have Jupyter notebook installed.Please install Jupyter notebook.")