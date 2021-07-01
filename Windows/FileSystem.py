## FileSystem

import codecs
import getpass
import os

ProjectName = str()
FolderLocation = str()

def CreateArch():
    os.mkdir(EnvironFolders.ErrorReportPath)
    os.mkdir(EnvironFolders.LinuxPath)
    os.mkdir(EnvironFolders.MacPath)
    os.mkdir(EnvironFolders.WindowsPath)

def CreateFiles():
    ## Environment Files
    UserAppName = open(EnvironFolders.UserAppName, "w")
    ReadmeFile = open(EnvironFolders.ReadmeFile, "w")
    ErrorListFile = open(EnvironFolders.ErrorListFile, "w")
    
    ## Linux
    SplashLinux = open(EnvironFolders.SplashLinux, "w")
    LinuxFile = open(EnvironFolders.LinuxFile, "w")
    LinuxAppFile = open(EnvironFolders.LinuxAppFile, "w")

    ## Mac
    SplashMac = open(EnvironFolders.SplashMac, "w")
    MacFile = open(EnvironFolders.MacFile, "w")
    MacAppFile = open(EnvironFolders.MacAppFile, "w")

    ## Windows
    SplashWindows = open(EnvironFolders.SplashWindows, "w")
    WindowsFile = open(EnvironFolders.WindowsFile, "w")
    WindowsAppFile = open(EnvironFolders.WindowsAppFile, "w")

def EnvironFolders():
    ## Environment Folders
    EnvironFolders.ErrorReportPath = f'{FolderLocation}ErrorReport/'
    EnvironFolders.LinuxPath = f'{FolderLocation}Linux/'
    EnvironFolders.MacPath = f'{FolderLocation}Mac/'
    EnvironFolders.WindowsPath = f'{FolderLocation}Windows/'

    ## Environment Files
    EnvironFolders.UserAppName = f'{FolderLocation}{ProjectName}.py'
    EnvironFolders.ReadmeFile = f'{FolderLocation}README.md'
    EnvironFolders.ErrorListFile = f'{EnvironFolders.ErrorReportPath}ErrorList.py'
    
    ## Linux
    EnvironFolders.SplashLinux = f'{EnvironFolders.LinuxPath}SplashScreen.py'
    EnvironFolders.LinuxFile = f'{EnvironFolders.LinuxPath}Linux.py'
    EnvironFolders.LinuxAppFile = f'{EnvironFolders.LinuxPath}LinuxApp.py'

    ## Mac
    EnvironFolders.SplashMac = f'{EnvironFolders.MacPath}SplashScreen.py'
    EnvironFolders.MacFile = f'{EnvironFolders.MacPath}Mac.py'
    EnvironFolders.MacAppFile = f'{EnvironFolders.MacPath}MacApp.py'

    ## Windows
    EnvironFolders.SplashWindows = f'{EnvironFolders.WindowsPath}SplashScreen.py'
    EnvironFolders.WindowsFile = f'{EnvironFolders.WindowsPath}Windows.py'
    EnvironFolders.WindowsAppFile = f'{EnvironFolders.WindowsPath}WindowsApp.py'

    ## Run Functions
    CreateArch()
    CreateFiles()
    CreateBridge()

def ProjectStruct():
    ## Launcher Script
    with codecs.open(EnvironFolders.UserAppName, "w", "utf-8-sig") as ProjStruct:
        ProjStruct.write(f'## {ProjectName} File\n')
        ProjStruct.write(f'## Here the contents will be processed to choose the best platform to go\n\n')
        ProjStruct.write(f'try:\n')
        ProjStruct.write(f'   ## Imported Libraries\n')
        ProjStruct.write(f'   from sys import platform\n\n')
        ProjStruct.write(f'   ## Local Libraries\n')
        ProjStruct.write(f'   from ErrorReport import ErrorList\n')
        ProjStruct.write(f'   from Linux import Linux\n')
        ProjStruct.write(f'   from Mac import Mac\n')
        ProjStruct.write(f'   from Windows import Windows\n\n')
        ProjStruct.write(f'   Platform = platform\n\n')
        ProjStruct.write(f'except:\n')
        ProjStruct.write(f'   ErrorList.ImportLib()\n\n')
        ProjStruct.write(f'def Main():\n')
        ProjStruct.write(f'   ## Linux\n')
        ProjStruct.write(f'   if Platform == "linux" or Platform == "linux2":\n')
        ProjStruct.write(f'      Linux.Linux()\n\n')
        ProjStruct.write(f'   ## Mac\n')
        ProjStruct.write(f'   elif Platform == "darwin":\n')
        ProjStruct.write(f'      Mac.Mac()\n\n')
        ProjStruct.write(f'   ## Windows\n')
        ProjStruct.write(f'   elif Platform == "win32":\n')
        ProjStruct.write(f'      Windows.Windows()\n\n')
        ProjStruct.write(f'Main()')
        ProjStruct.close()
    
def CreateReadMe():
    ## README File
    with codecs.open(EnvironFolders.ReadmeFile, "w", "utf-8-sig") as Readme:
        Readme.write(f'# {ProjectName}\n\n')
        Readme.write(f'This project was created using PyBridge\n')
        Readme.close()
    
