## Linux File
## This file is used to implement code used to run scripts for Linux
## Codes implemented here, will run before the script starts running

import os
from linux import Core
from linux import FileSystem

def Linux():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    from linux import SplashScreen

    ## Lets check system requirements
    from system import Requirements

    ## Start App for Linux
    from linux import LinuxApp