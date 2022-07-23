## MacApp File
## This file is used to implement code used to run scripts for Mac

from exception import Exceptions
from mac import Core

def Main():
    BridgeLoop = True
    Core.VerifyFolders()

    while BridgeLoop == True:
        print()
        print("="*80)
        print(">> MENU <<")
        print("="*80)
        print("[1] - Create Blank Project")
        print("[2] - Create a Menu Application Loop Project")
        print("[3] - Create Twitter Application Project")
        print("[4] - Create a Jupyter Notebook")
        print("[5] - Projects List")
        print("[6] - Backup Projects")
        print("[7] - Sample Projects...")
        print("[0] - Quit PyBridge")
        print()

        try:
            Opc = int(input(">>[!] Type The Item Number: "))
            print()

            if Opc == 0:
                BridgeLoop = False
                quit()

            elif Opc == 1:
                Core.ProjectOption = 1
                Core.ProjectType = "PyBridge Blank Project"
                Core.CreateBridge()

            elif Opc == 2:
                Core.ProjectOption = 2
                Core.ProjectType = "Menu Application Loop Project"
                Core.CreateBridge()

            elif Opc == 3:
                Core.ProjectOption = 3
                Core.ProjectType = "Twitter Application Project"
                Core.CreateBridge()

            elif Opc == 4:
                Core.ProjectOption = 4
                Core.ProjectType = "Jupyter Notebook Project"
                Core.CreateBridge()

            elif Opc == 5:
                Core.ProjList.clear()
                Core.ProjectList()
                
            elif Opc == 6:
                Core.Backup()

            elif Opc == 7:
                print("="*80)
                print(">> DOWNLOAD SAMPLE CODE <<")
                print("="*80)
                print('>>[1] - Download "GetInfo"...')
                print('>>[2] - Download "JoKenPo"')
                print('>>[0] - << Go Back')
                print()
                UserOption = int(input('>>[!] Type The Item Number: '))

                if UserOption == 0:
                    print("="*80)
                elif UserOption == 1:
                    Core.DownloadSample().GetInfo()
                elif UserOption == 2:
                    Core.DownloadSample().Jokenpo()
                else:
                    Exceptions.Throw.InvalidOption()
            else:
                Exceptions.Throw.InvalidOption()
        except:
            Exceptions.Throw.ProgramQuit()
Main()
