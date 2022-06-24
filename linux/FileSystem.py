## FileSystem
## This file contains some default directories of your system

import os

PythonExtension = '.py'

## Special Directories
CurrentPath = os.getcwd()
User = f'/home/{os.environ["USER"]}/'

Desktop = f'{User}Desktop/'
Documents = f'{User}Documents/'
Downloads = f'{User}Downloads/'
Music = f'{User}Music/'

## Project Directories
Backup = f'{CurrentPath}/Backup/'
Sample = f'{CurrentPath}/Sample/'
PyBridgeFolder = f'{Documents}PyBridge/'
ProjectsRepo = f'{PyBridgeFolder}Projects/'
