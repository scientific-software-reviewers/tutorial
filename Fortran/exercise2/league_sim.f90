program football_league_simulator
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

subroutine simulate_match(team1, team2, points)
    implicit none
    integer, intent(in) :: team1, team2
    integer, intent(inout) :: points(:)
    
    integer :: goals1, goals2
    real :: g1, g2        

    call random_seed()

    ! Simulate goals for each team (max 5 goals)
    call random_number(g1)
    call random_number(g2)
    goals1 = floor(6*g1) 
    goals2 = floor(6*g2)
    
    ! Update points based on match result
    if (goals1 > goals2) then
        points(team1) = points(team1) + 3   ! Team 1 wins
    else if (goals2 > goals1) then
        points(team2) = points(team2) + 3   ! Team 2 wins
    else
        points(team1) = points(team1) + 1   ! Draw, each team gets 1 point
        points(team2) = points(team2) + 1
    end if
   
end subroutine simulate_match

subroutine sort_teams(team_names, points)
    implicit none
    character(len=20), intent(inout) :: team_names(:)
    integer, intent(inout) :: points(:)
    integer :: i, j
    integer :: tempPoints
    character(len=20) :: tempName
    
    do i = 1, size(team_names) - 1
        do j = 1, size(team_names) - i
            if (points(j) < points(j + 1)) then
                ! Swap points
                tempPoints = points(j)
                points(j) = points(j + 1)
                points(j + 1) = tempPoints
                
                ! Swap team names accordingly
                tempName = team_names(j)
                team_names(j) = team_names(j + 1)
                team_names(j + 1) = tempName
            end if
        end do
    end do
end subroutine sort_teams



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
