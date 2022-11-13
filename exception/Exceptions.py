## Exceptions File
## This file contains events that's raised when the program must to stop

class Raise:
  def MajorVersion(self, CurrentVersion, TargetVersion, TargetMajor):
    raise Exception(f'>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')

  def MinorVersion(self, CurrentVersion, TargetVersion, TargetMinor):
    print('=' * 80)
    print(">> PYBRIDGE <<")
    print('=' * 80)
    print(">> WARNING <<")
    print('=' * 80)
    print(f'>> Your appication targets a version of Python older than the version currently\ninstalled. You may get errors during the process')
    print('=' * 80)
    print(f'- Current Version: {CurrentVersion}')
    print(f'- Target Version: {TargetVersion}')
    print(f'>> You can change `Requirements.py` on `system` Module')
    print('=' * 80)
    print()

  def BuildVersion(self, CurrentVersion, TargetVersion, BuildVer):
    raise Exception(f'>> This application only can run on Python {TargetVersion}. [Current Version: {CurrentVersion}]')

  def __init__(self, exctype):
    self.exctype = exctype

  def FileExists(self):
    raise Exception(f'{self.exctype} The file already exists')
  
  def DirectoryExists(self):
    raise Exception(f'{self.exctype} The directory already exists')
  
  def ImportLib():
   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

  def InputFormat(self):
    print("=" * 80)
    print(f'{self.exctype} INVALID INPUT')
    print("=" * 80)
    print(">> Your input is not valid: Check your input and try again\n\n")
    print("=" * 80)
  
  def ProgramQuit(self):
    print("=" * 80)
    print(f'{self.exctype} PYBRIDGE HAS QUIT!')
    print("=" * 80)
    print(f'>> The program has been closed and couldn`t be restored.\n>> Run the program again!')
    print("=" * 80)

  def InvalidOption(self):
    print("=" * 80)
    print(f'{self.exctype} INVALID OPTION')
    print("=" * 80)
    print(f'>> You typed an invalid option.\n>> Running the program again!')
    print("=" * 80)

  def ProjectsLoadFail(self):
    print("=" * 80)
    print(f'{self.exctype} PROJECT LOADING FAILED!')
    print("=" * 80)
    print(f'>> ERROR: Couldn`t load projects...')
    print("=" * 80)

  def BackupFail(self):
    print("=" * 80)
    print(f'{self.exctype} BACKUP CREATION FAILED!')
    print("=" * 80)
    print("*" * 80)
    print(f'>> PyBridge could not create backup for your projects folder')
    print(f'>> Try again later.')
    print("*" * 80)

  def CompressBackupFail(self):
    print("=" * 80)
    print(f'{self.exctype} COMPRESSED FILE CREATION FAILED!')
    print("=" * 80)
    print("*" * 80)
    print(f'>> PyBridge could not create a compressed file from your backup')
    print(f'>> Try again later.')
    print("*" * 80)

Throw = Raise(">> An Exception occurred:")