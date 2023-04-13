"""
Mac.py

- This file is used to implement code used to run scripts for Mac
- Codes implemented here, will run before the main script starts running
"""
## Mac File
## This file is used to implement code used to run scripts for Mac
## Codes implemented here, will run before the main script starts running

import os
from mac import Core
from mac import FileSystem

def Mac():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    from mac import SplashScreen

    ## Lets check system requirements
    from system import Requirements

    ### You just need to run ONCE: Be sure you commented this code after first run
    Requirements.InstallDependencies()
    ### You just need to run ONCE: Be sure you commented this code after first run
    
    ## Start App for Mac
    from mac import MacApp