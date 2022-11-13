## Mac File
## This file is used to implement code used to run scripts for Mac
## Codes implemented here, will run before the script starts running

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
    
    ## Start App for Mac
    from mac import MacApp