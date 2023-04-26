"""
MacApp.py

- This file is used to implement code used to run scripts for Mac
"""
## MacApp File
## This file is used to implement code used to run scripts for Mac

from exception import Exceptions
from mac import Core
from mac import SplashScreen
from system import Services

def Run():
    BridgeLoop = True

    while BridgeLoop == True:
        print()
        print("="*80)
        print(">> MENU <<")
        print("="*80)
        print("[1] - New Project...")
        print("[2] - Projects List")
        print("[3] - Backup Projects")
        print("[4] - Sample Projects...")
        print("[0] - Quit PyBridge")
        print()

        try:
            Opc = int(input(">>[!] Type The Item Number: "))
            print()

            if Opc == 0:
                BridgeLoop = False
                print("=" * 80)
                print(f'[{SplashScreen.SoftwareName}] - Quit')
                print("=" * 80)
                try:
                    quit()
                except:
                    return

            elif Opc == 1:
                NewProjectMenu()

            elif Opc == 2:
                Core.ProjectList()
                
            elif Opc == 3:
                Core.Backup()

            elif Opc == 4:
                Services.DownloadSamplesMenu()
            else:
                Exceptions.Throw.InvalidOption()
        except:
            Exceptions.Throw.InputFormat()

def NewProjectMenu():
    print("="*80)
    print(">> NEW PROJECT <<")
    print("="*80)
    print("[1] - Create Blank Project")
    print("[2] - Create a Menu Application Loop Project")
    print("[3] - Create Twitter Application Project")
    print("[4] - Create a Jupyter Notebook")
    print("[0] - << Go Back")
    print()

    try:
        Opc = int(input(">>[!] Type The Item Number: "))
        Core.ProjectOption = Opc
        print()

        if Opc == 0:
            return

        elif Opc == 1:
            Core.ProjectType = "PyBridge Blank Project"
            Core.CreateBridge()

        elif Opc == 2:
            Core.ProjectType = "Menu Application Loop Project"
            Core.CreateBridge()

        elif Opc == 3:
            Core.ProjectType = "Twitter Application Project"
            Core.CreateBridge()

        elif Opc == 4:
            Core.ProjectType = "Jupyter Notebook Project"
            Core.CreateBridge()

        else:
            Exceptions.Throw.InvalidOption()
    except:
        Exceptions.Throw.InputFormat()