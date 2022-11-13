## Windows File
## This file is used to implement code used to run scripts for Windows
## Codes implemented here, will run before the script starts running

import os
from windows import Core
from windows import FileSystem

def Windows():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    from windows import SplashScreen

    ## Lets check system requirements
    from system import Requirements
    
    ## Start App for Windows
    from windows import WindowsApp