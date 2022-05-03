## Core
## This file will process every step of file creation

import codecs
import getpass
import os
import requests
import shutil
import sys
from datetime import datetime
from exception import Exceptions
from mac import FileSystem
from pathlib import Path
from zipfile import ZipFile

ProjectType = ""
ProjectOption = 0
TweetStr = "{Tweet}"

MajorVersion = sys.version_info[0]
MinorVersion = sys.version_info[1]
BuildVersion = sys.version_info[2]
ProjList = []

class DownloadSample():
    def GetInfo(self):
        print("="*80)
        print(">> DOWNLOADING GETINFO SAMPLE... <<")
        print("="*80)
        print("[Status]: Downloading 'GetInfo'... <<")
        print("="*80)

        try:
            os.mkdir(f'{FileSystem.CurrentPath}/Sample/')
            print('[Status]: Verifying repository to download...')
        except:
            print('[Status]: Verifying repository to download...')

        try:
            os.mkdir(f'{FileSystem.CurrentPath}/Sample/GetInfo/')
            print("[Status]: Starting Download...")
        except:
            print("[Status]: Starting Download...")
            print("[Status]: The project seems to be in the path, already!")

        URL = "https://github.com/hbisneto/GetInfo/archive/refs/heads/main.zip"
        From = f'{FileSystem.CurrentPath}/main.zip'
        To = f'{FileSystem.CurrentPath}/Sample/GetInfo/main.zip'

        ServerResponse = requests.get(URL, stream = True)
        FileName = URL.split("/")[-1]
        with open(FileName, 'wb') as f:
            for Chunk in ServerResponse.iter_content(chunk_size = 1024):
                if Chunk:
                    f.write(Chunk)

        print("[Status]: 'GetInfo' download 100% completed!")
        print("[Status]: Verifying 'GetInfo'...")
        try:
            Path(From).rename(To)
            print("[Done]: 'GetInfo' download process complete!")
            print("="*80)
        except:
            Path(From).rename(To)
            print("[Done]: 'GetInfo' download process complete!")
            print("="*80)
        
        with ZipFile(To, 'r') as zipObj:
            zipObj.extractall(f'{FileSystem.CurrentPath}/Sample/GetInfo/main')
        print("[Done]: 'main' extraction process complete!")
        print("="*80)

    def Jokenpo(self):
        print("="*80)
        print(">> DOWNLOADING JOKENPO SAMPLE... <<")
        print("="*80)
        print("[Status]: Downloading 'JoKenPo'... <<")
        print("="*80)

        try:
            os.mkdir(f'{FileSystem.CurrentPath}/Sample/')
            print('[Status]: Verifying repository to download...')
        except:
            print('[Status]: Verifying repository to download...')

        try:
            os.mkdir(f'{FileSystem.CurrentPath}/Sample/JoKenPo/')
            print("[Status]: Starting Download...")
        except:
            print("[Status]: Starting Download...")
            print("[Status]: The project seems to be in the path, already!")
            

        URL = "https://github.com/hbisneto/JoKenPo/archive/refs/heads/main.zip"
        From = f'{FileSystem.CurrentPath}/main.zip'
        To = f'{FileSystem.CurrentPath}/Sample/JoKenPo/main.zip'

        ServerResponse = requests.get(URL, stream = True)
        FileName = URL.split("/")[-1]
        with open(FileName, 'wb') as f:
            for Chunk in ServerResponse.iter_content(chunk_size = 1024):
                if Chunk:
                    f.write(Chunk)

        print("[Status]: 'JoKenPo' download 100% completed!")
        print("[Status]: Verifying 'GetInfo'...")
        try:
            Path(From).rename(To)
            print("[Done]: 'JoKenPo' download process complete!")
            print("="*80)
        except:
            Path(From).rename(To)
            print("[Done]: 'JoKenPo' download process complete!")
            print("="*80)
        
        with ZipFile(To, 'r') as zipObj:
            zipObj.extractall(f'{FileSystem.CurrentPath}/Sample/JoKenPo/main')
        print("[Done]: 'main' extraction process complete!")
        print("="*80)

def Backup():
    Day = datetime.now().day
    Month = datetime.now().month
    Year = datetime.now().year
    Hour = datetime.now().hour
    Minute = datetime.now().minute
    Second = datetime.now().second

    DateFormat = f'PyBridge_BKP_{Day}_{Month}_{Year}-{Hour}_{Minute}_{Second}'

    Source = f'{FileSystem.ProjectsRepo}'
    Target = f'{FileSystem.CurrentPath}/Backup/{DateFormat}'

    def MakeZip(MyZip):
        print("[Backup Option]: Creating compressed file...")
        shutil.make_archive(MyZip, 'zip', MyZip)

    print("="*80)
    try:
        Start = datetime.now()
        print("[PyBridge]: Backing up...")
        print("="*80)
        shutil.copytree(Source, Target)
        print("[PyBridge]: Backup creation done!")
        End = datetime.now()
        Time = End - Start
        print(f'>> Operation completed in: {Time}')

        BKPInput = str(input("[Backup Option]: Do you want to create a compressed backup file? [Y/N]: "))
        if BKPInput == "Y" or BKPInput == "y" or BKPInput == "1":
            MakeZip(MyZip = Target)
            print("[Backup Option]: Compressed file creation done!")
            try:
                shutil.rmtree(Target)
            except OSError as DirError:
                Exceptions.CompressBackupFail()
                print(DirError)
        else:
            print(f'>> Operation completed in: {Time}')
            
    except shutil.Error as e:
        Exceptions.BackupFail()
        print("-"*20)
        print(e)
        print("-"*20)
    except OSError as OS_E:
        Exceptions.BackupFail()
        print("-"*20)
        print(OS_E)
        print("-"*20)
    print("="*80)
    print()
    
def Explorer():
    ProjectName = str()
    FolderLocation = str()

def VerifyFolders():
    def BridgeFolder():
        try:
            os.mkdir(FileSystem.PyBridgeFolder)
            print(f'>> PyBridge: "{FileSystem.PyBridgeFolder}" created')
        except:
            return

    def ProjectsFolder():
        try:
            os.mkdir(FileSystem.ProjectsRepo)
            print(f'>> PyBridge: "{FileSystem.ProjectsRepo}" created')
        except:
            return

    BridgeFolder()
    ProjectsFolder()

def ProjectList():
    try:
        BridgeRepo = os.listdir(FileSystem.ProjectsRepo)
        for Project in BridgeRepo:
            ProjList.append(Project)
            if '.DS_Store' in ProjList:
                ProjList.remove('.DS_Store')
    except:
        Exceptions.ProjectsLoadFail()
    
    BridgeLoop = True
    while BridgeLoop == True:
        print("="*80)
        print(f'>> PROJECTS LIST <<')
        print("="*80)

        Count = 0
        for App in ProjList:
            Count += 1
            print(f'[{Count}] - {App}')
        
        if Count == 0:
            print("="*80)
            print(f'>> Your list of projects is empty')
            print("="*80)
            print()
        BridgeLoop = False
        ProjOptions()

