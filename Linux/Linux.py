## Linux File
## This file is used to implement code used to run scripts for Linux
## Codes implemented here, will run before the script starts running.

import os
from Linux import Core
from Linux import FileSystem

def Linux():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    from Linux import SplashScreen

    ## Lets check system requirements
    from ErrorReport import SystemRequirements

    ## Start App for Linux
    from Linux import LinuxApp
