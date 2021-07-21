## Core
## This file will process every step of file creation

import codecs
import getpass
import os
import sys

from Windows import FileSystem

PythonExtension = ".py"
LoopApp = False

MajorVersion = sys.version_info[0]
MinorVersion = sys.version_info[1]
BuildVersion = sys.version_info[2]

def Explorer():
    ProjectName = str()
    FolderLocation = str()

def VerifyFolders():
    try:
        print(">> PyBridge: Checking System...")
        os.mkdir(FileSystem.PyBridgeFolder)
        os.mkdir(FileSystem.ProjectsRepo)
        print(">> PyBridge System Files: OK!")
    except:
        print(">> PyBridge System Files: OK!")

def CreateProject():
    print()
    print("="*80)
    print(">> CREATE PROJECT")
    print("="*80)
    ProjectName = str(input(">> Project Name: "))
    print(f'>> Creating bridge to the project "{ProjectName}"...')
    print("-"*80)
    print()
    try:
        FolderLocation = f'{FileSystem.ProjectsRepo}{ProjectName}/'
        os.mkdir(FolderLocation)
        Explorer.ProjectName = ProjectName
        Explorer.FolderLocation = FolderLocation
        EnvironFolders()
        print("="*80)
        print(f'>> The bridge to the project "{ProjectName}" was created successfully!')
        print("="*80)
    except:
        print()
        print(">> Could not create your project:")
        print(f'> Check if "{ProjectName}" already exists and try again.')
        from ErrorReport import ErrorList
        ErrorList.FileExists()

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
    SystemRequirements = open(EnvironFolders.SystemRequirements, "w")
    
    ## Linux
    LinuxFS = open(EnvironFolders.LinuxFS, "w")
    LinuxFile = open(EnvironFolders.LinuxFile, "w")
    LinuxAppFile = open(EnvironFolders.LinuxAppFile, "w")
    SplashLinux = open(EnvironFolders.SplashLinux, "w")

    ## Mac
    MacFS = open(EnvironFolders.MacFS, "w")
    MacFile = open(EnvironFolders.MacFile, "w")
    MacAppFile = open(EnvironFolders.MacAppFile, "w")
    SplashMac = open(EnvironFolders.SplashMac, "w")

    ## Windows
    WindowsFS = open(EnvironFolders.WindowsFS, "w")
    WindowsFile = open(EnvironFolders.WindowsFile, "w")
    WindowsAppFile = open(EnvironFolders.WindowsAppFile, "w")
    SplashWindows = open(EnvironFolders.SplashWindows, "w")

def EnvironFolders():
    ## Environment Folders
    EnvironFolders.ErrorReportPath = f'{Explorer.FolderLocation}ErrorReport/'
    EnvironFolders.LinuxPath = f'{Explorer.FolderLocation}Linux/'
    EnvironFolders.MacPath = f'{Explorer.FolderLocation}Mac/'
    EnvironFolders.WindowsPath = f'{Explorer.FolderLocation}Windows/'

    ## Environment Files
    EnvironFolders.UserAppName = f'{Explorer.FolderLocation}{Explorer.ProjectName}.py'
    EnvironFolders.ReadmeFile = f'{Explorer.FolderLocation}README.md'
    EnvironFolders.ErrorListFile = f'{EnvironFolders.ErrorReportPath}ErrorList.py'
    EnvironFolders.SystemRequirements = f'{EnvironFolders.ErrorReportPath}SystemRequirements.py'
    
    ## Linux
    EnvironFolders.LinuxFS = f'{EnvironFolders.LinuxPath}FileSystem.py'
    EnvironFolders.LinuxFile = f'{EnvironFolders.LinuxPath}Linux.py'
    EnvironFolders.LinuxAppFile = f'{EnvironFolders.LinuxPath}LinuxApp.py'
    EnvironFolders.SplashLinux = f'{EnvironFolders.LinuxPath}SplashScreen.py'
    
    ## Mac
    EnvironFolders.MacFS = f'{EnvironFolders.MacPath}FileSystem.py'
    EnvironFolders.MacFile = f'{EnvironFolders.MacPath}Mac.py'
    EnvironFolders.MacAppFile = f'{EnvironFolders.MacPath}MacApp.py'
    EnvironFolders.SplashMac = f'{EnvironFolders.MacPath}SplashScreen.py'

    ## Windows
    EnvironFolders.WindowsFS = f'{EnvironFolders.WindowsPath}FileSystem.py'
    EnvironFolders.WindowsFile = f'{EnvironFolders.WindowsPath}Windows.py'
    EnvironFolders.WindowsAppFile = f'{EnvironFolders.WindowsPath}WindowsApp.py'
    EnvironFolders.SplashWindows = f'{EnvironFolders.WindowsPath}SplashScreen.py'

    ## Run Functions
    CreateArch()
    CreateFiles()
    CreateBridge()