def ProjOptions():
    ## Create Local Library (Inside all OS Modules)
    def CreateLib(AppliesTo):
        LibName = str(input(">>[!] Type the Lib name: "))
        LinuxLibLocation = f'{AppliesTo}/linux/{LibName}{FileSystem.PythonExtension}'
        MacLibLocation = f'{AppliesTo}/mac/{LibName}{FileSystem.PythonExtension}'
        WindowsLibLocation = f'{AppliesTo}/windows/{LibName}{FileSystem.PythonExtension}'

        try:
            with codecs.open(LinuxLibLocation, "w", "utf-8-sig") as LocalLib:
                LocalLib.write(f'## {LibName} File\n')
                LocalLib.write(f'## Custom Universal Library: {LibName}\n\n')
                LocalLib.write(f'try:\n')
                LocalLib.write(f'   ## Imported Libraries\n')
                LocalLib.write(f'   from sys import platform\n\n')
                LocalLib.write(f'   ## Local Libraries\n')
                LocalLib.write(f'   from exception import Exceptions\n')
                LocalLib.write(f'   from linux import Linux\n\n')
                LocalLib.write(f'   Platform = platform\n\n')
                LocalLib.write(f'except:\n')
                LocalLib.write(f'   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")\n\n')
                LocalLib.write(f'def Main():\n')
                LocalLib.write(f'   print(">> Custom Universal Library")\n\n')
                LocalLib.write(f'Main()')
                LocalLib.close()
            print(f'>> [100%] Created Linux Library: "{LibName}{FileSystem.PythonExtension}"')
        except:
            print(f'>> [!] Skipped creation of "{LibName}{FileSystem.PythonExtension}" in "Linux" module')

        try:
            with codecs.open(MacLibLocation, "w", "utf-8-sig") as LocalLib:
                LocalLib.write(f'## {LibName} File\n')
                LocalLib.write(f'## Custom Universal Library: {LibName}\n\n')
                LocalLib.write(f'try:\n')
                LocalLib.write(f'   ## Imported Libraries\n')
                LocalLib.write(f'   from sys import platform\n\n')
                LocalLib.write(f'   ## Local Libraries\n')
                LocalLib.write(f'   from exception import Exceptions\n')
                LocalLib.write(f'   from mac import Mac\n\n')
                LocalLib.write(f'   Platform = platform\n\n')
                LocalLib.write(f'except:\n')
                LocalLib.write(f'   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")\n\n')
                LocalLib.write(f'def Main():\n')
                LocalLib.write(f'   print(">> Custom Universal Library")\n\n')
                LocalLib.write(f'Main()')
                LocalLib.close()
            print(f'>> [100%] Created Mac Library: "{LibName}{FileSystem.PythonExtension}"')
        except:
            print(f'>> [!] Skipped creation of "{LibName}{FileSystem.PythonExtension}" in "Mac" module')

        try:
            with codecs.open(WindowsLibLocation, "w", "utf-8-sig") as LocalLib:
                LocalLib.write(f'## {LibName} File\n')
                LocalLib.write(f'## Custom Universal Library: {LibName}\n\n')
                LocalLib.write(f'try:\n')
                LocalLib.write(f'   ## Imported Libraries\n')
                LocalLib.write(f'   from sys import platform\n\n')
                LocalLib.write(f'   ## Local Libraries\n')
                LocalLib.write(f'   from exception import Exceptions\n')
                LocalLib.write(f'   from windows import Windows\n\n')
                LocalLib.write(f'   Platform = platform\n\n')
                LocalLib.write(f'except:\n')
                LocalLib.write(f'   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")\n\n')
                LocalLib.write(f'def Main():\n')
                LocalLib.write(f'   print(">> Custom Universal Library")\n\n')
                LocalLib.write(f'Main()')
                LocalLib.close()
            print(f'>> [100%] Created Windows Library: "{LibName}{FileSystem.PythonExtension}"')
        except:
            print(f'>> [!] Skipped creation of "{LibName}{FileSystem.PythonExtension}" in "Windows" module')

    ## Create Local Module (Inside all OS Modules)
    def CreateMod(AppliesTo):
        ModName = str(input(">>[!] Type the module name: "))
        LinuxModLocation = f'{AppliesTo}/linux/{ModName}'
        MacModLocation = f'{AppliesTo}/mac/{ModName}'
        WindowsModLocation = f'{AppliesTo}/windows/{ModName}'

        try:
            os.mkdir(LinuxModLocation)
            print(f'>> [100%] Created Linux Module: "{ModName}"')
        except:
            print(f'>> [!] Skipped creation of "{ModName}" in "Linux" module')

        try:
            os.mkdir(MacModLocation)
            print(f'>> [100%] Created Mac Module: "{ModName}"')
        except:
            print(f'>> [!] Skipped creation of "{ModName}" in "Mac" module')

        try:
            os.mkdir(WindowsModLocation)
            print(f'>> [100%] Created Windows Module: "{ModName}"')
        except:
            print(f'>> [!] Skipped creation of "{ModName}" in "Windows" module')

    ## Create an Universal Library (Inside the root of project)
    def CreateUniversalLib(AppliesTo):
        LibName = str(input(">>[!] Type the Lib name: "))
        LibFileLocation = f'{AppliesTo}/{LibName}{FileSystem.PythonExtension}'

        try:
            with codecs.open(LibFileLocation, "w", "utf-8-sig") as UniversalLib:
                UniversalLib.write(f'## {LibName} File\n')
                UniversalLib.write(f'## Custom Universal Library: {LibName}\n\n')
                UniversalLib.write(f'try:\n')
                UniversalLib.write(f'   ## Imported Libraries\n')
                UniversalLib.write(f'   from sys import platform\n\n')
                UniversalLib.write(f'   ## Local Libraries\n')
                UniversalLib.write(f'   from exception import Exceptions\n')
                UniversalLib.write(f'   from linux import Linux\n')
                UniversalLib.write(f'   from mac import Mac\n')
                UniversalLib.write(f'   from windows import Windows\n\n')
                UniversalLib.write(f'   Platform = platform\n\n')
                UniversalLib.write(f'except:\n')
                UniversalLib.write(f'   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")\n\n')
                UniversalLib.write(f'def Main():\n')
                UniversalLib.write(f'   print(">> Custom Universal Library")\n\n')
                UniversalLib.write(f'Main()')
                UniversalLib.close()
            print(f'>> [100%] Created Library: "{LibName}{FileSystem.PythonExtension}"')
        except:
            print(f'>> [!] Could not create "{LibName}{FileSystem.PythonExtension}" inside root of project...')

    ## Create an Universal Module (Inside the root of project)
    def CreateUniversalMod(AppliesTo):
        ModName = str(input(">>[!] Type the module name: "))
        ModLocation = f'{AppliesTo}/{ModName}'

        try:
            os.mkdir(ModLocation)
            print(f'>> [100%] Created Module: "{ModName}"')
        except:
            print(f'>> [!] Could not create "{ModName}" inside root of project...')

    ## Delete a repository project inside "Documents/PyBridge/" folder
    def DeleteProject(AppliesTo):
        print("="*80)
        print(">> DELETE THIS PROJECT <<")
        print(f'[Project to delete: {ProjList[Opc-1]}]')
        print("="*80)
            
        ConfirmTyping = f'Projects/{ProjList[Opc-1]}'
        print(f'>> You`re trying to delete the project "{ProjList[Opc-1]}"')
        print(f'>> THIS OPERATION CAN`T BE UNDONE.\n>> BE SURE YOU REALLY WANT TO DELETE THE PROJECT')
        print()
        DeletePrompt = str(input(f'>>[!] Are you sure do you want to delete the project "{ProjList[Opc-1]}"? [Y/N]: '))

        if DeletePrompt == "Y" or DeletePrompt == "y" or DeletePrompt == "1":
            ConfirmDelete = str(input(f'>>[!] Type "{ConfirmTyping}" to delete the project: '))
            if ConfirmDelete == ConfirmTyping:
                DeleteDir = f'{FileSystem.ProjectsRepo}{ProjList[Opc - 1]}'

                try:
                    print("="*80)
                    print(f'>> DELETING PROJECT "{ProjList[Opc-1]}" <<')
                    print("="*80)

                    print(f'>> Project Name: {ProjList[Opc-1]}')
                    print(f'>> Location: {DeleteDir}')
                    print()
                    
                    shutil.rmtree(DeleteDir)
                    print(f'>> The project "{DeleteDir}" was deleted!')
                    print("="*80)
                except OSError as e:
                    print(">> [x] Erro: %s - %s." % (e.filename, e.strerror))
                    print("="*80)

            else:
                print(f'>> Delete confirmation password do not match!')
                print(f'>> Could not delete the project folder')
        else:
            print(">> Project folder was not deleted")
        
    print(f'[0] << Go Back')
    print("="*80)

    Opc = int(input(">>[!] Type a number to get options or go back: "))
    print()

    try:
        if Opc != 0:
            AppliesTo = f'{FileSystem.ProjectsRepo}{ProjList[Opc - 1]}'

            print("="*80)
            print(">> Management Options <<")
            print("="*80)
            
            print("[1] - Create Library")
            print("Will add a Library in all OS Modules")
            print("="*80)
            
            print("[2] - Create Universal Library")
            print("Will add a new Library on the root of project")
            print("="*80)

            print("[3] - Create Module")
            print("Will add a Module in all OS Modules")
            print("="*80)

            print("[4] - Create Universal Module")
            print("Will add a new Module on the root of project")
            print("="*80)

            print("[5] - DELETE THIS PROJECT")
            print("Deletes the project folder and all the contents in it.")
            print("CAUTION: THIS OPERATION CAN`T BE UNDONE...")
            print("="*80)

            print("[0] - Go Back")
            print("Navigate back to the main menu")
            print("="*80)

            SubMenu = int(input(">>[!] Type your choice: "))
            print("="*80)
            print()

            if SubMenu == 1:
                CreateLib(AppliesTo)
            elif SubMenu == 2:
                CreateUniversalLib(AppliesTo)
            elif SubMenu == 3:
                CreateMod(AppliesTo)
            elif SubMenu == 4:
                CreateUniversalMod(AppliesTo)
            elif SubMenu == 5:
                DeleteProject(AppliesTo)
            
            print("="*80)
            print(">> Management Options <<")
            print("="*80)
            print()
    except:
        Exceptions.InvalidOption()

