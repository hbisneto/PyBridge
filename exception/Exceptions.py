## ErrorList File
## This file contains events that's raised when the program must to stop
WarnSpacing = '\n\n\n'

class Raise:
  # class Requirements():
  def MajorVersion(self, CurrentVersion, TargetVersion, TargetMajor):
    raise Exception(f'{WarnSpacing}>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')

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
    print(f'>> You can change `Requirements.py` on `system` Module')
    print("="*40)
    print()

  def BuildVersion(self, CurrentVersion, TargetVersion, BuildVer):
    raise Exception(f'>> This application only can run on Python {TargetVersion}. [Current Version: {CurrentVersion}]')


  def __init__(self, exctype):
    self.exctype = exctype

  def FileExists(self):
    raise Exception(f'{WarnSpacing}{self.exctype} The file already exists')
  
  def DirectoryExists(self):
    raise Exception(f'{WarnSpacing}{self.exctype} The directory already exists')
  
  def ImportLib():
   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

  def InputFormat():
    print(">> Your input is not valid: Check your input and try again\n\n")
  
  def ProgramQuit(self):
    print("=" * 80)
    print(f'{self.exctype} The program was already closed!')
    print("=" * 80)
    print(f'>> The program has been closed and couldn`t be restored.\n>> Run the program again!')
    print("=" * 80)

  def InvalidOption(self):
    print(f'{WarnSpacing}')
    print("=" * 80)
    print(f'{self.exctype} Invalid Option!')
    print("=" * 80)
    print(f'>> You typed an invalid option.\n>> Running the program again!')
    print("=" * 80)

  def ProjectsLoadFail():
    print("=" * 80)
    print(f'>> ERROR: Couldn`t load projects...')
    print("=" * 80)

  def BackupFail(self):
    print("=" * 80)
    print(f'{self.exctype} BACKUP CREATION FAILED!')
    print("=" * 80)
    print("*" * 40)
    print(f'>> PyBridge could not create backup for your projects folder')
    print(f'>> Try again later.')
    print("*" * 40)

  def CompressBackupFail(self):
    print("=" * 80)
    print(f'{self.exctype} COMPRESSED FILE CREATION FAILED!')
    print("=" * 80)
    print("*" * 40)
    print(f'>> PyBridge could not create a compressed file from your backup')
    print(f'>> Try again later.')
    print("*" * 40)

Throw = Raise(">> An Exception occurred:")
