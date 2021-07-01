## Core

import os

CurrentPath = os.getcwd()
DocumentsFolder = f'/home/{os.environ["USER"]}/Documents/'
PyBridgeFolder = f'{DocumentsFolder}PyBridge/'
ProjectsRepo = f'{PyBridgeFolder}Projects/'

PytPythonExtension = ".py"

def VerifyFolders():
    try:
        print(">> PyBridge: Checking System...")
        os.mkdir(PyBridgeFolder)
        os.mkdir(ProjectsRepo)
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
        FolderLocation = f'{ProjectsRepo}{ProjectName}/'
        from Linux import FileSystem
        os.mkdir(FolderLocation)
        FileSystem.ProjectName = ProjectName
        FileSystem.FolderLocation = FolderLocation
        FileSystem.EnvironFolders()
        print("="*80)
        print(f'>> The bridge to the project "{ProjectName}" was created successfully!')
        print("="*80)
    except:
        print()
        print(">> Could not create your project:")
        print(f'> Check if "{ProjectName}" already exists and try again.')
        from ErrorReport import ErrorList
        ErrorList.FileExists()

