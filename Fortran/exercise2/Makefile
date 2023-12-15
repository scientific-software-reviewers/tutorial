FC=gfortran #fortran compiler
FFLAGS=-O2
SRC=league_sim_mod.f90 league_sim.f90
OBJ=${SRC:.f90=.o} #substitute .f90 with .o

%.o: %.f90 #wildcard rule, creation of *.o depends on *.f90
	$(FC) $(FFLAGS) -o $@ -c $<

league_sim.exe: $(OBJ)
	$(FC) $(FFLAGS) -o $@ $(OBJ) 

clean: #cleans all the old compilation files
	@rm -f *.mod *.o *.exe
