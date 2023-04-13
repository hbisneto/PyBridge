"""
FileSystem.py

- This file contains some default directories of your system
- You can use this file to implement custom directories used by your application
"""
## FileSystem
## This file contains some default directories of your system
## You can use this file to implement custom directories used by your application

import os

PythonExtension = '.py'

## SPECIAL DIRECTORIES
CurrentPath = os.getcwd()
User = f'/Users/{os.environ["USER"]}/'

## SYSTEM DIRECTORIES
Applications = f'{User}Applications/'
Desktop = f'{User}Desktop/'
Documents = f'{User}Documents/'
Downloads = f'{User}Downloads/'
Movies = f'{User}Movies/'
Music = f'{User}Music/'
Pictures = f'{User}Pictures/'
Public = f'{User}Public/'

## PROJECT DIRECTORIES
Backup = f'{CurrentPath}/Backup/'
Sample = f'{CurrentPath}/Sample/'
GetInfo = f'{Sample}GetInfo/'
JoKenPo = f'{Sample}JoKenPo/'
PyBridgeFolder = f'{Documents}PyBridge/'
ProjectsRepo = f'{PyBridgeFolder}Projects/'

### OTHER IMPLEMENTATION
# Folders Verified to assure PyBridge Will Run Properly
def VerifyFolders():
    try:
        os.mkdir(PyBridgeFolder)
        print(f'>> PyBridge: "{PyBridgeFolder}" created')
    except:
        pass

    try:
        os.mkdir(ProjectsRepo)
        print(f'>> PyBridge: "{ProjectsRepo}" created')
    except:
        pass