program football_league_simulator

    use league_simulator

    implicit none
    
    integer, parameter :: num_teams = 5
    integer :: points(num_teams)
    character(len=20) :: team_names(num_teams) = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    integer :: i, j
    
    ! Initialize points
    points = 0
    ! Simulate matches and update points
    do i = 1, num_teams
        do j = i+1, num_teams
            call simulate_match(i, j, points)
        end do
    end do
   
    call sort_teams(team_names, points)
 
    ! Print results
    call print_results(team_names, points)

contains

subroutine print_results(team_names, points)
    implicit none
    character(len=20), intent(in) :: team_names(:)
    integer, intent(in) :: points(:)
    integer :: i

    
    print *, "Football League Results:"
    print *, "------------------------"
    do i = 1, size(team_names)
        print *, team_names(i), ": ", points(i), " points"
    end do
end subroutine print_results

    
end program football_league_simulator
