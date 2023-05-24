## Description

There is a bug in the calc_pi.f90.
The calculation on line 17 should be

(x**2 + y**2 <= 1.0)

instead of 

(x**2 + x**2 <= 1.0)

## Fixes issue