def CreateExceptions():
    ## Exception Triggers
    with codecs.open(EnvironFolders.ErrorListFile, "w", "utf-8-sig") as Exceptions:
        Exceptions.write(f'## ErrorList File\n')
        Exceptions.write(f'## This file contains events thats raised when the program must to stop\n\n')
        Exceptions.write(f'def ImportLib():\n')
        Exceptions.write(f'   raise RuntimeError(">> Could Not Import Library: Check if the libraries are installed and run the program again.")\n\n')
        Exceptions.write(f'def FileExists():\n')
        Exceptions.write(f'   raise RuntimeError(">> The File Already Exists!")\n\n')
        Exceptions.write(f'def DirectoryExists():\n')
        Exceptions.write(f'   raise RuntimeError(">> The Directory Already Exists!")\n\n')
        Exceptions.close()

def LinuxSplash():
    ## Linux SplashScreen
    with codecs.open(EnvironFolders.SplashLinux, "w", "utf-8-sig") as SplashLinux:
        SplashLinux.write(f'## SplashScreen File\n')
        SplashLinux.write(f'## This file contains information about your project\n\n')
        SplashLinux.write(f'from datetime import date\n\n')
        SplashLinux.write(f'CurrentYear = date.today().year\n')
        SplashLinux.write(f'SoftwareName = "{ProjectName}"\n')
        SplashLinux.write(f'Version = "1.0"\n')
        SplashLinux.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
        SplashLinux.write(f'print("Name:", SoftwareName)\n')
        SplashLinux.write(f'print("Version:", Version)\n')
        SplashLinux.write(f'print("Created By:", CopyrightName)\n\n')
        SplashLinux.write(f'if CurrentYear == 2021:\n')
        SplashLinux.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")\n')
        SplashLinux.write(f'else:\n')
        SplashLinux.write(f'   print("Copyright © 2021 -", CurrentYear, "|", CopyrightName, "All rights reserved.")\n\n')
        SplashLinux.write(f'print("="*80)\n')
        SplashLinux.write("print(f'[{SoftwareName} for Linux] - Running...')\n")
        SplashLinux.write(f'print("="*80)\n')
        SplashLinux.close()

def CreateLinuxFile():
    ## Linux File
    with codecs.open(EnvironFolders.LinuxFile, "w", "utf-8-sig") as LinuxFile:
        LinuxFile.write(f'## Linux File\n')
        LinuxFile.write(f'## This file is used to implement code used to run scripts for Linux\n')
        LinuxFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        LinuxFile.write(f'def Linux():\n')
        LinuxFile.write(f'   ## NOTE: You can use this function\n')
        LinuxFile.write(f'   ## To load information before the app starts running\n\n')
        LinuxFile.write(f'   ## Lets run the SplashScreen\n')
        LinuxFile.write(f'   from Linux import SplashScreen\n\n')
        LinuxFile.write(f'   ## Start App for Linux\n')
        LinuxFile.write(f'   from Linux import LinuxApp\n\n')
        LinuxFile.close()

def CreateLinuxAppFile():
    ## LinuxApp File
    with codecs.open(EnvironFolders.LinuxAppFile, "w", "utf-8-sig") as LinuxAppFile:
        LinuxAppFile.write(f'## LinuxApp File\n')
        LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
        LinuxAppFile.write(f'def Main():\n')
        LinuxAppFile.write(f'   print("Hello World!")\n\n')
        LinuxAppFile.write(f'Main()\n')
        LinuxAppFile.close()
    
def MacSplash():
    ## Mac SplashScreen
    with codecs.open(EnvironFolders.SplashMac, "w", "utf-8-sig") as SplashMac:
        SplashMac.write(f'## SplashScreen File\n')
        SplashMac.write(f'## This file contains information about your project\n\n')
        SplashMac.write(f'from datetime import date\n\n')
        SplashMac.write(f'CurrentYear = date.today().year\n')
        SplashMac.write(f'SoftwareName = "{ProjectName}"\n')
        SplashMac.write(f'Version = "1.0"\n')
        SplashMac.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
        SplashMac.write(f'print("Name:", SoftwareName)\n')
        SplashMac.write(f'print("Version:", Version)\n')
        SplashMac.write(f'print("Created By:", CopyrightName)\n\n')
        SplashMac.write(f'if CurrentYear == 2021:\n')
        SplashMac.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")\n')
        SplashMac.write(f'else:\n')
        SplashMac.write(f'   print("Copyright © 2021 -", CurrentYear, "|", CopyrightName, "All rights reserved.")\n\n')
        SplashMac.write(f'print("="*80)\n')
        SplashMac.write("print(f'[{SoftwareName} for Mac] - Running...')\n")
        SplashMac.write(f'print("="*80)\n')
        SplashMac.close()

