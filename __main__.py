## PyBridge File
## This file is used to first run your application
## Here the contents will be processed to choose the best platform to go

## Native Libraries
from sys import platform

## Linux
if platform == "linux" or platform == "linux2":
    from linux import Linux
    Linux.Linux()

## Mac    
elif platform == "darwin":
    from mac import Mac
    Mac.Mac()
    
## Windows
elif platform == "win32" or platform == "win64":
    from windows import Windows
    Windows.Windows()