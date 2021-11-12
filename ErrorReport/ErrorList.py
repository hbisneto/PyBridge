## ErrorList File
## This file contains events that's raised when the program must to stop

class Raise():
   class Requirements():
      def MajorVersion(self, CurrentVersion, TargetVersion, TargetMajor):
         raise Exception(f'\n\n>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')

      def MinorVersion(self, CurrentVersion, TargetVersion, TargetMinor):
         print("="*40)
         print(">> PYBRIDGE <<")
         print("="*40)
         print(">> WARNING <<")
         print("="*40)
         print(f'>> Your appication targets a version of Python older than the version currently\ninstalled. You may get errors during the process')
         print("="*40)
         print(f'- Current Version: {CurrentVersion}')
         print(f'- Target Version: {TargetVersion}')
         print(f'>> You can change `SystemRequirements.py` on `ErrorReport` Module')
         print("="*40)
         print()

      def BuildVersion(self, CurrentVersion, TargetVersion, BuildVer):
         raise Exception(f'>> This application only can run on Python {TargetVersion}. [Current Version: {CurrentVersion}]')

def ImportLib():
   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

def FileExists():
   raise RuntimeError(">> The file already exists!")

def DirectoryExists():
   raise RuntimeError(">> The directory already exists!")

def InputFormat():
   print("\n\n>> Your input is not valid: Check your input and try again\n\n")

def InvalidOption():
   print("="*80)
   print(">> Invalid Option!")
   print("="*80)
   print(f'>> You typed an invalid option.\n>> Running the program again!')
   print("="*80)

def BackupFail():
   print("="*80)
   print(">> BACKUP CREATION FAILED!")
   print("="*80)
   print("[!]" * 20)
   print(f'>> PyBridge could not create backup for your project folder')
   print(f'>> Try again later.')
   print("[!]" * 20)
