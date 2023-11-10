"""
### requirements.py

- This file is used to check if system matches with the minimum requirements to run
"""

import sys
import subprocess
from exceptions import exception as ex

## Change "REQUIRE" to "False" to skip system check
REQUIRE = True
## Change "REQUIRE" to "True" to allow system check

if REQUIRE == True:
   ## Target System
   target_major = 3
   target_minor = 9
   target_build = 0
   target_version = f'{target_major}.{target_minor}.{target_build}'
   target_ver_str = f'{target_major}{target_minor}{target_build}'
   target_ver_int = int(target_ver_str)
   ## Target System

   ## Current System
   current_major = sys.version_info[0]
   current_minor = sys.version_info[1]
   current_build = sys.version_info[2]
   current_version = f'{current_major}.{current_minor}.{current_build}'
   current_ver_str = f'{current_major}{current_minor}{current_build}'
   current_ver_int = int(current_ver_str)
   ## Current System

   ## Uncomment to see information about your system
   ## print(f'>> My system current version: Python {current_version}')
   ## print(f'>> Required version to run: Python {target_version}')

   def check_version():
      if target_ver_int < current_ver_int:
         ex.throw.minor_version(current_version, target_version)
      elif target_ver_int > current_ver_int:
         ex.throw.major_version(current_version, target_version)
      else:
         pass

   def install_dependencies():
      print()
      print("=" * 80)
      print(">> INSTALL DEPENDENCIES <<")
      print("=" * 80)
      user_input = str(input("[ ! ] >> Do you wish to install dependencies? [Y/n]: "))

      if user_input == "Y" or user_input == "y" or user_input == "1":
         # show pip version
         print("=" * 80)
         print("[ ! ]: PIP Version: [Getting information about installed PIP version...]")
         print("=" * 80)
         cmd = subprocess.getoutput("pip --version")
         print("Details: ", cmd)
         print("=" * 80)

         # Update pip
         print()
         print("=" * 80)
         print("[ ! ]: Checking necessary packages: [Updating pip e pip3]")
         print("=" * 80)
         cmd = subprocess.getoutput("pip install --upgrade pip")
         print("Details: ", cmd)
         cmd = subprocess.getoutput("pip3 install --upgrade pip")
         print("Details: ", cmd)
         print("=" * 80)
         
         # Install Requests
         print()
         print("=" * 80)
         print("[ ! ]: Checking necessary packages: [Installing/updating requests]")
         print("=" * 80)
         cmd = subprocess.getoutput("pip install requests")
         print("Details: ", cmd)
         print("=" * 80)
      else:
         print("=" * 80)
         return