def ProjectStruct():
    ## Launcher Script
    print("="*80)
    print(">> Project <<")
    print("="*80)
    with codecs.open(EnvironFolders.UserAppName, "w", "utf-8-sig") as ProjStruct:
        ProjStruct.write(f'## {Explorer.ProjectName} File\n')
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

    ## README File
    print("> Creating 'README' File...")
    with codecs.open(EnvironFolders.ReadmeFile, "w", "utf-8-sig") as Readme:
        Readme.write(f'# {Explorer.ProjectName}\n\n')
        Readme.write(f'This project was created using PyBridge\n')
        Readme.close()
    
    ## Exception Triggers
    print("> Creating ErrorReports Module...")
    with codecs.open(EnvironFolders.ErrorListFile, "w", "utf-8-sig") as Exceptions:
        Exceptions.write(f'## ErrorList File\n')
        Exceptions.write(f'## This file contains events thats raised when the program must to stop\n\n')
        Exceptions.write(f'class RequirementsCheck():\n')
        Exceptions.write(f'   def MajorVersion(self, CurrentVersion, TargetVersion, TargetMajor):\n')
        Exceptions.write("      raise Exception(f'>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')\n\n")
        Exceptions.write(f'   def MinorVersion(self, CurrentVersion, TargetVersion, TargetMinor):\n')
        Exceptions.write(f'      print("="*80)\n')
        Exceptions.write(f'      print(">> PYBRIDGE <<")\n')
        Exceptions.write(f'      print("="*80)\n')
        Exceptions.write(f'      print(">> WARNING <<")\n')
        Exceptions.write(f'      print("="*80)\n')
        Exceptions.write("      print(f'>> Your appication targets a version of Python older than the version currently installed. You may get errors during the process')\n")
        Exceptions.write(f'      print("-"*80)\n')
        Exceptions.write("      print(f'- Current Version: {CurrentVersion}')\n")
        Exceptions.write("      print(f'- Target Version: {TargetVersion}')\n")
        Exceptions.write("      print(f'>> You can change requirements in `SystemRequirements.py` on `ErrorReport` Module')\n\n")
        Exceptions.write(f'      print("-"*80)\n\n')
        Exceptions.write(f'   def BuildVersion(self, CurrentVersion, TargetVersion, BuildVer):\n')
        Exceptions.write("      raise Exception(f'>> This application only can run on Python {TargetVersion}. [Current Version: {CurrentVersion}]')\n\n")
        Exceptions.write(f'def Requirements():\n')
        Exceptions.write(f'   return RequirementsCheck()\n\n')
        Exceptions.write(f'def ImportLib():\n')
        Exceptions.write(f'   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")\n\n')
        Exceptions.write(f'def FileExists():\n')
        Exceptions.write(f'   raise RuntimeError(">> The file already exists!")\n\n')
        Exceptions.write(f'def DirectoryExists():\n')
        Exceptions.write(f'   raise RuntimeError(">> The directory already exists!")\n\n')
        Exceptions.close()

    ## System Requirements File
    print("> Creating SystemRequirements Library...")
    with codecs.open(EnvironFolders.SystemRequirements, "w", "utf-8-sig") as Requirements:
        Requirements.write(f'## SystemRequirements File\n')
        Requirements.write(f'## This file is used to check if system matches with the minimum requirements to run\n\n')
        Requirements.write(f'from ErrorReport import ErrorList\n')
        Requirements.write(f'import sys\n\n')
        Requirements.write(f'## Change "Require" to "False" to skip system check\n')
        Requirements.write(f'Require = False\n')
        Requirements.write(f'## Change "Require" to "True" to allow system check\n\n')
        Requirements.write(f'if Require == True:\n')
        Requirements.write(f'   ## Target System\n')
        Requirements.write(f'   TargetMajor = {MajorVersion}\n')
        Requirements.write(f'   TargetMinor = {MinorVersion}\n')
        Requirements.write(f'   TargetBuild = {BuildVersion}\n')
        Requirements.write("   TargetVersion = f'{TargetMajor}.{TargetMinor}.{TargetBuild}'\n")
        Requirements.write(f'   ## Target System\n\n')
        Requirements.write(f'   ## Current System\n')
        Requirements.write(f'   MajorVersion = sys.version_info[0]\n')
        Requirements.write(f'   MinorVersion = sys.version_info[1]\n')
        Requirements.write(f'   BuildVersion = sys.version_info[2]\n')
        Requirements.write("   CurrentVersion = f'{MajorVersion}.{MinorVersion}.{BuildVersion}'\n")
        Requirements.write(f'   ## Current System\n\n')
        Requirements.write(f'   ## Uncomment to see information about your system\n')
        Requirements.write("   #print(f'>> My system current version: Python {CurrentVersion}')\n")
        Requirements.write("   #print(f'>> Required version to run: Python {TargetVersion}')\n\n")
        Requirements.write(f'   if TargetVersion > CurrentVersion:\n')
        Requirements.write(f'      ErrorList.Requirements().MajorVersion(CurrentVersion, TargetVersion, TargetMajor)\n')
        Requirements.write(f'   elif TargetVersion < CurrentVersion:\n')
        Requirements.write(f'      ErrorList.Requirements().MinorVersion(CurrentVersion, TargetVersion, TargetMinor)\n\n')
        Requirements.close()

