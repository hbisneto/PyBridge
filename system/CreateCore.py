# CreateCore.py
## Creates the Core.py library for all systems automatically

## Native Libraries
from sys import platform
import os

CURRENT_DIRECTORY = os.getcwd()
LINUX_MODULE_LOCATION = ""
MAC_MODULE_LOCATION = ""
WINDOWS_MODULE_LOCATION = ""

def CreateLinuxCore():
    print("Linux Passed!")

def CreateMacCore():
    print("Mac Passed!")

def CreateWindowsCore():
    print("Windows Passed!")

## Linux
if platform == "linux" or platform == "linux2":
    print("Linux Passed!")
    # CreateLinuxCore()

## Mac    
elif platform == "darwin":
    print("Mac Passed!")
    # CreateMacCore()
    
## Windows
elif platform == "win32" or platform == "win64":
    print("Windows Passed!")
    # CreateWindowsCore()