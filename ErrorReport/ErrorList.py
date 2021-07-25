## ErrorList File
## This file contains events thats raised when the program must to stop

class RequirementsCheck():
   def MajorVersion(self, CurrentVersion, TargetVersion, TargetMajor):
      raise Exception(f'>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')

   def MinorVersion(self, CurrentVersion, TargetVersion, TargetMinor):
      print("="*80)
      print(">> PYBRIDGE <<")
      print("="*80)
      print(">> WARNING <<")
      print("="*80)
      print(f'>> Your appication targets a version of Python older than the version currently installed. You may get errors during the process')
      print("-"*80)
      print(f'- Current Version: {CurrentVersion}')
      print(f'- Target Version: {TargetVersion}')
      print(f'>> You can change requirements in `SystemRequirements.py` on `ErrorReport` Module')

      print("-"*80)

   def BuildVersion(self, CurrentVersion, TargetVersion, BuildVer):
      raise Exception(f'>> This application only can run on Python {TargetVersion}. [Current Version: {CurrentVersion}]')

def Requirements():
   return RequirementsCheck()

def ImportLib():
   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

def FileExists():
   raise RuntimeError(">> The file already exists!")

def DirectoryExists():
   raise RuntimeError(">> The directory already exists!")

