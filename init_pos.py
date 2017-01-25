#! /usr/bin/env python3

'''
Library of functions for initializing a provided swarm structure.

Created on Tues Jan 24 2017

Author: Christopher Strickland
Email: wcstrick@live.unc.edu
'''

__author__ = "Christopher Strickland"
__email__ = "wcstrick@live.unc.edu"
__copyright__ = "Copyright 2017, Christopher Strickland"

import numpy as np

def random(swarm_pos, L):
    '''Uniform random initialization'''

    print('Intializing swarm with uniform random positions...')
    swarm_pos[:,0] = np.random.uniform(0, L[0], swarm_pos.shape[0])
    swarm_pos[:,1] = np.random.uniform(0, L[1], swarm_pos.shape[0])