def LinuxPlat():
    print("="*80)
    print(">> Creating Linux Modules <<")
    print("="*80)
    
    ## Linux File
    print("> Creating Linux Library...")
    with codecs.open(EnvironFolders.LinuxFile, "w", "utf-8-sig") as LinuxFile:
        LinuxFile.write(f'## Linux File\n')
        LinuxFile.write(f'## This file is used to implement code used to run scripts for Linux\n')
        LinuxFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        LinuxFile.write(f'def Linux():\n')
        LinuxFile.write(f'   ## NOTE: You can use this function\n')
        LinuxFile.write(f'   ## To load information before the app starts running\n\n')
        LinuxFile.write(f'   ## Lets run the SplashScreen\n')
        LinuxFile.write(f'   from Linux import SplashScreen\n\n')
        LinuxFile.write(f'   ## Lets check system requirements\n')
        LinuxFile.write(f'   from ErrorReport import SystemRequirements\n\n')
        LinuxFile.write(f'   ## Start App for Linux\n')
        LinuxFile.write(f'   from Linux import LinuxApp\n\n')
        LinuxFile.close()
    
    ## LinuxApp File
    if LoopApp == True:
        print("> Creating LinuxApp Library...")
        with codecs.open(EnvironFolders.LinuxAppFile, "w", "utf-8-sig") as LinuxAppFile:
            LinuxAppFile.write(f'## LinuxApp File\n')
            LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')

            LinuxAppFile.write(f'from ErrorReport import ErrorList\n\n')
            LinuxAppFile.write(f'def Main():\n')
            LinuxAppFile.write(f'   while True:\n')
            LinuxAppFile.write(f'      print("="*80)\n')
            LinuxAppFile.write(f'      print(">> Options Menu<<")\n')
            LinuxAppFile.write(f'      print(">> 1. Option One")\n')
            LinuxAppFile.write(f'      print(">> 2. Option Two")\n')
            LinuxAppFile.write(f'      print(">> 3. Option Three")\n\n')

            LinuxAppFile.write(f'      try:\n')
            LinuxAppFile.write(f'         UserInput = int(input(">> Type the option number: "))\n')
            LinuxAppFile.write(f'         print("="*80)\n')
            LinuxAppFile.write(f'         if UserInput == 1:\n')
            LinuxAppFile.write(f'            print("> Option 1")\n')
            LinuxAppFile.write(f'         elif UserInput == 2:\n')
            LinuxAppFile.write(f'            print("> Option 2")\n')
            LinuxAppFile.write(f'         elif UserInput == 3:\n')
            LinuxAppFile.write(f'            print("> Option 3")\n')
            LinuxAppFile.write(f'         else:\n')
            LinuxAppFile.write(f'            print(">> This option is unavailable at this time")\n')
            LinuxAppFile.write(f'      except:\n')
            LinuxAppFile.write(f'         print("-"*80)\n')
            LinuxAppFile.write(f'         print(">> This option is unavailable at this time")\n')
            LinuxAppFile.write(f'         print("-"*80)\n\n')
                 
            LinuxAppFile.write(f'Main()\n')
            LinuxAppFile.close()
    else:
        print("> Creating LinuxApp Library...")
        with codecs.open(EnvironFolders.LinuxAppFile, "w", "utf-8-sig") as LinuxAppFile:
            LinuxAppFile.write(f'## LinuxApp File\n')
            LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
            LinuxAppFile.write(f'from ErrorReport import ErrorList\n\n')
            LinuxAppFile.write(f'def Main():\n')
            LinuxAppFile.write(f'   print("Hello World!")\n\n')
            LinuxAppFile.write(f'Main()\n')
            LinuxAppFile.close()
    
    ## Linux SplashScreen
    print("> Creating SplashScreen...")
    with codecs.open(EnvironFolders.SplashLinux, "w", "utf-8-sig") as SplashLinux:
        SplashLinux.write(f'## SplashScreen File\n')
        SplashLinux.write(f'## This file contains information about your project\n\n')
        SplashLinux.write(f'from datetime import date\n\n')
        SplashLinux.write(f'CurrentYear = date.today().year\n')
        SplashLinux.write(f'SoftwareName = "{Explorer.ProjectName}"\n')
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
    
    ## Linux FileSystem
    print("> Creating Linux FileSystem Library...")
    with codecs.open(EnvironFolders.LinuxFS, "w", "utf-8-sig") as LinuxFS:
        Linux = "User = f'/home/{os.environ"
        FileSystem = '["USER"]}/'
        SUser = f"{Linux}{FileSystem}'"
        LinuxFS.write(f'## FileSystem\n')
        LinuxFS.write(f'## This file contains some default directories of your system\n')
        LinuxFS.write(f'import os\n\n')
        LinuxFS.write(f'## Special Directories\n')
        LinuxFS.write(f'CurrentPath = os.getcwd()\n')
        LinuxFS.write(f'{SUser}\n')
        LinuxFS.write("Desktop = f'{User}Desktop/'\n")
        LinuxFS.write("Documents = f'{User}Documents/'\n")
        LinuxFS.write("Downloads = f'{User}Downloads/'\n")
        LinuxFS.write("Music = f'{User}Music/'\n\n")
        LinuxFS.close()

