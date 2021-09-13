## WindowsApp File
## This file is used to implement code used to run scripts for Windows

from Windows import Core

def Main():
    BridgeLoop = True
    Core.VerifyFolders()
    while BridgeLoop == True:
        print("="*80)
        print(">> MENU")
        print("="*80)
        print(">> 1. Create Blank Project")
        print(">> 2. Create a Menu Application Loop Project")
        print(">> 3. Create Twitter Application Project")
        print(">> 4. Projects List")
        print(">> 0. Quit PyBridge")
        print()
        Opc = int(input(">> Type The Item Number: "))
        print("="*80)

        if Opc == 0:
            BridgeLoop = False
        elif Opc == 1:
            Core.ProjectOption = 1
            Core.ProjectType = "PyBridge Blank Project"
            Core.CreateProject()
            Core.CreationSuccess()
        elif Opc == 2:
            Core.ProjectOption = 2
            Core.ProjectType = "Menu Application Loop Project"
            Core.CreateProject()
            Core.ApplyLoopApp()
            Core.CreationSuccess()
        elif Opc == 3:
            Core.ProjectOption = 3
            Core.ProjectType = "Twitter Application Project"
            Core.CreateProject()
            Core.ApplyTwitterProject()
            Core.CreationSuccess()
        elif Opc == 4:
            Core.ProjList.clear()
            Core.ListProjects()
            Core.ProjectList()
        else:
            print("="*80)
            print(">> Invalid Option!")
            print("="*80)
            print(f'>> You typed an invalid option.\n>> Run the program again!')
            print("="*80)
    
Main()
