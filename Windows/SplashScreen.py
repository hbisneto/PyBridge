## SplashScreen File
## This file contains information about your project

from datetime import date

CurrentYear = date.today().year
SoftwareName = "PyBridge"
Version = "BETA 6"
CopyrightName = "Heitor Bisneto"

print("="*80)
print(f'[{SoftwareName} for Windows] - Running...')
print("="*80)

print(f'Name: {SoftwareName}')
print(f'Version: {Version}')
print(f'Created By: {CopyrightName}')

if CurrentYear == 2021:
    print(f'Copyright © {CurrentYear} | {CopyrightName}. All rights reserved.')
    print("="*80)
else:
    print(f'Copyright © 2021 - {CurrentYear} | {CopyrightName}. All rights reserved.')
    print("="*80)
