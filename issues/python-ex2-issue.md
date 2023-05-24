## Python Exercise 2: Calculating experiment time windows

A lab group is using a python script to calculate the number of hour-long 
experiments between an initial and final time. 

Some background: The goal is to run the NSF NCAR space weather model 
[TIEGCM](https://www.hao.ucar.edu/modeling/tgcm/tie.php) and stop every
hour to update the model using observations.
Each experiment uses observations from +/- 30 minutes from when the model
is stopped. This +/- 30 minutes is known as the experiment window.

The class [time_window.py](REPO_URL/python/exercise2/time_window.py) is the initialized 
with the start time, the final time, and the delta (the duration of a single 
experiment). From these input the number of experiments needed, and the start 
and stop for both the model and the window are calculated.
The script [run_test.py](REPO_URL/python/exercise2/run_test.py) provided by the lab group
can be used to demonstrate the bug: run_test.py initializes the class and prints
the window and model times. 

The issue: For one set of experiments, the delta was accidentally entered 
as negative. The number of windows was calculated correctly, but the times 
for each of the windows were incorrect.

The lab group want to add some error checking to the python script to prevent
this error happening again. 

Take a look at [time_window.py](REPO_URL/python/exercise2/time_window.py):

* Where would you put the error check?
* Are there other error checks that you think should be included in the script?

Take a look at the pull request:

* Does the pull request address the issue?
* Are there any unnecessary or incorrect changes?
* What would make the pull request easier to review?
* What would improve the pull request? Add a suggestion.
