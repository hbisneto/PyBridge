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
from linux import SplashScreen
from system import Requirements
from linux import FileSystem
from linux import LinuxApp

def Linux():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    SplashScreen.Show()

    ## Lets check system requirements
    Requirements.CheckVersion()

    ### You just need to run ONCE: Be sure you commented this code after first run
    Requirements.InstallDependencies()
    ### You just need to run ONCE: Be sure you commented this code after first run

    ### Verify environment folders
    FileSystem.VerifyFolders()
    
    ## Start App for Mac
    LinuxApp.Run()