def MacPlat():
    print("="*80)
    print(">> Creating Mac Modules <<")
    print("="*80)

    ## Mac File
    print("> Creating Mac Library...")
    with codecs.open(EnvironFolders.MacFile, "w", "utf-8-sig") as MacFile:
        MacFile.write(f'## Mac File\n')
        MacFile.write(f'## This file is used to implement code used to run scripts for Mac\n')
        MacFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        MacFile.write(f'def Mac():\n')
        MacFile.write(f'   ## NOTE: You can use this function\n')
        MacFile.write(f'   ## To load information before the app starts running\n\n')
        MacFile.write(f'   ## Lets run the SplashScreen\n')
        MacFile.write(f'   from Mac import SplashScreen\n\n')
        MacFile.write(f'   ## Lets check system requirements\n')
        MacFile.write(f'   from ErrorReport import SystemRequirements\n\n')
        MacFile.write(f'   ## Start App for Mac\n')
        MacFile.write(f'   from Mac import MacApp\n\n')
        MacFile.close()

    ## MacApp File
    if LoopApp == True:
        print("> Creating MacApp Library...")
        with codecs.open(EnvironFolders.MacAppFile, "w", "utf-8-sig") as MacAppFile:
            MacAppFile.write(f'## MacApp File\n')
            MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
            MacAppFile.write(f'from ErrorReport import ErrorList\n\n')
            MacAppFile.write(f'def Main():\n')
            MacAppFile.write(f'   while True:\n')
            MacAppFile.write(f'      print("="*80)\n')
            MacAppFile.write(f'      print(">> Options Menu<<")\n')
            MacAppFile.write(f'      print(">> 1. Option One")\n')
            MacAppFile.write(f'      print(">> 2. Option Two")\n')
            MacAppFile.write(f'      print(">> 3. Option Three")\n\n')
            MacAppFile.write(f'      try:\n')
            MacAppFile.write(f'         UserInput = int(input(">> Type the option number: "))\n')
            MacAppFile.write(f'         print("="*80)\n')
            MacAppFile.write(f'         if UserInput == 1:\n')
            MacAppFile.write(f'            print("> Option 1")\n')
            MacAppFile.write(f'         elif UserInput == 2:\n')
            MacAppFile.write(f'            print("> Option 2")\n')
            MacAppFile.write(f'         elif UserInput == 3:\n')
            MacAppFile.write(f'            print("> Option 3")\n')
            MacAppFile.write(f'         else:\n')
            MacAppFile.write(f'            print(">> This option is unavailable at this time")\n')
            MacAppFile.write(f'      except:\n')
            MacAppFile.write(f'         print("-"*80)\n')
            MacAppFile.write(f'         print(">> This option is unavailable at this time")\n')
            MacAppFile.write(f'         print("-"*80)\n\n')
            MacAppFile.write(f'Main()\n')
            MacAppFile.close()
    else:
        print("> Creating MacApp Library...")
        with codecs.open(EnvironFolders.MacAppFile, "w", "utf-8-sig") as MacAppFile:
            MacAppFile.write(f'## MacApp File\n')
            MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
            MacAppFile.write(f'from ErrorReport import ErrorList\n\n')
            MacAppFile.write(f'def Main():\n')
            MacAppFile.write(f'   print("Hello World!")\n\n')
            MacAppFile.write(f'Main()\n')
            MacAppFile.close()

    ## Mac SplashScreen
    print("> Creating SplashScreen...")
    with codecs.open(EnvironFolders.SplashMac, "w", "utf-8-sig") as SplashMac:
        SplashMac.write(f'## SplashScreen File\n')
        SplashMac.write(f'## This file contains information about your project\n\n')
        SplashMac.write(f'from datetime import date\n\n')
        SplashMac.write(f'CurrentYear = date.today().year\n')
        SplashMac.write(f'SoftwareName = "{Explorer.ProjectName}"\n')
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

    ## Mac FileSystem
    print("> Creating Mac FileSystem Library...")
    with codecs.open(EnvironFolders.MacFS, "w", "utf-8-sig") as MacFS:
        Mac = "User = f'/Users/{os.environ"
        FileSystem = '["USER"]}/'
        SUser = f"{Mac}{FileSystem}'"
        MacFS.write(f'## FileSystem\n')
        MacFS.write(f'## This file contains some default directories of your system\n')
        MacFS.write(f'import os\n\n')
        MacFS.write(f'## Special Directories\n')
        MacFS.write(f'CurrentPath = os.getcwd()\n')
        MacFS.write(f'{SUser}\n')
        MacFS.write("Applications = f'{User}Applications/'\n")
        MacFS.write("Desktop = f'{User}Desktop/'\n")
        MacFS.write("Documents = f'{User}Documents/'\n")
        MacFS.write("Downloads = f'{User}Downloads/'\n")
        MacFS.write("Movies = f'{User}Movies/'\n")
        MacFS.write("Music = f'{User}Music/'\n")
        MacFS.write("Pictures = f'{User}Pictures/'\n")
        MacFS.write("Public = f'{User}Public/'\n")
        MacFS.close()

