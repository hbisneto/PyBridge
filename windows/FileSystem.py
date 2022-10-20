## FileSystem
## This file contains some default directories of your system

import os

PythonExtension = '.py'

## Special Directories
CurrentPath = os.getcwd()
User = os.environ['USERPROFILE']

ApplicationData = f'{User}/AppData/Roaming/'
Desktop = f'{User}/Desktop/'
Documents = f'{User}/Documents/'
Downloads = f'{User}/Downloads/'
LocalAppData = f'{User}/AppData/Local/'
Temp = f'{LocalAppData}Temp'
Pictures = f'{User}/Pictures/'
Favorites = f'{User}/Favorites/'

## Project Directories
Backup = f'{CurrentPath}/Backup/'
Sample = f'{CurrentPath}/Sample/'
GetInfo = f'{Sample}GetInfo/'
JoKenPo = f'{Sample}JoKenPo/'
PyBridgeFolder = f'{Documents}PyBridge/'
ProjectsRepo = f'{PyBridgeFolder}Projects/'