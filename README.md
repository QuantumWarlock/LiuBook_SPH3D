# SPH3D
3D Smoothed Particle Hydrodynamics FORTRAN code. Adapted from source in __Smoothed Particle Hydrodynamics a meshfree particle method__ by G.R. Liu and M.B. Liu (2003). To aid building and analysis of results, a make system and several python scripts were created.

## Linux:

**Build:**
```bash
>make
```

**Clean**
There are 3 levels: clean, cleaner, sanitize. The commands to use them and what they do are as follows:
```bash
>make clean
```

```bash
>make cleaner
```

```bash
>make sanitize
```

**Execute:**
```bash
>./sph.x
```

## Scripts:

### plot_LaL_SPH_IF.py
**Execute:**
```bash
>python3 plot_LaL_SPH_IF.py
```

### plot_LaL_SPH_Movie.py
**Execute:**
```bash
>python3 plot_LaL_SPH_Movie.py
```
