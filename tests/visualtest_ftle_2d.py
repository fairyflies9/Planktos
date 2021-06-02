'''
Script for visual-inspection tests of 2D FTLE
'''

import numpy as np
import sys
sys.path.append('..')
import Planktos, motion

# TODO: get a less-difficult geometry
envir = Planktos.environment(char_L=0.1, rho=1, mu=0.001, U=15)
# envir.read_IB2d_vtk_data('data/channel_cyl', 5.0e-5, 1000, d_start=1)
envir.read_IB2d_vtk_data('data/channel_cyl', 5.0e-5, 1000, d_start=20, d_finish=20)
envir.read_IB2d_vertex_data('data/channel_cyl/channel.vertex')

# s = envir.add_swarm(900, init='grid', grid_dim=(30,30), testdir='x1')

# Test basic tracer particles on a masked mesh.
# envir.calculate_FTLE((102,25),T=0.1, dt=0.001, testdir='x1')
# sf, time_list, last_time = envir.calculate_FTLE((512,128),T=0.1,dt=0.001)


sf, time_list, last_time = envir.calculate_FTLE((512,128),T=0.1,dt=0.001,
                                                ode_gen=motion.inertial_particles,
                                                props={'R':2/3, 'diam':0.01})

envir.plot_2D_FTLE()