def CreateEnvironment():
    ## Environment Folders
    CreateEnvironment.exceptionPath = f'{Explorer.FolderLocation}exception/'
    CreateEnvironment.LinuxPath = f'{Explorer.FolderLocation}linux/'
    CreateEnvironment.MacPath = f'{Explorer.FolderLocation}mac/'
    CreateEnvironment.WindowsPath = f'{Explorer.FolderLocation}windows/'

    ## Environment Files
    CreateEnvironment.UserAppName = f'{Explorer.FolderLocation}__init__.py'
    CreateEnvironment.TokensFile = f'{Explorer.FolderLocation}Tokens.py'
    CreateEnvironment.ReadmeFile = f'{Explorer.FolderLocation}README.md'
    CreateEnvironment.ExceptionsFile = f'{CreateEnvironment.exceptionPath}Exceptions.py'
    CreateEnvironment.Requirements = f'{CreateEnvironment.exceptionPath}Requirements.py'
    
    ## Linux
    CreateEnvironment.LinuxFS = f'{CreateEnvironment.LinuxPath}FileSystem.py'
    CreateEnvironment.LinuxFile = f'{CreateEnvironment.LinuxPath}Linux.py'
    CreateEnvironment.LinuxAppFile = f'{CreateEnvironment.LinuxPath}LinuxApp.py'
    CreateEnvironment.SplashLinux = f'{CreateEnvironment.LinuxPath}SplashScreen.py'
    
    ## Mac
    CreateEnvironment.MacFS = f'{CreateEnvironment.MacPath}FileSystem.py'
    CreateEnvironment.MacFile = f'{CreateEnvironment.MacPath}Mac.py'
    CreateEnvironment.MacAppFile = f'{CreateEnvironment.MacPath}MacApp.py'
    CreateEnvironment.SplashMac = f'{CreateEnvironment.MacPath}SplashScreen.py'

    ## Windows
    CreateEnvironment.WindowsFS = f'{CreateEnvironment.WindowsPath}FileSystem.py'
    CreateEnvironment.WindowsFile = f'{CreateEnvironment.WindowsPath}Windows.py'
    CreateEnvironment.WindowsAppFile = f'{CreateEnvironment.WindowsPath}WindowsApp.py'
    CreateEnvironment.SplashWindows = f'{CreateEnvironment.WindowsPath}SplashScreen.py'

    # Create Archtecture
    try:
        os.mkdir(CreateEnvironment.exceptionPath)
        os.mkdir(CreateEnvironment.LinuxPath)
        os.mkdir(CreateEnvironment.MacPath)
        os.mkdir(CreateEnvironment.WindowsPath)
    except:
        print("="*80)
        print(">> Preparing Project Architecture...")
        print("="*80)
        print(">> Project Architecture Created!")

    # Create Files
    ## Environment Files
    UserAppName = open(CreateEnvironment.UserAppName, "w")
    ReadmeFile = open(CreateEnvironment.ReadmeFile, "w")
    ExceptionsFile = open(CreateEnvironment.ExceptionsFile, "w")
    Requirements = open(CreateEnvironment.Requirements, "w")
    
    ## Linux
    LinuxFS = open(CreateEnvironment.LinuxFS, "w")
    LinuxFile = open(CreateEnvironment.LinuxFile, "w")
    LinuxAppFile = open(CreateEnvironment.LinuxAppFile, "w")
    SplashLinux = open(CreateEnvironment.SplashLinux, "w")

    ## Mac
    MacFS = open(CreateEnvironment.MacFS, "w")
    MacFile = open(CreateEnvironment.MacFile, "w")
    MacAppFile = open(CreateEnvironment.MacAppFile, "w")
    SplashMac = open(CreateEnvironment.SplashMac, "w")

    ## Windows
    WindowsFS = open(CreateEnvironment.WindowsFS, "w")
    WindowsFile = open(CreateEnvironment.WindowsFile, "w")
    WindowsAppFile = open(CreateEnvironment.WindowsAppFile, "w")
    SplashWindows = open(CreateEnvironment.SplashWindows, "w")

    if ProjectOption == 3:
        TokensFile = open(CreateEnvironment.TokensFile, "w")

