## FileSystem
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
    
    # Linux
    SplashLinux = open(EnvironFolders.SplashLinux, "w")
    LinuxFile = open(EnvironFolders.LinuxFile, "w")
    LinuxAppFile = open(EnvironFolders.LinuxAppFile, "w")
    # Mac
    SplashMac = open(EnvironFolders.SplashMac, "w")
    MacFile = open(EnvironFolders.MacFile, "w")
    MacAppFile = open(EnvironFolders.MacAppFile, "w")
    # Windows
    SplashWindows = open(EnvironFolders.SplashWindows, "w")
    WindowsFile = open(EnvironFolders.WindowsFile, "w")
    WindowsAppFile = open(EnvironFolders.WindowsAppFile, "w")

def EnvironFolders():
    # Environment Folders
    EnvironFolders.ErrorReportPath = f'{FolderLocation}ErrorReport/'
    EnvironFolders.LinuxPath = f'{FolderLocation}Linux/'
    EnvironFolders.MacPath = f'{FolderLocation}Mac/'
    EnvironFolders.WindowsPath = f'{FolderLocation}Windows/'

    ## Environment Files
    EnvironFolders.UserAppName = f'{FolderLocation}{ProjectName}.py'
    EnvironFolders.ReadmeFile = f'{FolderLocation}README.md'
    EnvironFolders.ErrorListFile = f'{EnvironFolders.ErrorReportPath}ErrorList.py'
    
    # Linux
    EnvironFolders.SplashLinux = f'{EnvironFolders.LinuxPath}SplashScreen.py'
    EnvironFolders.LinuxFile = f'{EnvironFolders.LinuxPath}Linux.py'
    EnvironFolders.LinuxAppFile = f'{EnvironFolders.LinuxPath}LinuxApp.py'
    # Mac
    EnvironFolders.SplashMac = f'{EnvironFolders.MacPath}SplashScreen.py'
    EnvironFolders.MacFile = f'{EnvironFolders.MacPath}Mac.py'
    EnvironFolders.MacAppFile = f'{EnvironFolders.MacPath}MacApp.py'
    # Windows
    EnvironFolders.SplashWindows = f'{EnvironFolders.WindowsPath}SplashScreen.py'
    EnvironFolders.WindowsFile = f'{EnvironFolders.WindowsPath}Windows.py'
    EnvironFolders.WindowsAppFile = f'{EnvironFolders.WindowsPath}WindowsApp.py'

    CreateArch()
    CreateFiles()
    CreateBridge()

def WriteMyApp():
    ## Launcher Script
    WriteApp = open(EnvironFolders.UserAppName, "a")
    WriteApp.write(f'## {ProjectName} File\n')
    WriteApp.write(f'## Here the contents will be processed to choose the best platform to go\n\n')

    WriteApp.write(f'try:\n')
    WriteApp.write(f'   # Imported Libraries\n')
    WriteApp.write(f'   from sys import platform\n\n')

    WriteApp.write(f'   # Local Libraries\n')
    WriteApp.write(f'   from ErrorReport import ErrorList\n')
    WriteApp.write(f'   from Linux import Linux\n')
    WriteApp.write(f'   from Mac import Mac\n')
    WriteApp.write(f'   from Windows import Windows\n\n')

    WriteApp.write(f'   Platform = platform\n\n')
        
    WriteApp.write(f'except:\n')
    WriteApp.write(f'   ErrorList.ImportLib()\n\n')

    WriteApp.write(f'def Main():\n')
        
    WriteApp.write(f'   if Platform == "linux" or Platform == "linux2":\n')
    WriteApp.write(f'      # Linux\n')
    WriteApp.write(f'      Linux.Linux()\n\n')
            
    WriteApp.write(f'   elif Platform == "darwin":\n')
    WriteApp.write(f'      # Mac\n')
    WriteApp.write(f'      Mac.Mac()\n\n')
            
    WriteApp.write(f'   elif Platform == "win32":\n')
    WriteApp.write(f'      # Windows\n')
    WriteApp.write(f'      Windows.Windows()\n\n')
            
    WriteApp.write(f'Main()')

    # README File
    
    WriteMD = open(EnvironFolders.ReadmeFile, "a")
    WriteMD.write(f'# {ProjectName}\n\n')
    WriteMD.write(f'This project was created using PyBridge\n')
    
def WriteExceptions():
    WriteExc = open(EnvironFolders.ErrorListFile, "a")
    WriteExc.write(f'## ErrorList File\n')
    WriteExc.write(f'## This file contains events thats raised when the program must to stop\n\n')

    WriteExc.write(f'def ImportLib():\n')
    WriteExc.write(f'   raise RuntimeError(">> Erro ao importar biblioteca: Verifique se as bibliotecas do sistema estão instaladas e execute o programa novamente.")\n\n')

    WriteExc.write(f'def FileExists():\n')
    WriteExc.write(f'   raise RuntimeError(">> O arquivo já existe: Verifique o arquivo e tente novamente...")\n\n')

