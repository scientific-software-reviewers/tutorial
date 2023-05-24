## Fortran Exercise 2: Refactoring 

A team member (Betty) has been working on a project to simulate
a football league over a season. Betty's code is all in one 
program in a single file, [league_sim.f90](REPO_URL/Fortran/exercise2/league_sim.f90).
However, Betty would now like to use the routines contained in the main program 
in several of their other programs.

Betty created a module to enable the routines to be used by other programs and
submitted their changes in a pull request. They'd like you to take a look at their code 
and offer suggestions on how to improve it.

Take a look at the pull request:

* What would make the pull request easier to review?
* What would improve the pull request? Add a comment.
* Are the comments up to date, necessary, helpful? 
* Would you remove some of these comments? Add suggestions for which comments to remove and/or change.
* Which module variables and routines should be public? 
* Add a suggestion for which variables/routines to make private to the module.
* Have any bugs been introduced during the code refactoring?