def CreateInitFile():
    ## Launcher Script
    print("="*80)
    print(f'>> {ProjectType} <<')
    print("="*80)
    
    with codecs.open(CreateEnvironment.UserAppName, "w", "utf-8-sig") as AppName:
        AppName.write(f'## __init__.py File\n')
        AppName.write(f'## Here the contents will be processed to choose the best platform to go\n\n')
        AppName.write(f'try:\n')
        AppName.write(f'   ## Imported Libraries\n')
        AppName.write(f'   from sys import platform\n\n')
        AppName.write(f'   ## Local Libraries\n')
        AppName.write(f'   from exception import Exceptions\n')
        AppName.write(f'except:\n')
        AppName.write(f'   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")\n\n')
        AppName.write(f'def Main():\n')
        AppName.write(f'   Platform = platform\n\n')
        AppName.write(f'   ## Linux\n')
        AppName.write(f'   if Platform == "linux" or Platform == "linux2":\n')
        AppName.write(f'      from linux import Linux\n')
        AppName.write(f'      linux.Linux()\n\n')
        AppName.write(f'   ## Mac\n')
        AppName.write(f'   elif Platform == "darwin":\n')
        AppName.write(f'      from mac import Mac\n')
        AppName.write(f'      mac.Mac()\n\n')
        AppName.write(f'   ## Windows\n')
        AppName.write(f'   elif Platform == "win32" or Platform == "win64":\n')
        AppName.write(f'      from windows import Windows\n')
        AppName.write(f'      windows.Windows()\n\n')
        AppName.write(f'Main()')
        AppName.close()

def CreateReadmeFile():
    ## README File
    print("> Creating 'README' File...")
    with codecs.open(CreateEnvironment.ReadmeFile, "w", "utf-8-sig") as Readme:
        Readme.write(f'# {Explorer.ProjectName}\n\n')
        Readme.write(f'This project was created using [PyBridge](https://github.com/hbisneto/PyBridge)\n\n')
        Readme.write(f'## Requirements\n\n')
        Readme.write(f'{Explorer.ProjectName} requires Python {MajorVersion}.{MinorVersion}.{BuildVersion} or later to run\n\n')
        Readme.write(f'## Installation\n\n')
        Readme.write(f'```\n')
        Readme.write(f'pip install {Explorer.ProjectName}\n')
        Readme.write(f'```\n\n')
        Readme.write(f'## External Links\n\n')
        Readme.write(f'Here is some external links that you can use in your `README.md` file.\n\n')
        Readme.write(f'- [First Link](https://google.com)\n')
        Readme.write(f'- [Second Link](https://google.com)\n')
        Readme.write(f'- [Third Link](https://google.com)\n\n')
        Readme.write(f'#\n\n')
        Readme.write(f'Copyright © {datetime.now().year} {getpass.getuser().capitalize()}. All rights reserved.')
        Readme.close()

def CreateExceptions():
    ## Exception Triggers
    print("> Creating exceptions Module...")
    with codecs.open(CreateEnvironment.ExceptionsFile, "w", "utf-8-sig") as Exceptions:
        Exceptions.write(f'## Exceptions File\n')
        Exceptions.write(f'## This file contains events thats raised when the program must to stop\n\n')
        Exceptions.write(f'class Raise():\n')
        Exceptions.write(f'   class Requirements():\n')
        Exceptions.write(f'      def MajorVersion(self, CurrentVersion, TargetVersion, TargetMajor):\n')
        Exceptions.write("         raise Exception(f'>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')\n\n")
        Exceptions.write(f'      def MinorVersion(self, CurrentVersion, TargetVersion, TargetMinor):\n')
        Exceptions.write(f'         print("="*80)\n')
        Exceptions.write(f'         print(">> PYBRIDGE <<")\n')
        Exceptions.write(f'         print("="*80)\n')
        Exceptions.write(f'         print(">> WARNING <<")\n')
        Exceptions.write(f'         print("="*80)\n')
        Exceptions.write("         print(f'>> Your appication targets a version of Python older than the version currently installed. You may get errors during the process')\n")
        Exceptions.write(f'         print("="*80)\n')
        Exceptions.write("         print(f'- Current Version: {CurrentVersion}')\n")
        Exceptions.write("         print(f'- Target Version: {TargetVersion}')\n")
        Exceptions.write("         print(f'>> You can change `Requirements.py` on `exception` Module')\n")
        Exceptions.write(f'         print("="*80)\n')
        Exceptions.write(f'         print()\n\n')
        Exceptions.write(f'      def BuildVersion(self, CurrentVersion, TargetVersion, BuildVer):\n')
        Exceptions.write("         raise Exception(f'>> This application only can run on Python {TargetVersion}. [Current Version: {CurrentVersion}]')\n\n")
        Exceptions.write(f'def ImportLib():\n')
        Exceptions.write(f'   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")\n\n')
        Exceptions.write(f'def FileExists():\n')
        Exceptions.write(f'   raise RuntimeError(">> The file already exists!")\n\n')
        Exceptions.write(f'def DirectoryExists():\n')
        Exceptions.write(f'   raise RuntimeError(">> The directory already exists!")\n\n')
        Exceptions.write(f'def InputFormat():\n')
        Exceptions.write(f'   print(">> Your input is not valid: Check your input and try again")\n\n')
        Exceptions.write(f'def InvalidOption():\n')
        Exceptions.write(f'   print("="*80)\n')
        Exceptions.write(f'   print(">> Invalid Option!")\n')
        Exceptions.write(f'   print("="*80)\n')
        Exceptions.write("   print(f'>> You typed an invalid option. Run the program again!')\n")
        Exceptions.write(f'   print("="*80)\n')
        Exceptions.close()