def WriteLinuxFiles():
    # Linux
    Splash = open(EnvironFolders.SplashLinux, "a")

    Splash.write(f'## SplashScreen File\n')
    Splash.write(f'## This file contains information about your project\n\n')

    Splash.write(f'from datetime import date\n')
    Splash.write(f'import getpass\n\n')

    Splash.write(f'AnoAtual = date.today().year\n')
    Splash.write(f'SoftwareName = "{ProjectName}"\n')
    Splash.write(f'Version = "1.0"\n')
    Splash.write(f'CopyrightName = getpass.getuser().capitalize()\n\n')

    Splash.write(f'print("Nome:", SoftwareName)\n')
    Splash.write(f'print("Versão:", Version)\n')
    Splash.write(f'print("Criado por:", CopyrightName)\n\n')

    Splash.write(f'if AnoAtual == 2021:\n')
    Splash.write(f'   print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")\n')
    Splash.write(f'else:\n')
    Splash.write(f'   print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")\n\n')
    Splash.write(f'print("="*80)\n')
    Splash.write("print(f'[{SoftwareName} for Linux] - Em Execução...')\n")
    Splash.write(f'print("="*80)\n')

    # Linux File
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

    # LinuxApp File
    LinuxAppFile = open(EnvironFolders.LinuxAppFile, "a")
    LinuxAppFile.write(f'## LinuxApp File\n')
    LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')

    LinuxAppFile.write(f'def Main():\n')
    LinuxAppFile.write(f'   print("Hello World!")\n\n')
        
    LinuxAppFile.write(f'Main()\n')
    
def WriteMacFiles():
    # SplashScreen
    Splash = open(EnvironFolders.SplashMac, "a")

    Splash.write(f'## SplashScreen File\n')
    Splash.write(f'## This file contains information about your project\n\n')

    Splash.write(f'from datetime import date\n')
    Splash.write(f'import getpass\n\n')

    Splash.write(f'AnoAtual = date.today().year\n')
    Splash.write(f'SoftwareName = "{ProjectName}"\n')
    Splash.write(f'Version = "1.0"\n')
    Splash.write(f'CopyrightName = getpass.getuser().capitalize()\n\n')

    Splash.write(f'print("Nome:", SoftwareName)\n')
    Splash.write(f'print("Versão:", Version)\n')
    Splash.write(f'print("Criado por:", CopyrightName)\n\n')

    Splash.write(f'if AnoAtual == 2021:\n')
    Splash.write(f'   print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")\n')
    Splash.write(f'else:\n')
    Splash.write(f'   print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")\n\n')
    Splash.write(f'print("="*80)\n')
    Splash.write("print(f'[{SoftwareName} for Mac] - Em Execução...')\n")
    Splash.write(f'print("="*80)\n')

    # Mac File
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

    # MacApp File
    MacAppFile = open(EnvironFolders.MacAppFile, "a")
    MacAppFile.write(f'## MacApp File\n')
    MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')

    MacAppFile.write(f'def Main():\n')
    MacAppFile.write(f'   print("Hello World!")\n\n')
        
    MacAppFile.write(f'Main()\n')
    
def WriteWindowsFiles():
    Splash = open(EnvironFolders.SplashWindows, "a")

    Splash.write(f'## SplashScreen File\n')
    Splash.write(f'## This file contains information about your project\n\n')

    Splash.write(f'from datetime import date\n')
    Splash.write(f'import getpass\n\n')

    Splash.write(f'AnoAtual = date.today().year\n')
    Splash.write(f'SoftwareName = "{ProjectName}"\n')
    Splash.write(f'Version = "1.0"\n')
    Splash.write(f'CopyrightName = getpass.getuser().capitalize()\n\n')

    Splash.write(f'print("Nome:", SoftwareName)\n')
    Splash.write(f'print("Versão:", Version)\n')
    Splash.write(f'print("Criado por:", CopyrightName)\n\n')

    Splash.write(f'if AnoAtual == 2021:\n')
    Splash.write(f'   print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")\n')
    Splash.write(f'else:\n')
    Splash.write(f'   print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")\n\n')
    Splash.write(f'print("="*80)\n')
    Splash.write("print(f'[{SoftwareName} for Windows] - Em Execução...')\n")
    Splash.write(f'print("="*80)\n')

    # Windows File
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

    # WindowsApp File
    WindowsAppFile = open(EnvironFolders.WindowsAppFile, "a")
    WindowsAppFile.write(f'## WindowsApp File\n')
    WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')

    WindowsAppFile.write(f'def Main():\n')
    WindowsAppFile.write(f'   print("Hello World!")\n\n')
        
    WindowsAppFile.write(f'Main()\n')

def CreateBridge():
    print(">> Creating Bridge...")
    WriteMyApp()
    print(">> Creating ErrorReports Module...")
    WriteExceptions()
    print(">> Creating Linux Modules...")
    WriteLinuxFiles()
    print(">> Creating Mac Modules...")
    WriteMacFiles()
    print(">> Creating Windows Modules...")
    WriteWindowsFiles()

    ## Nome do projeto
    # Salvar no local preestabelecido

    # Criar o arquivo Core pra verificar e criar as pastas do sistema
