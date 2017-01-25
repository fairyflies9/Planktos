#! /usr/bin/env python3

'''
Swarm class file, for simulating many individuals at once.

Created on Tues Jan 24 2017

Author: Christopher Strickland
Email: wcstrick@live.unc.edu
'''

import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import warnings
import init_pos

__author__ = "Christopher Strickland"
__email__ = "wcstrick@live.unc.edu"
__copyright__ = "Copyright 2017, Christopher Strickland"

class environment:

    def __init__(self, Lx=100, Ly=100, x_bndry = None, y_bndry = None,
        init_swarms = None):
        ''' Initialize environmental variables.

        Arguments:
            Lx: Length of domain in x direction
            Ly: Length of domain in y direction
            x_bndry: [left bndry condition, right bndry condition]
            y_bndry: [low bndry condition, high bndry condition]
            init_swarms: initial swarms in this environment

        Right now, the only supported boundary condition is 'zero', which
        is also the default.
        '''

        # Save domain size
        self.L = [Lx, Ly]

        # Parse boundary conditions
        supprted_conds = ['zero']
        self.bndry = []

        if x_bndry is None:
            # default boundary conditions
            self.bndry.append(['zero', 'zero'])
        elif x_bndry[0] not in supprted_conds or x_bndry[1] not in supprted_conds:
            print("X boundary condition {} not implemented.".format(x_bndry))
            print("Exiting...")
            raise NameError
        else:
            self.bndry.append(x_bndry)
        if y_bndry is None:
            # default boundary conditions
            self.bndry.append(['zero', 'zero'])
        elif y_bndry[0] not in supprted_conds or y_bndry[1] not in supprted_conds:
            print("Y boundary condition {} not implemented.".format(y_bndry))
            print("Exiting...")
            raise NameError
        else:
            self.bndry.append(y_bndry)

        # swarm list
        if init_swarms is None:
            self.swarms = []
        else:
            if isinstance(init_swarms,list):
                self.swarms = init_swarms
            else:
                self.swarms = [init_swarms]



class swarm:

    def __init__(self, swarm_size=100, envir=None, init='random', **kwargs):
        ''' Initalizes planktos swarm in a domain of specified size.

        Arguments:
            envir: environment for the swarm, defaults to the standard environment
            swarm_size: Size of the swarm (int)
            init: Method for initalizing positions. Currently, only 'random'
                is supported.
            kwargs: keyword arguments to be passed to the method for
                initalizing positions
        '''

        # use a new default environment if one was not given
        if envir is None:
            self.envir = environment(init_swarms = self)
        else:
            try:
                assert isinstance(envir,environment)
                envir.swarms.append(self)
                self.envir = envir
            except AssertionError:
                print("Error: invalid environment object.")
                raise

        # initialize bug locations
        self.positions = ma.zeros((swarm_size, 2))
        if init == 'random':
            init_pos.random(self.positions, self.envir.L)
        else:
            print("Initialization method {} not implemented.".format(init))
            print("Exiting...")
            raise NameError

        # Initialize time and history
        self.time = 0.0
        self.time_history = []
        self.pos_history = []



    def move(self, dt=1.0, params=None):
        ''' Move all organsims in the swarm over an amount of time dt '''

        # Put current time/position in the history
        self.time_history.append(self.time)
        self.pos_history.append(self.positions.copy())

        # For now, just have everybody move according to a random walk.
        self.__gaussian_walk(self.positions, [0,0], dt*np.eye(2))

        # Apply boundary conditions.
        for dim, bndry in enumerate(self.envir.bndry):
            if bndry[0] == 'zero':
                # mask everything exiting on the left
                self.positions[self.positions[:,dim]<= 0, :] = ma.masked
            else:
                raise NameError
            if bndry[1] == 'zero':
                # mask everything exiting on the right
                self.positions[self.positions[:,dim]>= self.envir.L[dim], :] = ma.masked
            else:
                raise NameError
        
        # Record new time
        self.time += dt



    @staticmethod
    def __gaussian_walk(pos_array, mean, cov):
        ''' Move all rows of pos_array a random distance specified by
        a gaussian distribution with given mean and covarience matrix '''

        pos_array += np.random.multivariate_normal(mean, cov, pos_array.shape[0])



    def plot(self, blocking=True):
        ''' Plot the current position of the swarm '''

        plt.figure()
        plt.scatter(self.positions[:,0], self.positions[:,1], label='organism')
        plt.xlim((0, self.envir.L[0]))
        plt.ylim((0, self.envir.L[1]))
        plt.title('Organism positions')
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            if blocking:
                plt.show()
            else:
                plt.draw()
                plt.pause(0.001)



    def plot_all(self):
        ''' Plot the entire history of the swarm's movement, incl. current '''

        plt.figure()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            for pos, t in zip(self.pos_history, self.time_history):
                plt.scatter(pos[:,0], pos[:,1], label='organism')
                plt.xlim((0, self.envir.L[0]))
                plt.ylim((0, self.envir.L[1]))
                plt.title('Organism positions, time = {:.2f}'.format(t))
                plt.draw()
                plt.pause(0.001)
                plt.clf()
            plt.scatter(self.positions[:,0], self.positions[:,1], label='organism')
            plt.xlim((0, self.envir.L[0]))
            plt.ylim((0, self.envir.L[1]))
            plt.title('Organism positions, time = {:.2f}'.format(self.time))
            plt.draw()
            plt.pause(0.001)
            plt.show()
