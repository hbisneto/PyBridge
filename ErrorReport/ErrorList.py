## ErrorList File
## This file contains events thats raised when the program must to stop

def ImportLib():
   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

def FileExists():
   raise RuntimeError(">> The file already exists!")

def DirectoryExists():
   raise RuntimeError(">> The directory already exists!")

