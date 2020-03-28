# -*- coding: utf-8 -*-
"""
Purpose: This script will plot the "movie" outputs
         from the Liu & Liu SPH FORTRAN code for
         the shock tube simulation.

Created: Mar 2020

@author: Ryan Clement
         scisoft@outlook.com
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set FIGURE to 8 inches by 8 inches
mpl.rcParams['figure.figsize'] = [8.0, 8.0]



# FUNCTIONS
def plotData(t,x,vx,p,d,u):
    fig, axs = plt.subplots(2,2,sharex=True,constrained_layout=True)
    fig.suptitle('Time = '+str(t))
    # Velocity
    axs[0,0].plot(x,vx)
    axs[0,0].set_xlim(-.4,.4)
    axs[0,0].set_ylim(-.1,1.1)
    axs[0,0].set_title('Velocity')
    axs[0,0].grid(True)
    # Pressure
    axs[0,1].plot(x,p,'tab:red')
    axs[0,1].set_ylim(-.1,1.2)
    axs[0,1].set_title('Pressure')
    axs[0,1].grid(True)
    # Density
    axs[1,0].plot(x,d,'tab:purple')
    axs[1,0].set_ylim(0,1.2)
    axs[1,0].set_title('Density')
    axs[1,0].grid(True)
    # Internal Energy
    axs[1,1].plot(x,u,'tab:green')
    axs[1,1].set_ylim(1.5,2.8)
    axs[1,1].set_title('Internal Energy')
    axs[1,1].grid(True)

def getData():
    # Movie Data File
    mFile = '../data/movie.dat'
    # Load Data
    # Columns:
    #| time | x | vx | mass | rho | p | u
    mData    = np.loadtxt(mFile)
    return mData

def init():
    # Velocity
    aV.set_data([],[])
    # Pressure
    aP.set_data([],[])
    # Density
    aD.set_data([],[])
    # Internal Energy
    aU.set_data([],[])
    # Simulation Time
    tText.set_text('Time = 0.0')
    return aV, aP, aD, aU, tText

def animate(i):
    beg = 400*i
    end = 400*(i+1)
    t = mD[beg,0]
    x = mD[beg:end,1]
    v = mD[beg:end,2]
    d = mD[beg:end,4]
    p = mD[beg:end,5]
    u = mD[beg:end,6]
    s = 'Time = %.3f s' % t
    tText.set_text( s )
    aV.set_data(x,v)
    aP.set_data(x,p)
    aD.set_data(x,d)
    aU.set_data(x,u)
    return aV, aP, aD, aU, tText



# MAKE A MOVIE !
mD = getData()
nFrm = int(mD[:,1].size/400)
fig, axs = plt.subplots(2,2,sharex=True,constrained_layout=True)
fig.suptitle( 'Shock Tube' )
# Velocity
axs[0,0].set_xlim(-.4,.4)
axs[0,0].set_title('Velocity')
axs[0,0].set_ylim(-.15,1.1)
axs[0,0].grid(True)
tText = axs[0,0].text(-.39, 1, 'Time = 0.0', fontweight='bold')
aV, = axs[0,0].plot([],[])
# Pressure
axs[0,1].set_ylim(-.1,1.2)
axs[0,1].set_title('Pressure')
axs[0,1].grid(True)
aP, = axs[0,1].plot([],[],'tab:red')
# Density
axs[1,0].set_ylim(0,1.2)
axs[1,0].set_title('Density')
axs[1,0].grid(True)
aD, = axs[1,0].plot([],[],'tab:purple')
# Internal Energy
axs[1,1].set_ylim(1.5,2.8)
axs[1,1].set_title('Internal Energy')
axs[1,1].grid(True)
aU, = axs[1,1].plot([],[],'tab:green')

ani = animation.FuncAnimation(fig, animate, np.arange(nFrm),
                              interval=500,blit=True,
                              init_func=init)

pwriter = animation.PillowWriter(fps=2, metadata=dict(artist='Dr. Ryan Clement'))
ani.save('../movies/sph_movie.gif',writer=pwriter)
plt.show()







