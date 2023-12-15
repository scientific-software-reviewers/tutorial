! module for league simulation routines
module league_simulator

implicit none

integer :: max_goals = 5

private

public :: simulate_match, sort_teams, max_goals

contains

! simulates a match between two teams
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
    goals1 = floor(max_goals*g1) 
    goals2 = floor(max_goals*g2)
    
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

! sorts an array of teams by the points in array points
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

! prints out resuts from the league
subroutine print_results(team_names, points)
    implicit none
    character(len=20), intent(in) :: team_names(:)
    integer, intent(in) :: points(:)
    integer :: i

    
! prints out resuts from the league
    print *, "Football League Results:"
    print *, "------------------------"
    do i = 1, size(team_names)
        print *, team_names(i), ": ", points(i), " points"
    end do
end subroutine print_results

end module league_simulator
