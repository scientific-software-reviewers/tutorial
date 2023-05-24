FC=gfortran #fortran compiler
FFLAGS=-O2
SRC=calc_pi.f90
OBJ=${SRC:.f90=.o} #substitute .f90 with .o

%.o: %.f90 #wildcard rule, creation of *.o depends on *.f90
	$(FC) $(FFLAGS) -o $@ -c $<

calc_pi.exe: $(OBJ)
	$(FC) $(FFLAGS) -o $@ $(OBJ) 

clean: #cleans all the old compilation files
	@rm -f *.mod *.o *.exe