def WindowsPlat():
    print("="*80)
    print(">> Creating Windows Modules <<")
    print("="*80)
    
    ## Windows File
    print("> Creating Windows Library...")
    with codecs.open(EnvironFolders.WindowsFile, "w", "utf-8-sig") as WindowsFile:
        WindowsFile.write(f'## Windows File\n')
        WindowsFile.write(f'## This file is used to implement code used to run scripts for Windows\n')
        WindowsFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        WindowsFile.write(f'def Windows():\n')
        WindowsFile.write(f'   ## NOTE: You can use this function\n')
        WindowsFile.write(f'   ## To load information before the app starts running\n\n')
        WindowsFile.write(f'   ## Lets run the SplashScreen\n')
        WindowsFile.write(f'   from Windows import SplashScreen\n\n')
        WindowsFile.write(f'   ## Lets check system requirements\n')
        WindowsFile.write(f'   from ErrorReport import SystemRequirements\n\n')
        WindowsFile.write(f'   ## Start App for Windows\n')
        WindowsFile.write(f'   from Windows import WindowsApp\n\n')
        WindowsFile.close()

    ## WindowsApp File
    if LoopApp == True:
        print("> Creating WindowsApp Library...")
        with codecs.open(EnvironFolders.WindowsAppFile, "w", "utf-8-sig") as WindowsAppFile:
            WindowsAppFile.write(f'## WindowsApp File\n')
            WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
            WindowsAppFile.write(f'from ErrorReport import ErrorList\n\n')
            WindowsAppFile.write(f'def Main():\n')
            WindowsAppFile.write(f'   while True:\n')
            WindowsAppFile.write(f'      print("="*80)\n')
            WindowsAppFile.write(f'      print(">> Options Menu<<")\n')
            WindowsAppFile.write(f'      print(">> 1. Option One")\n')
            WindowsAppFile.write(f'      print(">> 2. Option Two")\n')
            WindowsAppFile.write(f'      print(">> 3. Option Three")\n\n')
            WindowsAppFile.write(f'      try:\n')
            WindowsAppFile.write(f'         UserInput = int(input(">> Type the option number: "))\n')
            WindowsAppFile.write(f'         print("="*80)\n')
            WindowsAppFile.write(f'         if UserInput == 1:\n')
            WindowsAppFile.write(f'            print("> Option 1")\n')
            WindowsAppFile.write(f'         elif UserInput == 2:\n')
            WindowsAppFile.write(f'            print("> Option 2")\n')
            WindowsAppFile.write(f'         elif UserInput == 3:\n')
            WindowsAppFile.write(f'            print("> Option 3")\n')
            WindowsAppFile.write(f'         else:\n')
            WindowsAppFile.write(f'            print(">> This option is unavailable at this time")\n')
            WindowsAppFile.write(f'      except:\n')
            WindowsAppFile.write(f'         print("-"*80)\n')
            WindowsAppFile.write(f'         print(">> This option is unavailable at this time")\n')
            WindowsAppFile.write(f'         print("-"*80)\n\n')  
            WindowsAppFile.write(f'Main()\n')
            WindowsAppFile.close()
    else:
        print("> Creating WindowsApp Library...")
        with codecs.open(EnvironFolders.WindowsAppFile, "w", "utf-8-sig") as WindowsAppFile:
            WindowsAppFile.write(f'## WindowsApp File\n')
            WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
            WindowsAppFile.write(f'from ErrorReport import ErrorList\n\n')
            WindowsAppFile.write(f'def Main():\n')
            WindowsAppFile.write(f'   print("Hello World!")\n\n') 
            WindowsAppFile.write(f'Main()\n')
            WindowsAppFile.close()

    ## Windows SplashScreen
    print("> Creating SplashScreen...")
    with codecs.open(EnvironFolders.SplashWindows, "w", "utf-8-sig") as SplashWindows:
        SplashWindows.write(f'## SplashScreen File\n')
        SplashWindows.write(f'## This file contains information about your project\n\n')
        SplashWindows.write(f'from datetime import date\n\n')
        SplashWindows.write(f'CurrentYear = date.today().year\n')
        SplashWindows.write(f'SoftwareName = "{Explorer.ProjectName}"\n')
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

    ## Windows FileSystem
    print("> Creating Windows FileSystem Library...")
    with codecs.open(EnvironFolders.WindowsFS, "w", "utf-8-sig") as WindowsFS:
        WindowsFS.write(f'## FileSystem\n')
        WindowsFS.write(f'## This file contains some default directories of your system\n')
        WindowsFS.write(f'import os\n\n')
        WindowsFS.write(f'## Special Directories\n')
        WindowsFS.write(f'CurrentPath = os.getcwd()\n')
        WindowsFS.write(f"User = os.environ['USERPROFILE']\n")
        
        WindowsFS.write("ApplicationData = f'{User}AppData/Roaming/'\n")
        WindowsFS.write("Desktop = f'{User}Desktop/'\n")
        WindowsFS.write("Documents = f'{User}Documents/'\n")
        WindowsFS.write("Downloads = f'{User}Downloads/'\n")
        WindowsFS.write("LocalAppData = f'{User}AppData/Local/'\n")
        WindowsFS.write("Temp = f'{LocalAppData}Temp'\n")
        WindowsFS.write("Pictures = f'{User}Pictures/'\n")
        WindowsFS.write("Favorites = f'{User}Favorites/'\n")
        WindowsFS.close()

def CreateBridge():
    ## Project Structure
    ## Readme File
    ## Reports Module
    ## System Requirements Module
    ProjectStruct()
    print("-"*80)
    print()

    ## Linux Module
    LinuxPlat()
    print("-"*80)
    print()
    ## macOS Modules
    MacPlat()
    print("-"*80)
    print()
    ## Windows Modules
    WindowsPlat()
    print("-"*80)
    print()
