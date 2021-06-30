## FileSystem
import os
import getpass

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

    # Run Functions
    CreateArch()
    CreateFiles()
    CreateBridge()

def ProjectStruct():
    ## Launcher Script
    ProjStruct = open(EnvironFolders.UserAppName, "a")
    ProjStruct.write(f'## {ProjectName} File\n')
    ProjStruct.write(f'## Here the contents will be processed to choose the best platform to go\n\n')
    ProjStruct.write(f'try:\n')
    ProjStruct.write(f'   # Imported Libraries\n')
    ProjStruct.write(f'   from sys import platform\n\n')
    ProjStruct.write(f'   # Local Libraries\n')
    ProjStruct.write(f'   from ErrorReport import ErrorList\n')
    ProjStruct.write(f'   from Linux import Linux\n')
    ProjStruct.write(f'   from Mac import Mac\n')
    ProjStruct.write(f'   from Windows import Windows\n\n')
    ProjStruct.write(f'   Platform = platform\n\n')
    ProjStruct.write(f'except:\n')
    ProjStruct.write(f'   ErrorList.ImportLib()\n\n')
    ProjStruct.write(f'def Main():\n')
    ProjStruct.write(f'   if Platform == "linux" or Platform == "linux2":\n')
    ProjStruct.write(f'      # Linux\n')
    ProjStruct.write(f'      Linux.Linux()\n\n')
    ProjStruct.write(f'   elif Platform == "darwin":\n')
    ProjStruct.write(f'      # Mac\n')
    ProjStruct.write(f'      Mac.Mac()\n\n')
    ProjStruct.write(f'   elif Platform == "win32":\n')
    ProjStruct.write(f'      # Windows\n')
    ProjStruct.write(f'      Windows.Windows()\n\n')
    ProjStruct.write(f'Main()')
    ProjStruct.close()
    
def CreateReadMe():
    ## README File
    CreateMD = open(EnvironFolders.ReadmeFile, "a")
    CreateMD.write(f'# {ProjectName}\n\n')
    CreateMD.write(f'This project was created using PyBridge\n')
    CreateMD.close()
    
def CreateExceptions():
    CreateExc = open(EnvironFolders.ErrorListFile, "a")
    CreateExc.write(f'## ErrorList File\n')
    CreateExc.write(f'## This file contains events thats raised when the program must to stop\n\n')
    CreateExc.write(f'def ImportLib():\n')
    CreateExc.write(f'   raise RuntimeError(">> Could Not Import Library: Check if the libraries are installed and run the program again.")\n\n')
    CreateExc.write(f'def FileExists():\n')
    CreateExc.write(f'   raise RuntimeError(">> The File Already Exists!")\n\n')
    CreateExc.write(f'def DirectoryExists():\n')
    CreateExc.write(f'   raise RuntimeError(">> The Directory Already Exists!")\n\n')
    CreateExc.close()

def LinuxSplash():
    ## Linux SplashScreen
    Splash = open(EnvironFolders.SplashLinux, "a")
    Splash.write(f'## SplashScreen File\n')
    Splash.write(f'## This file contains information about your project\n\n')
    Splash.write(f'from datetime import date\n')
    Splash.write(f'import getpass\n\n')
    Splash.write(f'CurrentYear = date.today().year\n')
    Splash.write(f'SoftwareName = "{ProjectName}"\n')
    Splash.write(f'Version = "1.0"\n')
    Splash.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
    Splash.write(f'print("Name:", SoftwareName)\n')
    Splash.write(f'print("Version:", Version)\n')
    Splash.write(f'print("Created By:", CopyrightName)\n\n')
    Splash.write(f'if CurrentYear == 2021:\n')
    Splash.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")\n')
    Splash.write(f'else:\n')
    Splash.write(f'   print("Copyright © 2021 -", CurrentYear, "|", CopyrightName, "All rights reserved.")\n\n')
    Splash.write(f'print("="*80)\n')
    Splash.write("print(f'[{SoftwareName} for Linux] - Running...')\n")
    Splash.write(f'print("="*80)\n')
    Splash.close()

def CreateLinuxFile():
    ## Linux File
    LinuxFile = open(EnvironFolders.LinuxFile, "a")
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
    LinuxAppFile = open(EnvironFolders.LinuxAppFile, "a")
    LinuxAppFile.write(f'## LinuxApp File\n')
    LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
    LinuxAppFile.write(f'def Main():\n')
    LinuxAppFile.write(f'   print("Hello World!")\n\n')
    LinuxAppFile.write(f'Main()\n')
    LinuxAppFile.close()
    
