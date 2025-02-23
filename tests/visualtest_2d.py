#! /usr/bin/env python3
''' Loads data for a concave, 2D mesh generated in ib2d with time-varying flow.
Simulates agents for the purpose of making sure that the boundary is respected.
'''

import numpy as np
import sys
sys.path.append('..')
import planktos

envir = planktos.environment()
envir.read_IB2d_vtk_data('data/leaf_data', 1.0e-5, 100, d_start=1)
### Use to test for boundary crossings ###
envir.read_IB2d_vertex_data('data/leaf_data/leaf.vertex', 1.45)
envir.add_vertices_to_2D_ibmesh()

### Test for boundary crossings ###
envir.add_swarm(seed=10)
s = envir.swarms[0]
s.positions[89,:] = (0.05, 0.075)
s.positions[95,:] = (0.17, 0.1)
s.shared_props['cov'] *= 0.001
#######

### This is the incorrect mesh for the fluid. Use only for init_grid testing ###
# from give_me_circle_vertices import give_Me_Immersed_Boundary_Geometry
# Nx = len(envir.flow_points[0])
# Ny = len(envir.flow_points[1])
# ds = min(envir.L[0]/(2*Nx),envir.L[1]/(2*Ny))
# give_Me_Immersed_Boundary_Geometry(ds,0.05,np.array(envir.L)/2)
# envir.read_IB2d_vertex_data('circle.vertex')
#######

### Test for mesh_init ###
# s = envir.add_swarm(init='grid', grid_dim=(30,40), testdir='x0')
#######

# envir.plot_envir()
s.plot()

# print('Moving swarm...')
# for ii in range(500):
#     s.move(0.0005)
    
# s.plot_all(movie_filename='leaf_2d_vort.mp4', figsize=(6,9), fps=30, fluid='vort')
