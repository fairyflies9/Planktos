'''
Script for visual-inspection tests of 2D FTLE
'''

import sys
sys.path.append('..')
<<<<<<< HEAD
import planktos
from planktos import motion

envir = planktos.environment(char_L=0.1, rho=1, mu=0.001, U=15)
envir.read_IB2d_vtk_data('data/channel_cyl', 5.0e-5, 1000, d_start=1)
# envir.read_IB2d_vtk_data('data/channel_cyl', 5.0e-5, 1000, d_start=20, d_finish=20)
=======
import Planktos

# TODO: get a less-difficult geometry
envir = Planktos.environment()
# envir.read_IB2d_vtk_data('data/channel_cyl', 5.0e-5, 1000, d_start=1)
envir.read_IB2d_vtk_data('data/channel_cyl', 5.0e-5, 1000, d_start=20, d_finish=20)
>>>>>>> parent of bf84b0e (Adds props argument to calculate_FTLE)
# envir.read_IB2d_vertex_data('data/channel_cyl/channel.vertex')

# envir.plot_flow()
# s = envir.add_swarm(900, init='grid', grid_dim=(30,30), testdir='x1')

<<<<<<< HEAD
#### for use when testing FTLE with passed in swarm ####
class ftle_swrm(planktos.swarm):
    
    def get_positions(self, dt, params=None):
       return self.positions + self.get_fluid_drift()*dt

#### Test basic tracer particles ####
# envir.calculate_FTLE((102,25),T=0.1, dt=0.001, testdir='x1') # w/ vertex data
sf, time_list, last_time = envir.calculate_FTLE((512,128),T=0.1,dt=0.001) # w/o vertex data

#### Test a passed in ode generator ####
# sf, time_list, last_time = envir.calculate_FTLE((512,128),T=0.1,dt=0.001,
#                                                 ode_gen=motion.inertial_particles,
#                                                 props={'R':2/3, 'diam':0.01})
=======
# Test basic tracer particles on a masked mesh.
# envir.calculate_FTLE((102,25),T=0.1, dt=0.001, testdir='x1')
sf, time_list, last_time = envir.calculate_FTLE((512,128),T=0.1,dt=0.001)
>>>>>>> parent of bf84b0e (Adds props argument to calculate_FTLE)

#### Test a passed in swarm object ####
# swrm = ftle_swrm(envir=envir)
# sf, time_list, last_time = envir.calculate_FTLE((512,128),T=0.1,dt=0.001, swrm=swrm)

envir.plot_2D_FTLE()