def MacSplash():
    ## Mac SplashScreen
    Splash = open(EnvironFolders.SplashMac, "a")
    Splash.write(f'## SplashScreen File\n')
    Splash.write(f'## This file contains information about your project\n\n')
    Splash.write(f'from datetime import date\n')
    Splash.write(f'import getpass\n\n')
    Splash.write(f'CurrentYear = date.today().year\n')
    Splash.write(f'SoftwareName = "{ProjectName}"\n')
    Splash.write(f'Version = "1.0"\n')
    Splash.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
    Splash.write(f'print("Name:", SoftwareName)\n')
    Splash.write(f'print("Version:", Version)\n')
    Splash.write(f'print("Created By:", CopyrightName)\n\n')
    Splash.write(f'if CurrentYear == 2021:\n')
    Splash.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")\n')
    Splash.write(f'else:\n')
    Splash.write(f'   print("Copyright © 2021 -", CurrentYear, "|", CopyrightName, "All rights reserved.")\n\n')
    Splash.write(f'print("="*80)\n')
    Splash.write("print(f'[{SoftwareName} for Mac] - Running...')\n")
    Splash.write(f'print("="*80)\n')
    Splash.close()

def CreateMacFile():
    ## Mac File
    MacFile = open(EnvironFolders.MacFile, "a")
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
    MacAppFile = open(EnvironFolders.MacAppFile, "a")
    MacAppFile.write(f'## MacApp File\n')
    MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
    MacAppFile.write(f'def Main():\n')
    MacAppFile.write(f'   print("Hello World!")\n\n')
    MacAppFile.write(f'Main()\n')
    MacAppFile.close()
    
def WindowsSplash():
    ## Windows SplashScreen
    Splash = open(EnvironFolders.SplashWindows, "a")
    Splash.write(f'## SplashScreen File\n')
    Splash.write(f'## This file contains information about your project\n\n')
    Splash.write(f'from datetime import date\n')
    Splash.write(f'import getpass\n\n')
    Splash.write(f'CurrentYear = date.today().year\n')
    Splash.write(f'SoftwareName = "{ProjectName}"\n')
    Splash.write(f'Version = "1.0"\n')
    Splash.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
    Splash.write(f'print("Name:", SoftwareName)\n')
    Splash.write(f'print("Version:", Version)\n')
    Splash.write(f'print("Created By:", CopyrightName)\n\n')
    Splash.write(f'if CurrentYear == 2021:\n')
    Splash.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")\n')
    Splash.write(f'else:\n')
    Splash.write(f'   print("Copyright © 2021 -", CurrentYear, "|", CopyrightName, "All rights reserved.")\n\n')
    Splash.write(f'print("="*80)\n')
    Splash.write("print(f'[{SoftwareName} for Windows] - Running...')\n")
    Splash.write(f'print("="*80)\n')
    Splash.close()

def CreateWindowsFile():
    ## Windows File
    WindowsFile = open(EnvironFolders.WindowsFile, "a")
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
    WindowsAppFile = open(EnvironFolders.WindowsAppFile, "a")
    WindowsAppFile.write(f'## WindowsApp File\n')
    WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
    WindowsAppFile.write(f'def Main():\n')
    WindowsAppFile.write(f'   print("Hello World!")\n\n') 
    WindowsAppFile.write(f'Main()\n')
    WindowsAppFile.close()

def CreateBridge():
    ## Project Structure
    print(">> Creating Bridge...")
    ProjectStruct()
    print()

    ## Reports Module
    print(">> Creating ErrorReports Module...")
    CreateExceptions()
    print()

    ## Readme File
    print(">> Creating Readme File...")
    CreateReadMe()
    print()
    
    ## Linux Modules
    print(">> Creating Linux Modules...")
    print("> Creating SplashScreen...")
    LinuxSplash()
    print("> Creating Linux File...")
    CreateLinuxFile()
    print("> Creating LinuxApp File...")
    CreateLinuxAppFile()
    print()

    ## macOS Modules
    print(">> Creating macOS Modules...")
    print("> Creating SplashScreen...")
    MacSplash()
    print("> Creating Mac File...")
    CreateMacFile()
    print("> Creating MacApp File...")
    CreateMacAppFile()
    print()

    ## Windows Modules
    print(">> Creating Windows Modules...")
    print("> Creating SplashScreen...")
    WindowsSplash()
    print("> Creating Windows File...")
    CreateWindowsFile()
    print("> Creating WindowsApp File...")
    CreateWindowsAppFile()
