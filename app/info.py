"""
### info.py

- This file contains information about your project
"""

import getpass
import sys
from datetime import date
from datetime import datetime
from sys import platform

NAME = "PyBridge"
VERSION = "3.0"
COPYRIGHT = "Heitor Bisneto"
TYPE = "Menu Application Loop"
LICENCE = "MIT"
USERNAME_CURRENT = getpass.getuser().capitalize()

### PYTHON RUNNING VERSION
MAJOR_VERSION = sys.version_info[0]
MINOR_VERSION = sys.version_info[1]
BUILD_VERSION = sys.version_info[2]
CURRENT_PYTHON_VERSION = f'{MAJOR_VERSION}.{MINOR_VERSION}.{BUILD_VERSION}'
### PYTHON RUNNING VERSION

CURRENT_YEAR = date.today().year
NOW = datetime.now()
HOUR = int(NOW.strftime("%H"))
TIME_ACCESS = NOW.strftime("%H:%M:%S")

### UNCOMMENT TO USE VARIABLES
# Minute = int(Now.strftime("%M"))
# Second = int(Now.strftime("%S"))
### UNCOMMENT TO USE VARIABLES
        
def load_splashscreen():
    print("="*80)
    print(f'[{NAME} for {PLATFORM_NAME}] - Running...')
    print("="*80)

    print(f'Name: {NAME}')
    print(f'Version: {VERSION}')
    print(f'Created By: {COPYRIGHT}')

    if CURRENT_YEAR == 2021:
        print(f'Copyright © {CURRENT_YEAR} | {COPYRIGHT}. All rights reserved.')
        print("="*80)
    else:
        print(f'Copyright © 2021 - {CURRENT_YEAR} | {COPYRIGHT}. All rights reserved.')
        print("="*80)

    if HOUR >= 6 and HOUR < 12:
        DAY_PERIOD = "Morning"
        print(f'Hello {USERNAME_CURRENT}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
        print("="*80)
    elif HOUR >= 12 and HOUR < 18:
        DAY_PERIOD = "Afternoon"
        print(f'Hello {USERNAME_CURRENT}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
        print("="*80)
    elif HOUR >= 18 and HOUR != 0:
        DAY_PERIOD = "Evening"
        print(f'Hello {USERNAME_CURRENT}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
        print("="*80)
    else:
        print(f'Hello {USERNAME_CURRENT}. Nice to see you! - {TIME_ACCESS}')
        print("="*80)

## Linux
if platform == "linux" or platform == "linux2":
    PLATFORM_NAME = "Linux"
## Mac
elif platform == "darwin":
    PLATFORM_NAME = "Mac"
## Windows
elif platform == "win32" or platform == "win64":
    PLATFORM_NAME = "Windows"