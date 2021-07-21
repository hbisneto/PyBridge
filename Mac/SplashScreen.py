## SplashScreen File
## This file contains information about your project

from datetime import date
import getpass

CurrentYear = date.today().year
SoftwareName = "PyBridge"
Version = "BETA 5"
CopyrightName = getpass.getuser().capitalize()

print("Name:", SoftwareName)
print("Version:", Version)
print("Created By:", CopyrightName)

if CurrentYear == 2021:
    print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", CurrentYear, "|", CopyrightName, "All rights reserved.")
print()
print("="*80)
print(f'[{SoftwareName} for Mac] - Running...')
print("="*80)
print()
