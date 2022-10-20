## SplashScreen File
## This file contains information about your project

import getpass
from datetime import datetime

CurrentYear = datetime.now().year
SoftwareName = "PyBridge"
Version = "2.0"
CopyrightName = "Heitor Bisneto"

Now = datetime.now()
Hour = int(Now.strftime("%H"))
Minute = int(Now.strftime("%M"))
Second = int(Now.strftime("%S"))
TimeAccess = Now.strftime("%H:%M:%S")
UserName = getpass.getuser().capitalize()

def Main():    
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

def Salutation():
    
    if Hour >= 6 and Hour < 12:
        DayPeriod = "Morning"
        print(f'Hello {UserName}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    elif Hour >= 12 and Hour < 18:
        DayPeriod = "Afternoon"
        print(f'Hello {UserName}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    elif Hour >= 18 and Hour != 0:
        DayPeriod = "Evening"
        print(f'Hello {UserName}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    else:
        print(f'Hello {UserName}. Nice to see you! - {TimeAccess}')
        print("="*80)
        
Main()
Salutation()