## WindowsApp File
## This file is used to implement code used to run scripts for Windows

from Windows import Core

def Main():
    Core.VerifyFolders()
    print("="*80)
    print(">> MENU")
    print("="*80)
    print(">> 1. Create Project")
    print()
    Opc = int(input(">> Type The Item Number: "))

    if Opc == 1:
        Core.CreateProject()
    else:
        print("="*80)
        print(">> Invalid Option!")
        print("="*80)
        print(f'>> You typed an invalid option.\n>> Run the program again!')
        print("="*80)
    
Main()
