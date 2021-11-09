## PyBridge File
## This file is used to first run your application
## Here the contents will be processed to choose the best platform to go

try:
    ## Imported Libraries
    from sys import platform

    ## Local Libraries
    from ErrorReport import ErrorList

except:
    Separator = "="*80
    Message = ">> Couldn`t Import Libraries:\n>> Check if the libraries are installed and run the program again."
    raise RuntimeError("\n\n\n" + Separator + "\n" + Message + "\n" + Separator)

def Main():
    Platform = platform
    
    ## Linux
    if Platform == "linux" or Platform == "linux2":
        from Linux import Linux
        Linux.Linux()

    ## Mac    
    elif Platform == "darwin":
        from Mac import Mac
        Mac.Mac()
        
    ## Windows
    elif Platform == "win32" or Platform == "win64":
        from Windows import Windows
        Windows.Windows()

Main()