def CreateMacFile():
    ## Mac File
    with codecs.open(EnvironFolders.MacFile, "w", "utf-8-sig") as MacFile:
        MacFile.write(f'## Mac File\n')
        MacFile.write(f'## This file is used to implement code used to run scripts for Mac\n')
        MacFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        MacFile.write(f'def Mac():\n')
        MacFile.write(f'   ## NOTE: You can use this function\n')
        MacFile.write(f'   ## To load information before the app starts running\n\n')
        MacFile.write(f'   ## Lets run the SplashScreen\n')
        MacFile.write(f'   from Mac import SplashScreen\n\n')
        MacFile.write(f'   ## Start App for Mac\n')
        MacFile.write(f'   from Mac import MacApp\n\n')
        MacFile.close()

def CreateMacAppFile():
    ## MacApp File
    with codecs.open(EnvironFolders.MacAppFile, "w", "utf-8-sig") as MacAppFile:
        MacAppFile.write(f'## MacApp File\n')
        MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
        MacAppFile.write(f'def Main():\n')
        MacAppFile.write(f'   print("Hello World!")\n\n')
        MacAppFile.write(f'Main()\n')
        MacAppFile.close()
    
def WindowsSplash():
    ## Windows SplashScreen
    with codecs.open(EnvironFolders.SplashWindows, "w", "utf-8-sig") as SplashWindows:
        SplashWindows.write(f'## SplashScreen File\n')
        SplashWindows.write(f'## This file contains information about your project\n\n')
        SplashWindows.write(f'from datetime import date\n\n')
        SplashWindows.write(f'CurrentYear = date.today().year\n')
        SplashWindows.write(f'SoftwareName = "{ProjectName}"\n')
        SplashWindows.write(f'Version = "1.0"\n')
        SplashWindows.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
        SplashWindows.write(f'print("Name:", SoftwareName)\n')
        SplashWindows.write(f'print("Version:", Version)\n')
        SplashWindows.write(f'print("Created By:", CopyrightName)\n\n')
        SplashWindows.write(f'if CurrentYear == 2021:\n')
        SplashWindows.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")\n')
        SplashWindows.write(f'else:\n')
        SplashWindows.write(f'   print("Copyright © 2021 -", CurrentYear, "|", CopyrightName, "All rights reserved.")\n\n')
        SplashWindows.write(f'print("="*80)\n')
        SplashWindows.write("print(f'[{SoftwareName} for Windows] - Running...')\n")
        SplashWindows.write(f'print("="*80)\n')
        SplashWindows.close()

def CreateWindowsFile():
    ## Windows File
    with codecs.open(EnvironFolders.WindowsFile, "w", "utf-8-sig") as WindowsFile:
        WindowsFile.write(f'## Windows File\n')
        WindowsFile.write(f'## This file is used to implement code used to run scripts for Windows\n')
        WindowsFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        WindowsFile.write(f'def Windows():\n')
        WindowsFile.write(f'   ## NOTE: You can use this function\n')
        WindowsFile.write(f'   ## To load information before the app starts running\n\n')
        WindowsFile.write(f'   ## Lets run the SplashScreen\n')
        WindowsFile.write(f'   from Windows import SplashScreen\n\n')
        WindowsFile.write(f'   ## Start App for Windows\n')
        WindowsFile.write(f'   from Windows import WindowsApp\n\n')
        WindowsFile.close()

def CreateWindowsAppFile():
    ## WindowsApp File
    with codecs.open(EnvironFolders.WindowsAppFile, "w", "utf-8-sig") as WindowsAppFile:
        WindowsAppFile.write(f'## WindowsApp File\n')
        WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
        WindowsAppFile.write(f'def Main():\n')
        WindowsAppFile.write(f'   print("Hello World!")\n\n') 
        WindowsAppFile.write(f'Main()\n')
        WindowsAppFile.close()

def CreateBridge():
    ## Project Structure
    print("="*80)
    print(">> Project Structure <<")
    print("="*80)
    #print("> Creating Bridge...")
    ProjectStruct()

    ## Readme File
    print("> Creating Readme File...")
    CreateReadMe()

    ## Reports Module
    print("> Creating ErrorReports Module...")
    CreateExceptions()
    print("-"*80)
    print()

    ## Linux Module
    print("="*80)
    print(">> Creating Linux Modules <<")
    print("="*80)
    print("> Creating Linux File...")
    CreateLinuxFile()
    print("> Creating LinuxApp File...")
    CreateLinuxAppFile()
    print("> Creating SplashScreen...")
    LinuxSplash()
    print("-"*80)
    print()

    ## macOS Modules
    print("="*80)
    print(">> Creating Mac Modules <<")
    print("="*80)
    print("> Creating Mac File...")
    CreateMacFile()
    print("> Creating MacApp File...")
    CreateMacAppFile()
    print("> Creating SplashScreen...")
    MacSplash()
    print("-"*80)
    print()

    ## Windows Modules
    print("="*80)
    print(">> Creating Windows Modules <<")
    print("="*80)
    print("> Creating Windows File...")
    CreateWindowsFile()
    print("> Creating WindowsApp File...")
    CreateWindowsAppFile()
    print("> Creating SplashScreen...")
    WindowsSplash()
    print("-"*80)
    print()