def CreateRequirements():
    ## System Requirements File
    print("> Creating Requirements Library...")
    with codecs.open(CreateEnvironment.Requirements, "w", "utf-8-sig") as Requirements:
        Requirements.write(f'## Requirements File\n')
        Requirements.write(f'## This file is used to check if system matches with the minimum requirements to run\n\n')
        Requirements.write(f'import sys\n')
        Requirements.write(f'from exception import Exceptions\n\n')
        Requirements.write(f'## Change "Require" to "False" to skip system check\n')
        Requirements.write(f'Require = True\n')
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
        Requirements.write("   ## print(f'>> My system current version: Python {CurrentVersion}')\n")
        Requirements.write("   ## print(f'>> Required version to run: Python {TargetVersion}')\n\n")
        Requirements.write(f'   if TargetVersion > CurrentVersion:\n')
        Requirements.write(f'      Exceptions.Raise().Requirements().MajorVersion(CurrentVersion, TargetVersion, TargetMajor)\n')
        Requirements.write(f'   elif TargetVersion < CurrentVersion:\n')
        Requirements.write(f'      Exceptions.Raise().Requirements().MinorVersion(CurrentVersion, TargetVersion, TargetMinor)\n')
        Requirements.close()

def CreateLinuxFile():
    print("="*80)
    print(">> Creating Linux Modules <<")
    print("="*80)
    
    ## Linux File
    print("> Creating Linux Library...")
    with codecs.open(CreateEnvironment.LinuxFile, "w", "utf-8-sig") as LinuxFile:
        LinuxFile.write(f'## Linux File\n')
        LinuxFile.write(f'## This file is used to implement code used to run scripts for Linux\n')
        LinuxFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        LinuxFile.write(f'import os\n')
        LinuxFile.write(f'from linux import FileSystem\n\n')
        LinuxFile.write(f'def Linux():\n')
        LinuxFile.write(f'   ## NOTE: You can use this function\n')
        LinuxFile.write(f'   ## To load information before the app starts running\n\n')
        LinuxFile.write(f'   ## Lets run the SplashScreen\n')
        LinuxFile.write(f'   from linux import SplashScreen\n\n')
        LinuxFile.write(f'   ## Lets check system requirements\n')
        LinuxFile.write(f'   from exception import Requirements\n\n')
        LinuxFile.write(f'   ## Start App for Linux\n')
        LinuxFile.write(f'   from linux import LinuxApp\n\n')
        LinuxFile.close()

def CreateLinuxAppFile():
    ## LinuxApp File
    if ProjectOption == 1:
        print("> Creating LinuxApp Library...")
        with codecs.open(CreateEnvironment.LinuxAppFile, "w", "utf-8-sig") as LinuxAppFile:
            LinuxAppFile.write(f'## LinuxApp File\n')
            LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
            LinuxAppFile.write(f'from exception import Exceptions\n')
            LinuxAppFile.write(f'from linux import FileSystem\n\n')
            LinuxAppFile.write(f'def Main():\n')
            LinuxAppFile.write(f'   print("Hello World!")\n\n')
            LinuxAppFile.write(f'Main()\n')
            LinuxAppFile.close()
            
    elif ProjectOption == 2:
        print(">> Applying Loop Application on Environment on Linux...\n>> Please wait...")
        print("> Creating LinuxApp Library...")
        with codecs.open(CreateEnvironment.LinuxAppFile, "w", "utf-8-sig") as LinuxAppFile:
            LinuxAppFile.write(f'## LinuxApp File\n')
            LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
            LinuxAppFile.write(f'from exception import Exceptions\n')
            LinuxAppFile.write(f'from linux import FileSystem\n\n')
            LinuxAppFile.write(f'def Main():\n')
            LinuxAppFile.write(f'   while True:\n')
            LinuxAppFile.write(f'      print("="*80)\n')
            LinuxAppFile.write(f'      print(">> Options Menu<<")\n')
            LinuxAppFile.write(f'      print(">> 1. Option One")\n')
            LinuxAppFile.write(f'      print(">> 2. Option Two")\n')
            LinuxAppFile.write(f'      print(">> 3. Option Three")\n\n')
            LinuxAppFile.write(f'      try:\n')
            LinuxAppFile.write(f'         UserInput = int(input(">>[!] Type the option number: "))\n')
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

    elif ProjectOption == 3:
        with codecs.open(CreateEnvironment.LinuxAppFile, "w", "utf-8-sig") as LinuxAppFile:
            LinuxAppFile.write(f'## LinuxApp File\n')
            LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
            LinuxAppFile.write(f'import Tokens\n')
            LinuxAppFile.write(f'from exception import Exceptions\n')
            LinuxAppFile.write(f'from linux import FileSystem\n\n')
            LinuxAppFile.write(f'def NewTweet():\n')
            LinuxAppFile.write(f'   print("="*80)\n')
            LinuxAppFile.write(f'   print("NEW TWEET")\n')
            LinuxAppFile.write(f'   print("="*80)\n')
            LinuxAppFile.write(f'   Tweet = str(input(">>[!] Whats happening? "))\n')
            LinuxAppFile.write(f'   print("="*80)\n')
            LinuxAppFile.write(f'   print()\n')
            LinuxAppFile.write(f'   print("-"*80)\n')
            LinuxAppFile.write(f'   print(">> Your tweet was sent")\n')
            LinuxAppFile.write(f'   print("-"*80)\n')
            LinuxAppFile.write(f'   print()\n')
            LinuxAppFile.write(f'   print("="*80)\n\n')
            LinuxAppFile.write(f'   try:\n')
            LinuxAppFile.write(f'      Tokens.Twitter.update_status(Tweet)\n')
            LinuxAppFile.write(f"      print(f'>> Your last tweet:')\n")
            LinuxAppFile.write(f"      print(f' > {TweetStr}')\n")
            LinuxAppFile.write(f'      print("-" * 80)\n')
            LinuxAppFile.write(f'   except:\n')
            LinuxAppFile.write(f'      print(">>  Something went wrong: Unabled to connect to Twitter.")\n\n')
            LinuxAppFile.write(f'def Main():\n')
            LinuxAppFile.write(f'   NewTweet()\n\n')
            LinuxAppFile.write(f'Main()\n')
            LinuxAppFile.close()

