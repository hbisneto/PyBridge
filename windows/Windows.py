"""
Windows.py

- This file is used to implement code used to run scripts for Windows
- Codes implemented here, will run before the main script starts running
"""
## Windows File
## This file is used to implement code used to run scripts for Windows
## Codes implemented here, will run before the script starts running

import os
from windows import Core
from windows import SplashScreen
from system import Requirements
from windows import FileSystem
from windows import WindowsApp

def Windows():
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
    WindowsApp.Run()