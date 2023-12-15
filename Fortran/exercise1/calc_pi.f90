program calc_pi
use iso_fortran_env
implicit none

integer, parameter :: num_samples = 1000000  ! Number of random samples

real(real64) :: x, y
real(real64) :: pi_approx
integer :: i, count_inside_circle

count_inside_circle = 0

! Loop through random points and check if they fall inside the unit circle
do i = 1, num_samples
    call random_number(x)
    call random_number(y)
    
    if (x**2 + y**2 <= 1.0) then
        count_inside_circle = count_inside_circle + 1
    end if
end do

! Approximate pi value
pi_approx = 4.0 * real(count_inside_circle) / real(num_samples)

print *, "Approximated value of pi:", pi_approx
    
end program calc_pi

