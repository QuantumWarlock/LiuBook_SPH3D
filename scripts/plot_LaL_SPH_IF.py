# -*- coding: utf-8 -*-
"""
Purpose: This script will plot the INITIAL (0.0 seconds)
         and FINAL (0.2 seconds) outputs from the Liu & Liu SPH
         FORTRAN code for the shock tube simulation.

Created: Mar 2020

@author: Ryan Clement
         scisoft@outlook.com
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Set FIGURE to 8 inches by 8 inches
mpl.rcParams['figure.figsize'] = [8.0, 8.0]


def getData():
    # Initial Condition Files
    fileI1 = '../data/ini_xv.dat'
    fileI2 = '../data/ini_state.dat'
    fileI3 = '../data/ini_other.dat'

    # Final Result Files
    fileF1 = '../data/f_xv.dat'
    fileF2 = '../data/f_state.dat'
    fileF3 = '../data/f_other.dat'

    # Load Data
    xvID    = np.loadtxt(fileI1)
    stateID = np.loadtxt(fileI2)
    otherID = np.loadtxt(fileI3)
    xvFD    = np.loadtxt(fileF1)
    stateFD = np.loadtxt(fileF2)
    otherFD = np.loadtxt(fileF3)

    return xvID, stateID, otherID, xvFD, stateFD, otherFD


def plotData(x,yV,yP,yD,yIE,t):
    fig, axs = plt.subplots(2,2,sharex=True,constrained_layout=True)
    fig.suptitle('Time = '+str(t)+' s')
    # Velocity
    axs[0,0].plot(x,yV)
    axs[0,0].set_xlim(-.4,.4)
    axs[0,0].set_ylim(-.1,1.1)
    axs[0,0].set_title('Velocity')
    axs[0,0].grid(True)
    # Pressure
    axs[0,1].plot(x,yP,'tab:red')
    axs[0,1].set_ylim(-.1,1.2)
    axs[0,1].set_title('Pressure')
    axs[0,1].grid(True)
    # Density
    axs[1,0].plot(x,yD,'tab:purple')
    axs[1,0].set_ylim(0,1.2)
    axs[1,0].set_title('Density')
    axs[1,0].grid(True)
    # Internal Energy
    axs[1,1].plot(x,yIE,'tab:green')
    axs[1,1].set_ylim(1.5,2.8)
    axs[1,1].set_title('Internal Energy')
    axs[1,1].grid(True)


if __name__ == '__main__':
    xvID, stateID, otherID, xvFD, stateFD, otherFD = getData()
    # Initial
    xi = xvID[:,1]
    yiV = xvID[:,2]
    yiP = stateID[:,3]
    yiD = stateID[:,2]
    yiIE = stateID[:,4]
    plotData(xi,yiV,yiP,yiD,yiIE,0.0)
    # Final
    xf = xvFD[:,1]
    yfV = xvFD[:,2]
    yfP = stateFD[:,3]
    yfD = stateFD[:,2]
    yfIE = stateFD[:,4]
    plotData(xf,yfV,yfP,yfD,yfIE,0.2)

    plt.show()
