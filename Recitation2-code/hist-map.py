#!/usr/bin/env python
import sys
import numpy

### Prevents pipe IO errors for large files.
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
###

# read parameters from distributed cache - nbins, minmeanmax

f = open('nbins','r') # read nbins file
params = f.readline().strip().split() # read nbins file
nbins = int(params[0]) # set maximum number of bins
f.close()

f = open('mmm','r') # open mmm file

'''
Read mmm file and assign min, max and mean values.
File read operation in similar to above reading procedure.
'''
params =  # your code
xmax = float(params[1]) 
params = # your code
xmean = float(params[1])
params = # your code 
xmin = float(params[1])
f.close()


'''
Bin width = (max - min) / total bins
Calculate bin width using formula
'''
dx = # bin width calculation 


# compute bin centre
#### complete this code


# process input data
#### complete this code
