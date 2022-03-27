## SystemRequirements File
## This file is used to check if system matches with the minimum requirements to run

import sys
from exception import Exceptions

## Change "Require" to "False" to skip system check
Require = True
## Change "Require" to "True" to allow system check

if Require == True:
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

   if TargetVersion > CurrentVersion:
      Exceptions.Raise().Requirements().MajorVersion(CurrentVersion, TargetVersion, TargetMajor)
   elif TargetVersion < CurrentVersion:
      Exceptions.Raise().Requirements().MinorVersion(CurrentVersion, TargetVersion, TargetMinor)

