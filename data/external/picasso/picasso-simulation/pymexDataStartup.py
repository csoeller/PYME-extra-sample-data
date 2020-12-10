# startup setup
import numpy as np
import matplotlib.pyplot as plt
plt.rc('image', interpolation='nearest', cmap='gray')

import os
# make sure we have the directory into which we write build-data
bdir = 'build'
def inbdir(filename):
    return os.path.join(bdir,filename)

if not os.path.exists(bdir):
    os.makedirs(bdir)
