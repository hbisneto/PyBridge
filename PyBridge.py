## PyBridge File
## This file is used to first run your application
## Here the contents will be processed to choose the best platform to go

try:
    ## Imported Libraries
    from sys import platform

    ## Local Libraries
    from ErrorReport import ErrorList
    from Linux import Linux
    from Mac import Mac
    from Windows import Windows

    Platform = platform
    
except:
    ErrorList.ImportLib()

def Main():
    ## Linux
    if Platform == "linux" or Platform == "linux2":
        Linux.Linux()

    ## Mac    
    elif Platform == "darwin":
        Mac.Mac()
        
    ## Windows
    elif Platform == "win32":
        Windows.Windows()

Main()

