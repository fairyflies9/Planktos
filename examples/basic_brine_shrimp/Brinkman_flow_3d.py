#! /usr/bin/env python3

import sys
sys.path.append('../..')
from sys import platform
if platform == 'darwin': # OSX backend does not support blitting
    import matplotlib
    matplotlib.use('Qt5Agg')
import planktos

# High-viscous enviornment (Re=10)
envir = planktos.environment(Lx=.5,Ly=.5,Lz=1, rho=1000, mu=10)
# Specify static velocity along the top of the domain
U = 0.09818
# Specify pressure gradient
dpdx = 0.0234759411877

envir.set_brinkman_flow(alpha=37.24, h_p=0.15, U=U, dpdx=dpdx, res=101)
envir.add_swarm()
s = envir.swarms[0]

# Specify amount of jitter (mean, covariance)
# Set std as 1 cm = 0.01 m
s.shared_props['cov'] *= 0.01**2

print('Moving swarm...')
for ii in range(240):
    s.move(0.1)


##########              Plot!               ###########
s.plot_all(movie_filename='brine_shrimp_Brinkman.mp4', fps=20)
#s.plot_all()