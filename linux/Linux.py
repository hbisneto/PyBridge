"""
Linux.py

- This file is used to implement code used to run scripts for Linux
- Codes implemented here, will run before the main script starts running
"""
## Linux File
## This file is used to implement code used to run scripts for Linux
## Codes implemented here, will run before the main script starts running

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

    ### You just need to run ONCE: Be sure you commented this code after first run
    Requirements.InstallDependencies()
    ### You just need to run ONCE: Be sure you commented this code after first run
    
    ## Start App for Linux
    from linux import LinuxApp