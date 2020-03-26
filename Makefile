##################################################
#
#  SIMPLE Makefile to build the Fortran SPH code
#  from the book Smoothed Particle Hydrodynamics
#  a meshfree particle method by Liu & Liu (2003)
#  with the GNU compiler on Linux (gfortran). 
#  Again, a SIMPLE Makefile.
#
#  Author: Ryan Clement
#          scisoft@outlook.com
#
#  Date:   March 2020
#
##################################################
.SUFFIXES : .o .f90 .f

SRCDIR  = source
BLDDIR  = build

# Compiler
FC      = gfortran
FCFLAGS = -I.

# Program
MAIN    = sph.x

# Source Files
FSRCS   = art_heat.f art_visc.f av_vel.f density.f direct_find.f eos.f 
FSRCS  += external_force.f grid_geom.f hsml.f init_grid.f input.f      
FSRCS  += internal_force.f kernel.f link_list.f output.f single_step.f 
FSRCS  += sph.f time_integration.f virt_part.f viscosity.f     

F90SRCS =  time_elapsed.f90 time_print.f90
#$(info $(FSRCS))   # Uncomment to print *.f files.
#$(info $(F90SRCS)) # Uncomment to print *.f90 files.

# Include Files
FINCS   = $(SRCDIR)/param.inc

# Object Files
FOBJS   = $(FSRCS:.f=.o) 
F90OBJS = $(F90SRCS:.f90=.o)
FOBJS  := $(addprefix $(BLDDIR)/, $(FOBJS))
F90OBJS:= $(addprefix $(BLDDIR)/, $(F90OBJS))
#$(info $(FOBJS))   # Uncomment to print *.f files.
#$(info $(F90OBJS)) # Uncomment to print *.f90 files.

# Add dir to srcs
#FSRCS  := $(addprefix $(SRCDIR)/,$(FSRCS))

.PHONY: all
all: $(FOBJS) $(F90OBJS) $(FINCS)
	@echo Compiled all files...
	$(FC) $(FCFLAGS) -o $(MAIN) $(FOBJS) $(F90OBJS) 

# Compile Rules
$(FOBJS) : $(BLDDIR)/%.o : $(SRCDIR)/%.f
	$(FC) $(FCFLAGS) -c $< -o $@ 

$(F90OBJS) : $(BLDDIR)/%.o : $(SRCDIR)/%.f90
	$(FC) $(FCFLAGS) -c $< -o $@ 

.PHONY: clean
clean:
	rm -f $(BLDDIR)/*.o
	rm -f sph.x

