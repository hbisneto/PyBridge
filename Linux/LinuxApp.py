## LinuxApp File
## This file is used to implement code used to run scripts for Linux.

from ErrorReport import ErrorList
from Linux import Core

de Main():
    BridgeLoop = True
    Core.VerifyFolders()

    while BridgeLoop == True:
        print("="*80)
        print(">> MENU <<")
        print("="*80)
        print(">>[1] - Create Blank Project")
        print(">>[2] - Create a Menu Application Loop Project")
        print(">>[3] - Create Twitter Application Project")
        print(">>[4] - Projects List")
        print(">>[5] - Backup Projects")
        print(">>[0] - Quit PyBridge")
        print()
        Opc = int(input(">>[!] Type The Item Number: "))
        print()

        if Opc == 0:
            BridgeLoop = False
            quit()

        elif Opc == 1:
            Core.ProjectOption = 1
            Core.ProjectType = "PyBridge Blank Project"
            Core.CreateBridge()
            Core.CreationSuccess()

        elif Opc == 2:
            Core.ProjectOption = 2
            Core.ProjectType = "Menu Application Loop Project"
            Core.CreateBridge()
            Core.CreationSuccess()

        elif Opc == 3:
            Core.ProjectOption = 3
            Core.ProjectType = "Twitter Application Project"
            Core.CreateBridge()
            Core.CreationSuccess()

        elif Opc == 4:
            Core.ProjList.clear()
            Core.ProjectList()
            
        elif Opc == 5:
            Core.Backup()

        else:
            ErrorList.InvalidOption()
    
Main()
