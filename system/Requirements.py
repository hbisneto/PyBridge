## Requirements File
## This file is used to check if system matches with the minimum requirements to run

import sys
import subprocess
from exception import Exceptions

## Change "REQUIRE" to "False" to skip system check
REQUIRE = True
## Change "REQUIRE" to "True" to allow system check

if REQUIRE == True:
   ## Target System
   TargetMajor = 3
   TargetMinor = 9
   TargetBuild = 0
   TargetVersion = f'{TargetMajor}.{TargetMinor}.{TargetBuild}'
   ## Target System

   ## Current System
   MajorVersion = sys.version_info[0]
   MinorVersion = sys.version_info[1]
   BuildVersion = sys.version_info[2]
   CurrentVersion = f'{MajorVersion}.{MinorVersion}.{BuildVersion}'
   ## Current System

   ## Uncomment to see information about your system
   ## print(f'>> My system current version: Python {CurrentVersion}')
   ## print(f'>> Required version to run: Python {TargetVersion}')

   def CheckVersion():
      ## Note: if this key is set to False, the system won`t run even if meets requirements
      AllowKey = True
      ## Note: if this key is set to False, the system won`t run even if meets requirements

      ## Note: if this key is set to True, the system will warn evertime it runs
      ShowWarn = True
      ## Note: if this key is set to True, the system will warn evertime it runs

      if TargetVersion == CurrentVersion:
         return
      else:
         if MajorVersion < TargetMajor:
            AllowKey = False
            ShowWarn = True
         else:
            if MinorVersion < TargetMinor:
               AllowKey = False
               ShowWarn = True
            else:
               if BuildVersion < TargetBuild:
                  AllowKey = False
                  ShowWarn = True

      if AllowKey == False:
         Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)
      
      if ShowWarn == True:
         Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)

   def InstallDependencies():
      print("=" * 80)
      print(">> INSTALL DEPENDENCIES <<")
      print("=" * 80)
      UserInput = str(input("[!] >> Do you wish to install dependencies? [Y/n]: "))

      if UserInput == "Y" or UserInput == "y" or UserInput == "1":
         # show pip version
         print("=" * 80)
         print("[!]: PIP Version: [Getting information about installed PIP version...]")
         print("=" * 80)
         cmd = subprocess.getoutput("pip --version")
         print("Details: ", cmd)
         print("=" * 80)

         # Update pip
         print()
         print("=" * 80)
         print("[!]: Checking necessary packages: [Updating pip e pip3]")
         print("=" * 80)
         cmd = subprocess.getoutput("pip install --upgrade pip")
         print("Details: ", cmd)
         cmd = subprocess.getoutput("pip3 install --upgrade pip")
         print("Details: ", cmd)
         print("=" * 80)
         
         # Install Requests
         print()
         print("=" * 80)
         print("[!]: Checking necessary packages: [Installing/updating requests]")
         print("=" * 80)
         cmd = subprocess.getoutput("pip install requests")
         print("Details: ", cmd)
         print("=" * 80)
      else:
         print("=" * 80)
         return

   CheckVersion()