def CreateLinuxSplashScreen():
    ## Linux SplashScreen
    if ProjectOption == 3:
        with codecs.open(CreateEnvironment.SplashLinux, "w", "utf-8-sig") as SplashLinux:
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
            SplashLinux.write(f'if CurrentYear == 2022:\n')
            SplashLinux.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashLinux.write(f'else:\n')
            SplashLinux.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write("print(f'[{SoftwareName} for Linux] - Running...')\n")
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write(f"print(f'>> Checking Twitter connection. Please wait...')\n")
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write(f'print()')
            SplashLinux.close()
    else:
        print("> Creating SplashScreen...")
        with codecs.open(CreateEnvironment.SplashLinux, "w", "utf-8-sig") as SplashLinux:
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
            SplashLinux.write(f'if CurrentYear == 2022:\n')
            SplashLinux.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashLinux.write(f'else:\n')
            SplashLinux.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write("print(f'[{SoftwareName} for Linux] - Running...')\n")
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write(f'print()\n')
            SplashLinux.close()

def CreateLinuxFileSystem():
    ## Linux FileSystem
    print("> Creating Linux FileSystem Library...")
    with codecs.open(CreateEnvironment.LinuxFS, "w", "utf-8-sig") as LinuxFS:
        Linux = "User = f'/home/{os.environ"
        FileSystem = '["USER"]}/'
        SUser = f"{Linux}{FileSystem}'"
        LinuxFS.write(f'## FileSystem\n')
        LinuxFS.write(f'## This file contains some default directories of your system\n\n')
        LinuxFS.write(f'import os\n\n')
        LinuxFS.write(f'## Special Directories\n')
        LinuxFS.write(f'CurrentPath = os.getcwd()\n')
        LinuxFS.write(f'{SUser}\n\n')
        LinuxFS.write("Desktop = f'{User}Desktop/'\n")
        LinuxFS.write("Documents = f'{User}Documents/'\n")
        LinuxFS.write("Downloads = f'{User}Downloads/'\n")
        LinuxFS.write("Music = f'{User}Music/'\n\n")
        LinuxFS.write("## Project Directories\n")
        LinuxFS.write("PyBridgeFolder = f'{Documents}PyBridge/'\n")
        LinuxFS.write("ProjectsRepo = f'{PyBridgeFolder}Projects/'\n")
        LinuxFS.write("PythonExtension = '.py'\n")
        LinuxFS.close()

def CreateMacFile():
    print("="*80)
    print(">> Creating Mac Modules <<")
    print("="*80)

    ## Mac File
    print("> Creating Mac Library...")
    with codecs.open(CreateEnvironment.MacFile, "w", "utf-8-sig") as MacFile:
        MacFile.write(f'## Mac File\n')
        MacFile.write(f'## This file is used to implement code used to run scripts for Mac\n')
        MacFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        MacFile.write(f'import os\n')
        MacFile.write(f'from mac import FileSystem\n\n')
        MacFile.write(f'def Mac():\n')
        MacFile.write(f'   ## NOTE: You can use this function\n')
        MacFile.write(f'   ## To load information before the app starts running\n\n')
        MacFile.write(f'   ## Lets run the SplashScreen\n')
        MacFile.write(f'   from mac import SplashScreen\n\n')
        MacFile.write(f'   ## Lets check system requirements\n')
        MacFile.write(f'   from exception import Requirements\n\n')
        MacFile.write(f'   ## Start App for Mac\n')
        MacFile.write(f'   from mac import MacApp\n\n')
        MacFile.close()

def CreateMacAppFile():
    ## MacApp File
    if ProjectOption == 1:
        print("> Creating MacApp Library...")
        with codecs.open(CreateEnvironment.MacAppFile, "w", "utf-8-sig") as MacAppFile:
            MacAppFile.write(f'## MacApp File\n')
            MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
            MacAppFile.write(f'from exception import Exceptions\n')
            MacAppFile.write(f'from mac import FileSystem\n\n')
            MacAppFile.write(f'def Main():\n')
            MacAppFile.write(f'   print("Hello World!")\n\n')
            MacAppFile.write(f'Main()\n')
            MacAppFile.close()

    elif ProjectOption == 2:
        print(">> Applying Loop Application on Environment on Mac...\n>> Please wait...")
        print("> Creating MacApp Library...")
        with codecs.open(CreateEnvironment.MacAppFile, "w", "utf-8-sig") as MacAppFile:
            MacAppFile.write(f'## MacApp File\n')
            MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
            MacAppFile.write(f'from exception import Exceptions\n')
            MacAppFile.write(f'from mac import FileSystem\n\n')
            MacAppFile.write(f'def Main():\n')
            MacAppFile.write(f'   while True:\n')
            MacAppFile.write(f'      print("="*80)\n')
            MacAppFile.write(f'      print(">> Options Menu<<")\n')
            MacAppFile.write(f'      print(">> 1. Option One")\n')
            MacAppFile.write(f'      print(">> 2. Option Two")\n')
            MacAppFile.write(f'      print(">> 3. Option Three")\n\n')
            MacAppFile.write(f'      try:\n')
            MacAppFile.write(f'         UserInput = int(input(">>[!] Type the option number: "))\n')
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

    elif ProjectOption == 3:
        with codecs.open(CreateEnvironment.MacAppFile, "w", "utf-8-sig") as MacAppFile:
            MacAppFile.write(f'## MacApp File\n')
            MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
            MacAppFile.write(f'import Tokens\n')
            MacAppFile.write(f'from exception import Exceptions\n')
            MacAppFile.write(f'from mac import FileSystem\n\n')
            MacAppFile.write(f'def NewTweet():\n')
            MacAppFile.write(f'   print("="*80)\n')
            MacAppFile.write(f'   print("NEW TWEET")\n')
            MacAppFile.write(f'   print("="*80)\n')
            MacAppFile.write(f'   Tweet = str(input(">>[!] Whats happening? "))\n')
            MacAppFile.write(f'   print("="*80)\n')
            MacAppFile.write(f'   print()\n')
            MacAppFile.write(f'   print("-"*80)\n')
            MacAppFile.write(f'   print(">> Your tweet was sent")\n')
            MacAppFile.write(f'   print("-"*80)\n')
            MacAppFile.write(f'   print()\n')
            MacAppFile.write(f'   print("="*80)\n\n')
            MacAppFile.write(f'   try:\n')
            MacAppFile.write(f'      Tokens.Twitter.update_status(Tweet)\n')
            MacAppFile.write(f"      print(f'>> Your last tweet:')\n")
            MacAppFile.write(f"      print(f' > {TweetStr}')\n")
            MacAppFile.write(f'      print("-" * 80)\n')
            MacAppFile.write(f'   except:\n')
            MacAppFile.write(f'      print(">>  Something went wrong: Unabled to connect to Twitter.")\n\n') 
            MacAppFile.write(f'def Main():\n')
            MacAppFile.write(f'   NewTweet()\n\n')
            MacAppFile.write(f'Main()\n')
            MacAppFile.close()

