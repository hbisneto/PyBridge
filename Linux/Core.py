## Core

import os

CurrentPath = os.getcwd()
DocumentsFolder = f'/home/{os.environ["USER"]}/Documents/'
PyBridgeFolder = f'{DocumentsFolder}PyBridge/'
ProjectsRepo = f'{PyBridgeFolder}Projects/'

PythonExtension = ".py"

def VerifyFolders():
    try:
        print(">> PyBridge: Verificando Sistema...")
        os.mkdir(PyBridgeFolder)
        os.mkdir(ProjectsRepo)
        print(">> PyBridge: Verificação Concluída.")
    except:
        print(">> PyBridge: Verificação Concluída.")

def CreateProject():
    print("="*80)
    print(">> CRIAR PROJETO")
    print("="*80)
    ProjectName = str(input(">> Project Name: "))
    print(f'>> Criando projeto "{ProjectName}"...')
    try:
        FolderLocation = f'{ProjectsRepo}{ProjectName}/'
        from Mac import FileSystem
        os.mkdir(FolderLocation)
        FileSystem.ProjectName = ProjectName
        FileSystem.FolderLocation = FolderLocation
        FileSystem.EnvironFolders()
        print(f'>> Seu projeto "{ProjectName}" foi criado com sucesso!')
    except:
        print()
        print(">> Não foi possível criar o projeto:")
        print(f'> Provavelmente já exista um projeto com o nome "{ProjectName}".\n> Verifique o projeto e tente novamente...')
        from ErrorReport import ErrorList
        ErrorList.ProjectExists()

