## WindowsApp File
## This file is used to implement code used to run scripts for Windows

from Windows import Core

def Main():
    Core.VerifyFolders()
    while True:
        print("="*80)
        print(">> MENU")
        print("="*80)
        print(">> 1. Create Project")
        print(">> 2. Create a 'LoopingMenu' Project")
        print()
        Opc = int(input(">> Type The Item Number: "))
        print("="*80)

        if Opc == 1:
            Core.CreateProject()
        elif Opc == 2:
            Core.LoopApp = True
            Core.CreateProject()
        else:
            print("="*80)
            print(">> Invalid Option!")
            print("="*80)
            print(f'>> You typed an invalid option.\n>> Run the program again!')
            print("="*80)
    
Main()