def CreateMacSplashScreen():
    ## Mac SplashScreen
    if ProjectOption == 3:
        with codecs.open(CreateEnvironment.SplashMac, "w", "utf-8-sig") as SplashMac:
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
            SplashMac.write(f'if CurrentYear == 2022:\n')
            SplashMac.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashMac.write(f'else:\n')
            SplashMac.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write("print(f'[{SoftwareName} for Mac] - Running...')\n")
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write(f"print(f'>> Checking Twitter connection. Please wait...')\n")
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write(f'print()')
            SplashMac.close()
    else:
        print("> Creating SplashScreen...")
        with codecs.open(CreateEnvironment.SplashMac, "w", "utf-8-sig") as SplashMac:
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
            SplashMac.write(f'if CurrentYear == 2022:\n')
            SplashMac.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashMac.write(f'else:\n')
            SplashMac.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write("print(f'[{SoftwareName} for Mac] - Running...')\n")
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write(f'print()\n')
            SplashMac.close()

def CreateMacFileSystem():
    ## Mac FileSystem
    print("> Creating Mac FileSystem Library...")
    with codecs.open(CreateEnvironment.MacFS, "w", "utf-8-sig") as MacFS:
        Mac = "User = f'/Users/{os.environ"
        FileSystem = '["USER"]}/'
        SUser = f"{Mac}{FileSystem}'"
        MacFS.write(f'## FileSystem\n')
        MacFS.write(f'## This file contains some default directories of your system\n\n')
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
        MacFS.write("Public = f'{User}Public/'\n\n")
        MacFS.write("## Project Directories\n")
        MacFS.write("PyBridgeFolder = f'{Documents}PyBridge/'\n")
        MacFS.write("ProjectsRepo = f'{PyBridgeFolder}Projects/'\n")
        MacFS.write("PythonExtension = '.py'\n")
        MacFS.close()

def CreateWindowsFile():
    print("="*80)
    print(">> Creating Windows Modules <<")
    print("="*80)
    
    ## Windows File
    print("> Creating Windows Library...")
    with codecs.open(CreateEnvironment.WindowsFile, "w", "utf-8-sig") as WindowsFile:
        WindowsFile.write(f'## Windows File\n')
        WindowsFile.write(f'## This file is used to implement code used to run scripts for Windows\n')
        WindowsFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        WindowsFile.write(f'import os\n')
        WindowsFile.write(f'from windows import FileSystem\n\n')
        WindowsFile.write(f'def Windows():\n')
        WindowsFile.write(f'   ## NOTE: You can use this function\n')
        WindowsFile.write(f'   ## To load information before the app starts running\n\n')
        WindowsFile.write(f'   ## Lets run the SplashScreen\n')
        WindowsFile.write(f'   from windows import SplashScreen\n\n')
        WindowsFile.write(f'   ## Lets check system requirements\n')
        WindowsFile.write(f'   from exception import Requirements\n\n')
        WindowsFile.write(f'   ## Start App for Windows\n')
        WindowsFile.write(f'   from windows import WindowsApp\n\n')
        WindowsFile.close()

def CreateWindowsAppFile():
    ## WindowsApp File
    if ProjectOption == 1:
        print("> Creating WindowsApp Library...")
        with codecs.open(CreateEnvironment.WindowsAppFile, "w", "utf-8-sig") as WindowsAppFile:
            WindowsAppFile.write(f'## WindowsApp File\n')
            WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
            WindowsAppFile.write(f'from exception import Exceptions\n')
            WindowsAppFile.write(f'from windows import FileSystem\n\n')
            WindowsAppFile.write(f'def Main():\n')
            WindowsAppFile.write(f'   print("Hello World!")\n\n') 
            WindowsAppFile.write(f'Main()\n')
            WindowsAppFile.close()
            
    elif ProjectOption == 2:
        print(">> Applying Loop Application on Environment on Windows...\n>> Please wait...")
        print("> Creating WindowsApp Library...")
        with codecs.open(CreateEnvironment.WindowsAppFile, "w", "utf-8-sig") as WindowsAppFile:
            WindowsAppFile.write(f'## WindowsApp File\n')
            WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
            WindowsAppFile.write(f'from exception import Exceptions\n')
            WindowsAppFile.write(f'from windows import FileSystem\n\n')
            WindowsAppFile.write(f'def Main():\n')
            WindowsAppFile.write(f'   while True:\n')
            WindowsAppFile.write(f'      print("="*80)\n')
            WindowsAppFile.write(f'      print(">> Options Menu<<")\n')
            WindowsAppFile.write(f'      print(">> 1. Option One")\n')
            WindowsAppFile.write(f'      print(">> 2. Option Two")\n')
            WindowsAppFile.write(f'      print(">> 3. Option Three")\n\n')
            WindowsAppFile.write(f'      try:\n')
            WindowsAppFile.write(f'         UserInput = int(input(">>[!] Type the option number: "))\n')
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
        
    elif ProjectOption == 3:
        with codecs.open(CreateEnvironment.WindowsAppFile, "w", "utf-8-sig") as WindowsAppFile:
            WindowsAppFile.write(f'## WindowsApp File\n')
            WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
            WindowsAppFile.write(f'import Tokens\n')
            WindowsAppFile.write(f'from exception import Exceptions\n')
            WindowsAppFile.write(f'from windows import FileSystem\n\n')
            WindowsAppFile.write(f'def NewTweet():\n')
            WindowsAppFile.write(f'   print("="*80)\n')
            WindowsAppFile.write(f'   print("NEW TWEET")\n')
            WindowsAppFile.write(f'   print("="*80)\n')
            WindowsAppFile.write(f'   Tweet = str(input(">>[!] Whats happening? "))\n')
            WindowsAppFile.write(f'   print("="*80)\n')
            WindowsAppFile.write(f'   print()\n')
            WindowsAppFile.write(f'   print("-"*80)\n')
            WindowsAppFile.write(f'   print(">> Your tweet was sent")\n')
            WindowsAppFile.write(f'   print("-"*80)\n')
            WindowsAppFile.write(f'   print()\n')
            WindowsAppFile.write(f'   print("="*80)\n\n')
            WindowsAppFile.write(f'   try:\n')
            WindowsAppFile.write(f'      Tokens.Twitter.update_status(Tweet)\n')
            WindowsAppFile.write(f"      print(f'>> Your last tweet:')\n")
            WindowsAppFile.write(f"      print(f' > {TweetStr}')\n")
            WindowsAppFile.write(f'      print("-" * 80)\n')
            WindowsAppFile.write(f'   except:\n')
            WindowsAppFile.write(f'      print(">>  Something went wrong: Unabled to connect to Twitter.")\n\n')  
            WindowsAppFile.write(f'def Main():\n')
            WindowsAppFile.write(f'   NewTweet()\n\n')
            WindowsAppFile.write(f'Main()\n')
            WindowsAppFile.close()
        
