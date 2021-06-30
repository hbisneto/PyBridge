## Core

import os

CurrentPath = os.getcwd()
DocumentsFolder = f'/home/{os.environ["USER"]}/Documents/'
PyBridgeFolder = f'{DocumentsFolder}PyBridge/'
ProjectsRepo = f'{PyBridgeFolder}Projects/'

PythonExtension = ".py"

def VerifyFolders():
    try:
        print(">> PyBridge: Checking System...")
        os.mkdir(PyBridgeFolder)
        os.mkdir(ProjectsRepo)
        print(">> PyBridge System Files: OK!")
    except:
        print(">> PyBridge System Files: OK!")

def CreateProject():
    print("="*80)
    print(">> CREATE PROJECT")
    print("="*80)
    ProjectName = str(input(">> Project Name: "))
    print(f'>> Creating Project "{ProjectName}"...')
    try:
        FolderLocation = f'{ProjectsRepo}{ProjectName}/'
        from Mac import FileSystem
        os.mkdir(FolderLocation)
        FileSystem.ProjectName = ProjectName
        FileSystem.FolderLocation = FolderLocation
        FileSystem.EnvironFolders()
        print(f'>> The project "{ProjectName}" was created successfully!')
    except:
        print()
        print(">> Could not create your project:")
        print(f'> Check if "{ProjectName}" already exists and try again.')
        from ErrorReport import ErrorList
        ErrorList.FileExists()

