# CreateCore.py
## Creates the Core.py library for all systems automatically

## Native Libraries
from sys import platform
import os
import codecs

CURRENT_DIRECTORY = os.getcwd()
LINUX_MODULE_LOCATION = CURRENT_DIRECTORY + "/linux/"
MAC_MODULE_LOCATION = CURRENT_DIRECTORY + "/mac/"
WINDOWS_MODULE_LOCATION = CURRENT_DIRECTORY + "/windows/"
CORE_FILE = "Core.py"
TEST_CORE_FILE = "TestCore.py"

SourceFileContent = []

print("[!] - Current Directory:", CURRENT_DIRECTORY)


# def CreateLinuxCore():
#     print("Linux Passed!")

def CreateMacCore():
    print("Mac Passed!")
    print(">> Mac Module Location:", MAC_MODULE_LOCATION)
    with open(MAC_MODULE_LOCATION + CORE_FILE) as f:
        SourceFileContent = f.readlines()
    
    for i in SourceFileContent:
        print(">> TEXT", i)
        with codecs.open(LINUX_MODULE_LOCATION + TEST_CORE_FILE, "a", "utf-8-sig") as CoreFile:
            CoreFile.write(i)
            CoreFile.close()

# def CreateWindowsCore():
#     print("Windows Passed!")

## Linux
# if platform == "linux" or platform == "linux2":
#     print("Linux Passed!")
#     # CreateLinuxCore()

## Mac    
if platform == "darwin":
    # print("Mac Passed!")
    CreateMacCore()
    
## Windows
# elif platform == "win32" or platform == "win64":
#     print("Windows Passed!")
#     # CreateWindowsCore()