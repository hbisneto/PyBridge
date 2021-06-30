## ErrorList File
## This file contains events thats raised when the program must to stop

def ImportLib():
   raise RuntimeError(">> Could Not Import Library: Check if the libraries are installed and run the program again.")

def FileExists():
   raise RuntimeError(">> The File Already Exists!")

def DirectoryExists():
   raise RuntimeError(">> The Directory Already Exists!")

