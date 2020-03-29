# SPH3D
3D Smoothed Particle Hydrodynamics FORTRAN code. Adapted from source in __Smoothed Particle Hydrodynamics a meshfree particle method__ by G.R. Liu and M.B. Liu (2003). To aid building and analysis of results, a make system and several python scripts were created.

## Linux:

**Build:**
```bash
>make
```
This command will execute the Makefile script. This script will create, if they don't already exist, the build, movie, and data directories. It will compile the FORTRAN, i.e. *.f and *.f90, files in the source directory and the link them to create the executable __sph.x__.

**Clean:**

There are 3 levels: clean, cleaner, sanitize. The commands to use them and what they do are as follows:
```bash
>make clean
```
This will delete the executable and the object files in the build directory.

```bash
>make cleaner
```
This will do __clean__ plus delete the data files in the data directory.

```bash
>make sanitize
```
This will do __cleaner__ plus remove the build, movie and data directories.

**Execute:**
```bash
>./sph.x
```

## Scripts:
Currently, the scripts are focused on the 1D shock tube simulation. While they are specific to that problem, they do provide a starting point for adaptation and generalization to plot outputs to match the full capability of the SPH code.

### plot_LaL_SPH_IF.py
**Execute:**
```bash
>python3 plot_LaL_SPH_IF.py
```
Plots the initial and final states of the shock tube simulation for velocity, pressure, density, and internal energy as a function of particle position.

### plot_LaL_SPH_Movie.py
**Execute:**
```bash
>python3 plot_LaL_SPH_Movie.py
```
Creates an animated __gif__ file and then plots movie of the time evolution of the shock tube simulation for velocity, pressure, density, and internal energy as a function of particle position.