def CreateWindowsSplashScreen():
    ## Windows SplashScreen
    if ProjectOption == 3:
        with codecs.open(CreateEnvironment.SplashWindows, "w", "utf-8-sig") as SplashWindows:
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
            SplashWindows.write(f'if CurrentYear == 2022:\n')
            SplashWindows.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashWindows.write(f'else:\n')
            SplashWindows.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write("print(f'[{SoftwareName} for Windows] - Running...')\n")
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write(f"print(f'>> Checking Twitter connection. Please wait...')\n")
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write(f'print()')
            SplashWindows.close()
    else:
        print("> Creating SplashScreen...")
        with codecs.open(CreateEnvironment.SplashWindows, "w", "utf-8-sig") as SplashWindows:
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
            SplashWindows.write(f'if CurrentYear == 2022:\n')
            SplashWindows.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashWindows.write(f'else:\n')
            SplashWindows.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write("print(f'[{SoftwareName} for Windows] - Running...')\n")
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write(f'print()\n')
            SplashWindows.close()

def CreateWindowsFileSystem():
    ## Windows FileSystem
    print("> Creating Windows FileSystem Library...")
    with codecs.open(CreateEnvironment.WindowsFS, "w", "utf-8-sig") as WindowsFS:
        WindowsFS.write(f'## FileSystem\n')
        WindowsFS.write(f'## This file contains some default directories of your system\n\n')
        WindowsFS.write(f'import os\n\n')
        WindowsFS.write(f'## Special Directories\n')
        WindowsFS.write(f'CurrentPath = os.getcwd()\n')
        WindowsFS.write(f"User = os.environ['USERPROFILE']\n")
        WindowsFS.write("ApplicationData = f'{User}/AppData/Roaming/'\n")
        WindowsFS.write("Desktop = f'{User}/Desktop/'\n")
        WindowsFS.write("Documents = f'{User}/Documents/'\n")
        WindowsFS.write("Downloads = f'{User}/Downloads/'\n")
        WindowsFS.write("LocalAppData = f'{User}/AppData/Local/'\n")
        WindowsFS.write("Temp = f'{LocalAppData}Temp'\n")
        WindowsFS.write("Pictures = f'{User}/Pictures/'\n")
        WindowsFS.write("Favorites = f'{User}/Favorites/'\n\n")
        WindowsFS.write("## Project Directories\n")
        WindowsFS.write("PyBridgeFolder = f'{Documents}PyBridge/'\n")
        WindowsFS.write("ProjectsRepo = f'{PyBridgeFolder}Projects/'\n")
        WindowsFS.write("PythonExtension = '.py'\n")
        WindowsFS.close()

def CreateTokensFile():
    ## Tokens File
    print(">> Applying Twitter Application on Environment...\n>> Please wait...")
    with codecs.open(CreateEnvironment.TokensFile, "w", "utf-8-sig") as Tokens:
        Tokens.write(f'## Tokens\n')
        Tokens.write(f'## Setup and connect you Twitter account here!\n')
        Tokens.write(f'# Note: DO NOT share your tokens\n')
        Tokens.write(f'## You can generate and regenerate tokens on Twitter Developer Platform\n\n')
        Tokens.write(f'import tweepy\n')
        Tokens.write(f'from tweepy import OAuthHandler\n\n')
        Tokens.write(f'## API Key and API Key Secret\n')
        Tokens.write(f"ConsumerKey = str('')\n")
        Tokens.write(f"ConsumerSecret = str('')\n\n")
        Tokens.write(f'## Access Token and Access Token Secret\n')
        Tokens.write(f'AccessToken = str("")\n')
        Tokens.write(f'AccessTokenSecret = str("")\n\n')
        Tokens.write(f'## Authorization\n')
        Tokens.write(f'Auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)\n')
        Tokens.write(f'Auth.set_access_token(AccessToken, AccessTokenSecret)\n\n')
        Tokens.write(f'## Create an API Object\n')
        Tokens.write(f'Twitter = tweepy.API(Auth, wait_on_rate_limit = True)')
        Tokens.close()

def CreateBridge():
    print("="*80)
    print(">> CREATE PROJECT <<")
    print("="*80)
    ProjectName = str(input(">>[!] Project Name: "))
    print(f'>> Creating bridge to the project "{ProjectName}"...')
    print()
    
    try:
        FolderLocation = f'{FileSystem.ProjectsRepo}{ProjectName}/'
        os.mkdir(FolderLocation)
        Explorer.ProjectName = ProjectName
        Explorer.FolderLocation = FolderLocation
        CreateEnvironment()
    except:
        print()
        print("="*80)
        print(">> Could not create your project:")
        print(f'> Check if "{ProjectName}" already exists and try again.')
        print("="*80)
        # Exceptions.Log(Message = "Criar arquivo de LOG: Arquivo já existente!", Location = FileSystem.CurrentPath + "NomeArquivo.log")
        Exceptions.FileExists()
        
    ### Project Structure ###
    CreateEnvironment()
    ## Init File
    CreateInitFile()
    ## Readme File
    CreateReadmeFile()
    ## Exceptions File
    CreateExceptions()
    ## Requirements File
    CreateRequirements()
    print("="*80)
    print()

    if ProjectOption == 3:
        CreateTokensFile()

    ### Linux Module ###
    ## Linux File
    CreateLinuxFile()
    ## LinuxApp File
    CreateLinuxAppFile()
    ## Linux SplashScreen File
    CreateLinuxSplashScreen()
    ## Linux FileSystem File
    CreateLinuxFileSystem()
    print("="*80)
    print()
    
    ### macOS Modules ###
    ## Mac File
    CreateMacFile()
    ## MacApp File
    CreateMacAppFile()
    ## Mac SplashScreen File
    CreateMacSplashScreen()
    ## Mac FileSystem File
    CreateMacFileSystem()
    print("="*80)
    print()

    ### Windows Modules ###
    ## Windows File
    CreateWindowsFile()
    ## WindowsApp File
    CreateWindowsAppFile()
    ## Windows SplashScreen File
    CreateWindowsSplashScreen()
    ## Windows FileSystem File
    CreateWindowsFileSystem()

    print("="*80)
    print(f'>> The bridge to the project "{Explorer.ProjectName}" was created successfully!')
    print("="*80)
    print()

    print("="*80)
