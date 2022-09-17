## Requirements File
## This file is used to check if system matches with the minimum requirements to run

import sys
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

   def CheckMajorVersion():
      ## Note: if this key is set to False, the system won't run even if meets requirements
      AllowKey = True
      ## Note: if this key is set to False, the system won't run even if meets requirements
      
      if MajorVersion < TargetMajor:
         AllowKey = False
      else:
         if MinorVersion < TargetMinor:
             AllowKey = False
         else:
             if BuildVersion < TargetBuild:
                 AllowKey = False
                 
      if AllowKey == False:
         # Exceptions.Raise().Requirements().MajorVersion(CurrentVersion, TargetVersion, TargetMajor)
         Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)

   def CheckMinorVersion():
      ## Note: if this key is set to True, the system will warn evertime it runs
      ShowWarn = False
      ## Note: if this key is set to True, the system will warn evertime it runs
      
      if MajorVersion > TargetMajor:
         ShowWarn = True
      else:
         if MinorVersion > TargetMinor:
             ShowWarn = True
         else:
             if BuildVersion > TargetBuild:
                 ShowWarn = True
                 
      if ShowWarn == True:
         # Exceptions.Raise().Requirements().MinorVersion(CurrentVersion, TargetVersion, TargetMinor)
         Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)

   CheckMajorVersion()
   CheckMinorVersion()