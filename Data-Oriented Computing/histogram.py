#from myhistogram import histogram1d
from numpy import *
def histogram(xall,xmin,xmax,nbinsx=10,rawcounts=False):
    xfac = float(nbinsx)/float(xmax-xmin)
    inbox = logical_and(xall>=xmin,xall<xmax);
    x = xall[ inbox ]
    ix = array( (x-xmin)*xfac, dtype=int )
    counts = zeros(nbinsx,dtype=int)
    add.at( counts, ix, 1 )
    dx = (xmax-xmin)/float(nbinsx)
    #bincenters = linspace(xmin,xmax,nbinsx+1)[:-1]+0.5*dx
    left        = linspace(xmin,xmax,nbinsx+1)[:-1] # left ends of bins
    if rawcounts:
       #return bincenters,counts
       return left,counts
    else:
        # return probability density samples
        #return bincenters, counts/(dx*float(len(xall)))
        return left, counts/(dx*float(len(xall)))