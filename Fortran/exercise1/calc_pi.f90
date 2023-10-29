program calc_pi

use ISO_FORTRAN_ENV

implicit none



double precision     :: step, x, s, pi
integer(kind=int64)  :: num_steps, i

num_steps= 500000
s = 0d0
step = 1.0d0 / num_steps

do i = 1, num_steps
   x = (i - 0.5d0) * step
   s = s + 4.0d0 / (1.0d0 + x*x)
end do

pi = s * step

print*, 'Calculated value of pi = ', pi

end program calc_pi
